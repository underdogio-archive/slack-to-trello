# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  # Use Ubuntu 14.04 64 bit as our platform
  # https://atlas.hashicorp.com/ubuntu/boxes/trusty64
  config.vm.box = "ubuntu/trusty64"

  # Open up ports for our application and PostgreSQL
  config.vm.network "forwarded_port", guest: 5000, host: 5000

  # Give more than the standard amount of CPUs and RAM
  config.vm.provider "virtualbox" do |vb|
    vb.cpus = 2
    vb.memory = "2048"
  end

  # Provision our VM via a bash script
  config.vm.provision "shell", path: "bin/bootstrap-vagrant.sh"
end
