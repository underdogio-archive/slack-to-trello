#!/usr/bin/env bash
# If there is an error, exit early
set -e

# Update apt-get
if ! test -f .updated-apt-get; then
  sudo apt-get update
  touch .updated-apt-get
fi

# Install pip
if ! which pip &> /dev/null; then
  sudo apt-get install -y python-setuptools python-pip
fi

# Upgrade pip
if ! pip --version | grep 'pip 7.1.0' &> /dev/null; then
  sudo pip install pip==7.1.0
fi

# Install git
if ! which git &> /dev/null; then
  sudo apt-get install -y git
fi

# Install PostgreSQL and psycopg2 dependencies
if ! which psql &> /dev/null; then
  # Setup PostgreSQL 9.3 for our database
  sudo apt-get install -y postgresql-9.3 postgresql-server-dev-9.3 python-dev
fi

# Set up PostgreSQL 9.3 configuration
# Modified from https://github.com/twolfson/vagrant-nodebugme/blob/1.0.0/bin/bootstrap.sh#L26-L54
# If we can't open `psql` as `vagrant`
psql_port=5432
echo_command="psql --port=\"$psql_port\" --db postgres --command \"SELECT 'hai';\""
if ! sudo su --command "$echo_command" vagrant &> /dev/null; then
  # Set up `vagrant` user in PostgreSQL
  create_user_command="psql --port=\"$psql_port\" --command \"CREATE ROLE vagrant WITH SUPERUSER CREATEDB LOGIN;\""
  sudo su --command "$create_user_command" postgres

  # Set up `slack-to-trello` user in PostgreSQL
  create_user_command="psql --port=\"$psql_port\" --command \"CREATE ROLE \\\"slack-to-trello\\\" WITH SUPERUSER LOGIN;\""
  sudo su --command "$create_user_command" postgres
  set_user_password="psql --port=\"$psql_port\" --command \"ALTER ROLE \\\"slack-to-trello\\\" WITH PASSWORD 'slack-to-trello';\""
  sudo su --command "$set_user_password" postgres

  # Create an `slack-to-trello` database
  create_db_command="createdb --port=\"$psql_port\" slack-to-trello"
  sudo su --command "$create_db_command" postgres
fi

# Set up quick start scripts
if ! test -f /home/vagrant/start-slack-to-trello.sh; then
  ln -s /vagrant/bin/start-slack-to-trello.sh /home/vagrant/start-slack-to-trello.sh
fi

# Copy over PostgreSQL security policies to allow Vagrant host access
# DEV: We always run this to guarantee PostgreSQL has the proper host IP address
# How to open a PostgreSQL to the world http://stackoverflow.com/questions/14139017/cannot-connect-to-postgres-running-on-vm-from-host-machine-using-md5-method
# How to host machine IP address http://stackoverflow.com/questions/19917148/tell-vagrant-the-ip-of-the-host-machine
cp -f /vagrant/data/development/etc/postgresql/9.3/main/pg_hba.conf /tmp/pg_hba.conf
host_ip="$(netstat -rn | grep "^0.0.0.0 " | cut -d " " -f10)"
echo "host    all             all             $host_ip/0              md5" >> /tmp/pg_hba.conf
sudo cp /vagrant/data/development/etc/postgresql/9.3/main/postgresql.conf /etc/postgresql/9.3/main/postgresql.conf
sudo cp /tmp/pg_hba.conf /etc/postgresql/9.3/main/pg_hba.conf
sudo /etc/init.d/postgresql restart
