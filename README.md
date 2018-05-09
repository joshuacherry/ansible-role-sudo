# ansible-role-sudo

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/joshuacherry/ansible-role-sudo.svg?branch=master)](https://travis-ci.org/joshuacherry/ansible-role-sudo)
![Ansible](https://img.shields.io/badge/ansible-2.4.3.0-blue.svg)
![Ansible](https://img.shields.io/badge/ansible-2.5.0-blue.svg)

Configures sudo users on a linux server.

## Requirements

- Ansible
  - Tested Versions:
    - 2.4.3.0
    - 2.5.0

## Install

### Install from GitHub

`ansible-galaxy install git+https://github.com/joshuacherry/ansible-role-sudo.git`

## Features

| OS            |
| :------------ |
| Ubuntu 16.04  |
| Centos 7      |

## Versioning

[Semantic Versioning](http://semver.org/)

For the versions available, see the [tags on this repository](https://github.com/joshuacherry/ansible-role-sudo/tags).

Additionaly you can see what change in each version in the [CHANGELOG.md](CHANGELOG.md) file.

## Role variables

Look to the [defaults](defaults/main.yml) properties file to see the possible configuration properties.

## Testing

This role includes a Vagrantfile used with a Docker-based test harness. Using Vagrant allows all contributors to test on the same platform and avoid false test failures due to untested or incompatible docker versions.

1. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/).
1. Run `vagrant up` from the same directory as the Vagrantfile in this repository.
1. SSH into the VM with: `vagrant ssh`
1. Run tests with `molecule`.

### Testing with Docker and tox

Tox will test against the configured dependencies in [tox.ini](tox.ini). This allows you to test the role against multiple version of ansible, molecule, python, and more. Once the dependencies are set, tox will run the same molecule command to test code.

```bash
cd /ansible-role-sudo
tox
```

### Testing with Docker and molecule

```bash
cd /ansible-role-sudo
molecule test
```

See `molecule` for more information including a full list of available commands.

### interactive debugging

You can use log into a docker image created by molecule for interactive testing with the below commands.

```bash
cd /ansible-role-sudo
molecule converge
# Ubuntu
docker exec -it ubuntu /bin/bash
# CentOS
docker exec -it centos /bin/bash
```

## Example Playbook

```yaml
---
- name: Playbook for ansible-role-sudo
  hosts: all

  tasks:
  - include_role:
      name: ansible-role-sudo
```