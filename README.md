# Ansible EnvKey

This is a lookup plugin for using [EnvKey](https://envkey.com) as a secret store with [Ansible](https://www.ansible.com).

## Installation

Checkout this repo wherever you like and then point to it in your `ansible.cfg` file. eg:

    [defaults]
    lookup_plugins = ~/.ansible/ansible-envkey/lookup_plugins/

## Usage

You can use this like any other lookup plugin, for example, to get the Redis password in your group_vars you can do this...

    redis_password: "{{ lookup('envkey','REDIS_PASSWORD') }}"


