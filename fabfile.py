from fabric.api import env
from webdev_fab import set_project_defaults
from webdev_fab.tasks import *
from webdev_fab.tasks.django import *

# See webdev-fab documentation for details

env.user = '{{ project_name }}'

# A shortcut to set 'db', 'db_user', 'group' and 'project' values equal
# to 'user', which are required for this tasks to function
set_project_defaults(env.user)

# Default list of hosts to run tasks on
if not env.hosts:
    env.hosts = ['somehost.yourteam.com:2222']

# The user with full sudo privileges, defaults to the user running 'fab'
# env.poweruser = 'privilegedusername'

# Fabric can utilize some ~/.ssh/config shortcuts
#env.use_ssh_config = True

# A group to own project/tmp directory with fcgi socket/pid files, defaults
# to 'nginx'
#env.webserver_group = 'www-data'
