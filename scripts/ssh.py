"""
SSH activities
"""
from fabric.api import sudo
# pylint: disable=C0325

def restart():
    """
    Restart SSH service
    """
    print('Restart ssh')
    sudo('service ssh restart')
