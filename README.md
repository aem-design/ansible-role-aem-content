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
  roles:
    - { role: aem_design.aem_license,
      aem_license_key: "your key",
      aem_license_name: "your company",
      aem_port: "4502",
      aem_host: "localhost",
    }
```

## License

Apache 2.0

## Author Information

This role was created by [Max Barrass](https://aem.design/).