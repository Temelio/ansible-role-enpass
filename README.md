# enpass

[![Build Status](https://travis-ci.org/Temelio/ansible-role-enpass.svg?branch=master)](https://travis-ci.org/Temelio/ansible-role-enpass)

Install enpass package.

## Requirements

This role requires Ansible 2.2 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- Debian Jessie
- Ubuntu Xenial

and use:
- Ansible 2.2.x
- Ansible 2.3.x
- Ansible 2.4.x

### Running tests

#### Using Docker driver

```
$ tox
```

## Role Variables

### Default role variables

``` yaml
# Installation mode
enpass_install_from_repository: "{{ _enpass_install_from_repository }}"

# Repository management
enpass_apt_cache_valid_time: 3600
enpass_repository_gpg_keys: "{{ _enpass_repository_gpg_keys }}"
enpass_repositories: "{{ _enpass_repositories }}"

# Packages
enpass_packages: "{{ _enpass_packages }}"
enpass_system_dependencies: "{{ _enpass_system_dependencies }}"
```

### Debian OS family role variables

``` yaml
# Installation mode
_enpass_install_from_repository: True

# Repository management
_enpass_repository_gpg_keys:
  - url: 'https://dl.sinew.in/keys/enpass-linux.key'
_enpass_repositories:
  - repo: 'deb http://repo.sinew.in/ stable main'
    filename: 'enpass'

# Packages
_enpass_packages:
  - name: 'enpass'
_enpass_system_dependencies:
  - name: 'ca-certificates'
  - name: 'libxss1'
  - name: 'lsof'
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: Temelio.enpass }
```

## License

MIT

## Author Information

Alexandre Chaussier (for Temelio company)
- http://www.temelio.com
- alexandre.chaussier [at] temelio.com
