"""
Environment details
"""
import os


def read_environment():
    """
    Check if your environment variables are ready
    """
    print('Local test')
    remote_host=os.getenv('REMOTE_HOST')
    print('REMOTE_HOST: "{0}"'.format(remote_host))
    username = os.getenv('REMOTE_USERNAME')
    print('REMOTE_USERNAME: "{0}"'.format(username))
    host_keys_directory = os.getenv('HOST_KEYS_DIRECTORY')
    print('HOST_KEYS_DIRECTORY: "{0}"'.format(host_keys_directory))
    ssh_private_key_filename = os.getenv('SSH_PRIVATE_KEY_FILENAME')
    print('SSH_PRIVATE_KEY_FILENAME: "{0}"'.format(ssh_private_key_filename))
