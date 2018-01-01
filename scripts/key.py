"""
SSH key operations
"""
import os
import password
import ssh
import user
from fabric.api import env
from fabric.api import put
from fabric.api import run
from fabric.api import sudo
from fabric.contrib.files import append
from fabric.contrib.files import contains
from fabric.contrib.files import uncomment

env.hosts = [os.getenv('REMOTE_HOST')]


# def use_keys():
#     """
#     Setup key access to the remote server
#     """
#     print('Use keys')
#     env.user = os.getenv('ROOT_REMOTE_USERNAME')
#     private_key_filename = os.getenv('ROOT_PRIVATE_KEY_FILENAME')
#     ssh_keys_path = os.getenv('CONTAINER_SSH_KEYS_PATH')
#     print('User is {0}, private key filename {1}, docker key path is {2}'
#           .format(env.user, private_key_filename, ssh_keys_path))
#     env.key_filename = os.path.join(
#         '/', ssh_keys_path, private_key_filename)
#     print('Key filename is {0}'.format(env.key_filename))


def key_remote_test():
    """
    A small test to check if you can access your remote server using a key,
    it will try to get details about the operating system
    """
    # use_keys()
    print('Key remote test against hosts {0}'.format(env.hosts))
    run('uname -a')


# def disable_write_authorized_keys(username):
#     """
#     Disable to write the SSH keys
#     """
#     print('Disable write authorized keys for user {0}'.format(username))
#     sudo('chmod u-w /home/{name}/.ssh/authorized_keys'.format(name=username))


# def enable_write_authorized_keys(username):
#     """
#     Enable to write the SSH keys
#     """
#     print('Enable write authorized keys for user{0}'.format(username))
#     sudo('touch /home/{name}/.ssh/authorized_keys'.format(name=username))
#     sudo('chmod u+w /home/{name}/.ssh/authorized_keys'.format(name=username))


# def tell_key_does_not_need_password(username):
#     """
#     Indicate that the keys does not need a password
#     """
#     print('Tell key does not need password for user {0}'.format(username))
#     condition = '{name} ALL=(ALL) NOPASSWD: ALL'.format(name=username)
#     if not contains('/etc/sudoers', condition):
#         append('/etc/sudoers', condition, use_sudo=True)


# def authorize_keys():
#     """
#     Authorize the use of SSH keys authentication
#     """
#     print('Authorize keys')
#     uncomment('/etc/ssh/sshd_config', '#AuthorizedKeysFile', use_sudo=True)


# def prepare_keys_directory(username):
#     """
#     Create the SSH keys directory
#     """
#     print('Prepare keys directory for user {0}'.format(username))
#     sudo('mkdir -p /home/{name}/.ssh'.format(name=username))


# def tell_user_own_key(username):
#     """
#     Make the user owner of the SSH key
#     """
#     print('Tell that the user {0} owns the key'.format(username))
#     sudo('chown {name} /home/{name}/.ssh/authorized_keys'
#          .format(name=username))


# def upload_key_for_user(username, key_path):
#     """
#     Upload the SSH keys for a username
#     """
#     print('Upload key {0} for user {1}'.format(key_path, username))
#     """
#     TODO: Instead of overwriting the keys,
#     I should append if not already present
#     """
#     put(key_path, '/home/{name}/.ssh/authorized_keys'.format(name=username))


# def setup_key_access(username, key_path):
#     """
#     Prepare access using keys instead of password
#     """
#     print('Setup key access for user {0} and path {1}'
#           .format(username, key_path))
#     use_keys()
#     user.create_user(username)
#     prepare_keys_directory(username)
#     enable_write_authorized_keys(username)
#     upload_key_for_user(username, key_path)
#     disable_write_authorized_keys(username)
#     tell_user_own_key(username)
#     tell_key_does_not_need_password(username)
#     authorize_keys()
#     password.disable_password_authentication()
#     ssh.restart()
