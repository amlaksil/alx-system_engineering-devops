# Configuration management
## Requirements
* All files are interpreted on Ubuntu 20.04 LTS
* Puppet manifests must pass `puppet-lint` version 2.1.1 
## Install puppet
```
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet
```
## Install `puppet-lint`
```$ gem install puppet-lint```
