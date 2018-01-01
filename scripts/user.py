"""
User details
"""
from fabric.api import sudo
# pylint: disable=C0325


def create_user(username):
    """
    Create a new user in the server
    """
    print('Create user {0}'.format(username))
    sudo('id -u {name} &>/dev/null || useradd --user-group \
         --create-home --shell /bin/bash {name} || true'.format(name=username))
    print('User created successfully')
