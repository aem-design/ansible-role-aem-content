# Ansible Role: AEM Content

[![Build Status](https://travis-ci.org/aem-design/ansible-role-aem-content.svg?branch=master)](https://travis-ci.org/aem-design/ansible-role-aem-content)

Perform actions on content in AEM.
> This role was developed as part of
> [AEM.Design](http://aem.design/)

## Requirements

None.

## Content Actions

| Name           	| aem_content_action 	| Example                                                                                                                                                                  	|
|----------------	|--------------------	|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| Set Permission 	| set_permission     	| - { <br>&nbsp;&nbsp;user_or_group_name: 'exporter',<br>&nbsp;&nbsp;path: '/',<br>&nbsp;&nbsp;permissions: 'read:true,modify:false,create:false,delete:false,acl_read:false,acl_edit:false,replicate:false' <br>} 	|
| Set Property   	| set_property       	| - { <br>&nbsp;&nbsp;path: '/',<br>&nbsp;&nbsp;property_name: 'sling:target',<br>&nbsp;&nbsp;property_value: '/projects' <br>   }                                                                       	|

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

| Name                     	| Required 	| Default                                          	| Notes                                                 	|
|--------------------------	|----------	|--------------------------------------------------	|-------------------------------------------------------	|
|                          	|          	|                                                  	|                                                       	|
| aem_port                 	|          	| 4502                                           	| aem service port                                      	|
| aem_host                 	|          	| localhost                                      	| aem service host                                      	|
| aem_username           	|          	| admin                                             |                                                           |
| aem_password           	|          	| admin                                             |                                                           |
|                          	|          	|                                                  	|                                                       	|
| wait_delay               	|          	| 1                                                	| how long to wait between retries                      	|
| wait_timeout            	|          	| 1                                                	| how long to wait before terminating                      	|
| wait_retries            	|          	| 1                                                	| how many times to retry waiting                        	|
|                          	|          	|                                                  	|                                                       	|
| aem_content_action        |          	|                                                   | set Content Action to perform                             |
| aem_content_list          |          	|                                                   | content list to run action with                           |
|                          	|          	|                                                  	|                                                       	|


## Dependencies

None.

## Example Playbook

```yaml
- hosts: all
  tasks:
    - name: set permissions
      include_role:
        name: "{{ role_name }}"
      vars:
        aem_port: "{{ test_aem_port }}"
        aem_host: "{{ dockerhost_ip.stdout }}"
        aem_content_action: "set_permission"
        aem_content_list:
          - {
            user_or_group_name: 'everyone',
            path: '/libs/granite/dispatcher/content/vanityUrls',
            permissions: 'read:true'
          }
        debug_hide: false
    - name: set property
      include_role:
        name: "{{ role_name }}"
      vars:
        aem_port: "{{ test_aem_port }}"
        aem_host: "{{ dockerhost_ip.stdout }}"
        aem_content_action: "set_property"
        aem_content_list:
          - {
            path: '/libs/granite/dispatcher/content/vanityUrls',
            property_name: 'test',
            property_value: "{{ test_aem_property_content }}"
          }
        debug_hide: false
```

## License

Apache 2.0

## Author Information

This role was created by [Max Barrass](https://aem.design/).