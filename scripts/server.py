"""
Prepare a server for access
"""
import os
import docker_setup
import key
from fabric.api import env
# pylint: disable=W0511
# pylint: disable=C0325


def prepare_new():
    """
    Get a server and make it ready to be used in production
    """
    print('Prepare new server')
    env.user = os.getenv('REMOTE_ROOT_USERNAME')
    env.password = os.getenv('REMOTE_ROOT_PASSWORD')
    username = os.getenv('REMOTE_USERNAME')
    public_key_filename = os.getenv('PUBLIC_KEY_FILENAME')
    ssh_keys_path = os.getenv('CONTAINER_SSH_KEYS_PATH')
    public_key_path = os.path.join('/', ssh_keys_path, public_key_filename)
    key.setup_key_access(username, public_key_path)
    docker_setup.setup_with_deploy_user()

def setup_new_no_root():
    """
    Get a server with key access only
    and make it ready to be used in production
    """
    print('Prepare new server without using password')
    # env.user = os.getenv('REMOTE_ROOT_USERNAME')
    # env.password = os.getenv('REMOTE_ROOT_PASSWORD')
    ssh_keys_path = os.getenv('CONTAINER_SSH_KEYS_PATH')

    root_public_key_filename = os.getenv('ROOT_PUBLIC_KEY_FILENAME')
    root_username = os.getenv('ROOT_REMOTE_USERNAME')
    root_public_key_path = os.path.join(
        '/', ssh_keys_path, root_public_key_filename)
    key.setup_key_access(root_username, root_public_key_path)

    deploy_public_key_filename = os.getenv('DEPLOY_PUBLIC_KEY_FILENAME')
    deploy_username = os.getenv('DEPLOY_REMOTE_USERNAME')
    deploy_public_key_path = os.path.join(
        '/', ssh_keys_path, deploy_public_key_filename)
    key.setup_key_access(deploy_username, deploy_public_key_path)

    docker_setup.setup_for_user(deploy_username)
