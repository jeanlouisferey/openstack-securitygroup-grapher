#!/usr/bin/python

# Copyright (c) 2014 Hewlett-Packard Development Company, L.P.
# Modified by Serge Huraux from os_port to os_security_groups_facts
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>.

import fnmatch

try:
    import shade
    from shade import meta
    HAS_SHADE = True
except ImportError:
    HAS_SHADE = False

DOCUMENTATION = '''
---
module: os_security_groups_facts
short_description: list all security_groups and security_groups_rules of a project
version_added: "2.0"
description:
    - Retrieve facts about security_groups instances from OpenStack.
notes:
    - This module creates a new top-level C(openstack_security_groups) fact, which
      contains a list of security_groups and their rules.
requirements:
    - "python >= 2.6"
    - "shade"
options:
     no options at this time
 extends_documentation_fragment: openstack
'''

EXAMPLES = '''
# Gather facts about all security_groups :
- os_security_groups_facts:
    cloud: rax-dfw
    security_groups: web*
- debug:
    var: openstack_security_groups
'''


def main():

    argument_spec = openstack_full_argument_spec(
        security_group=dict(required=False),
        filters=dict(required=False, type='dict', default=None),
    )

#    module_kwargs = openstack_module_kwargs()
#    module = AnsibleModule(argument_spec, **module_kwargs)

    module = AnsibleModule(argument_spec)

    if not HAS_SHADE:
        module.fail_json(msg='shade is required for this module')

#    security_group =module.params.pop('security_group') 
#    filters = module.params.pop('filters')

    try:
        cloud = shade.openstack_cloud(**module.params)
        openstack_security_groups = cloud.list_security_groups()

        module.exit_json(changed=False, ansible_facts=dict(
            openstack_security_groups=openstack_security_groups)) 

    except shade.OpenStackCloudException as e:
        module.fail_json(msg=str(e))

# this is magic, see lib/ansible/module_common.py
from ansible.module_utils.basic import *
from ansible.module_utils.openstack import *
if __name__ == '__main__':
    main()
