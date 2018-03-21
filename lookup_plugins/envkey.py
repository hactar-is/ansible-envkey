# -*- coding: utf-8 -*-

"""
    envkey_lookup
    ~~~~~~~~~~~~~
    A lookup plugin for getting variables from EnvKey
"""

from __future__ import absolute_import, unicode_literals, division, print_function

import os
from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError


class EnvKeyException(AnsibleError):
    pass


try:
    import envkey  # NOQA
except ValueError:
    ek = os.environ.get('ENVKEY', None)
    if ek is None:
        raise EnvKeyException('EnvKey missing')
    else:
        raise EnvKeyException('EnvKey "{}" is invalid'.format(ek))


__metaclass__ = type


DOCUMENTATION = """
    lookup: envkey
    author:
      -  Hactar <systems@hactar.is>
    requirements:
      - enkey python package - pip(env) install envkey
      - Must have set an envkey in the current shell - export ENVKEY=yoursecretenvkeygoeshere
    short_description: Look up secrets in EnvKey
    description:
      - An Ansible lookup plugin for retrieving secrets from EnvKey - https://www.envkey.com
"""

EXAMPLES = """
- debug: msg="Secret provided by envkey: {{ lookup('envkey','MY_SECRET') }}"
"""

RETURN = """
  _list:
    description:
      - values from the environment variables.
    type: list
"""


class LookupModule(LookupBase):

    def run(self, terms, variables, **kwargs):
        """Something something magic.

        Args:
            terms (list): The variable names to look up
            variables (list, Optional): A list of varaibles already available
            **kwargs: Any additional keyword args

        Returns:
            list: A list of converted variables I think
        """
        try:
            return [os.environ.get(var, '') for var in terms]
        except Exception:
            raise EnvKeyException('Some kind of error soz.')
