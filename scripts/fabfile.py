"""
Provision a server to be ready to work
"""
# import docker_setup
import environment
import key
# import server
from fabric.api import task


@task
def local_test():
    """
    Check if your environment variables are ready
    """
    environment.read_environment()


@task
def remote_test():
    """
    A small test to check if you can access your remote server using a key,
    it will try to get details about the operating system
    """
    key.key_remote_test()


# @task
# def prepare_new_server():
#     """
#     Get a server and make it ready to be used in production
#     """
#     server.prepare_new()


# @task
# def setup_new_no_root():
#     """
#     Get a server with key access only
#     and make it ready to be used in production
#     """
#     server.setup_new_no_root()


# @task
# def setup_docker_with_deploy_user():
#     """
#     Install docker and setup a 'deploy' user
#     """
#     docker_setup.setup_for_user()
