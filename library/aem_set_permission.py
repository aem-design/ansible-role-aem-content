#!/usr/bin/python

from ansible.module_utils.basic import *

import pyaem2


def main():
    fields = {
        "host": {"required": True, "type": "str"},
        "port": {"required": True, "type": "str"},
        "user_or_group_name": {"required": True, "type": "str"},
        "path": {"required": True, "type": "str"},
        "permissions": {"required": True, "type": "str"},
        "aem_username": {"required": True, "type": "str"},
        "aem_password": {"required": True, "type": "str", "no_log": True}
    }

    module = AnsibleModule(argument_spec=fields)

    host = module.params['host']
    port = module.params['port']
    user_or_group_name = module.params['user_or_group_name']
    path = module.params['path']
    permissions = module.params['permissions']

    aem_username = module.params['aem_username']
    aem_password = module.params['aem_password']

    try:
        aem = pyaem2.PyAem2(aem_username, aem_password, host, port)

        result = aem.set_permission(user_or_group_name, path, permissions)

        module.exit_json(
            failed=False,
            changed='set on path' in result.message,
            msg=result.message
        )

    except pyaem2.PyAem2Exception as err:
        module.fail_json(
            failed=True,
            changed=False,
            host=host,
            port=port,
            username=aem_username,
            password=aem_password,
            msg=str(err),
            installed=False
        )


if __name__ == '__main__':
    main()