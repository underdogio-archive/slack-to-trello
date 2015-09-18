#!/usr/bin/env bash
# Navigate to the vagrant folder
cd /vagrant/

# Enable our virtualenv for all scenarios
echo "Enabling virtualenv" 1>&2
workon slack-to-trello

# Start our server
echo "Starting slack-to-trello server" 1>&2
./run.sh
