"""
Docker setup
"""
import os
import user
from fabric.api import sudo
# pylint: disable=W0511
# pylint: disable=C0325


def setup_docker_user(username):
    """
    Configure an account dedicated to Docker
    """
    print('Setup Docker user {0}'.format(username))
    sudo('usermod -aG docker {name}'.format(name=username))


def install_docker_compose():
    """
    Install Docker Compose
    """
    print('Install Docker-Compose')
    docker_compose_version = os.getenv('DOCKER_COMPOSE_VERSION')
    sudo('sh -c "curl -L https://github.com/docker/compose/releases/download/{0}/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose"'
         .format(docker_compose_version))
    sudo('chmod +x /usr/local/bin/docker-compose')
    sudo('sh -c "curl -L https://raw.githubusercontent.com/docker/compose/{0}/contrib/completion/bash/docker-compose > /etc/bash_completion.d/docker-compose"'
         .format(docker_compose_version))


def install():
    """
    Install Docker
    """
    print('Install Docker')
    sudo('curl -sSL https://get.docker.com/ | sh')


def setup_for_user(username):
    """
    Install Docker with Docker Compose and setup a 'deploy' user
    """
    print('Setup Docker for {0} user'.format(username))
    install()
    user.create_user(username)
    setup_docker_user(username)
    install_docker_compose()
