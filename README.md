# ansible-role-sudo

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/joshuacherry/ansible-role-sudo.svg?branch=master)](https://travis-ci.org/joshuacherry/ansible-role-sudo)
![Ansible](https://img.shields.io/badge/ansible-2.8-blue.svg)
![Ansible](https://img.shields.io/badge/ansible-2.9-blue.svg)

Configures sudo users on a linux server.

## Requirements

- Ansible
  - Tested Versions:
    - 2.8
    - 2.9

## Install

### Install from GitHub

`ansible-galaxy install git+https://github.com/joshuacherry/ansible-role-sudo.git`

## Features

| Operating System   |
| :----------------- |
| Ubuntu 16.04       |
| Ubuntu 18.04       |
| Centos 7           |
| Centos 8           |

## Versioning

[Semantic Versioning](http://semver.org/)

For the versions available, see the [tags on this repository](https://github.com/joshuacherry/ansible-role-sudo/tags).

Additionally you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Role variables

Look to the [defaults](defaults/main.yml) properties file to see the possible configuration properties.

## Testing

This role includes a Vagrantfile used with a Docker-based test harness that approximates the Travis CI setup for integration testing. Using Vagrant allows all contributors to test on the same platform and avoid false test failures due to untested or incompatible docker versions.

This molecule configuration depends on docker images from [https://hub.docker.com/u/joshuacherry/](https://hub.docker.com/u/joshuacherry/) to quickly test the role against a variety of operating systems.

1. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/).
1. Run `vagrant up` from the same directory as the Vagrantfile in this repository.
1. SSH into the VM with: `vagrant ssh`
1. Run tests with `molecule`.

### Testing with Docker and tox

Tox will test against the configured dependencies in [tox.ini](tox.ini). This allows you to test the role against multiple version of ansible, molecule, python, and more. Once the dependencies are set, tox will run the same molecule command to test code.

Due to how Virtualbox mounts shared folders, it is recommended to copy the role into a local directory within the virtual machine before running tox, otherwise the python environments will perform significantly slower. Run the below commands each time you make a change to the source code and need to test against all scenarios defined in [tox.ini](tox.ini)

```bash
rsync -ua /ansible-role-sudo/ ~/ansible-role-sudo/ --delete
cd ~/ansible-role-sudo
tox
```

### Testing with Docker and molecule

This method will only test the code with the most recent version of Ansible, tox testing should be used before commits to master so that all scenarios can be tested.

```bash
cd /ansible-role-sudo
molecule test
```

See `molecule` for more information including a full list of available commands.

### interactive debugging

You can use log into a docker image created by molecule for interactive testing with the below commands. As defined in [molecule.yml](molecule/default/molecule.yml), the default instance is set to `ubuntu1604`. If you wish to test other operating systems, you must define the environment variables `MOLECULE_DISTRO` and `MOLECULE_DOCKER_COMMAND`. A table of supported options are below.

```bash
cd /ansible-role-sudo
export MOLECULE_DISTRO=centos7
export MOLECULE_DOCKER_COMMAND=/usr/lib/systemd/systemd
molecule converge
docker exec -it instance /bin/bash
```

| OS            | MOLECULE_DISTRO | MOLECULE_DOCKER_COMMAND  |
| :------------ | :-------------: | :----------------------- |
| Ubuntu 16.04  | ubuntu1604      | /lib/systemd/systemd     |
| ubuntu 18.04  | ubuntu1804      | /lib/systemd/systemd     |
| Centos 7      | centos7         | /usr/lib/systemd/systemd |
| Centos 8      | centos8         | /usr/lib/systemd/systemd |

## Example Playbook

```yaml
---
- name: Playbook for ansible-role-sudo
  hosts: all

  tasks:
  - include_role:
      name: ansible-role-sudo
```