"""
Password settings
"""
from fabric.contrib.files import contains
from fabric.contrib.files import sed
from fabric.contrib.files import uncomment
# pylint: disable=C0325


def enable_password_authentication():
    """
    Enable password authentication
    """
    print('Enable password authentications settings')
    if contains('/etc/ssh/sshd_config', 'PasswordAuthentication yes'):
        uncomment('/etc/ssh/sshd_config', 'PasswordAuthentication yes',
                  use_sudo=True)


def disable_password_authentication():
    """
    Disable password authentication
    """
    print('Disable password authentication')
    enable_password_authentication()
    sed('/etc/ssh/sshd_config', 'PasswordAuthentication yes',
        'PasswordAuthentication no')
    print('Password authentication disabled')
