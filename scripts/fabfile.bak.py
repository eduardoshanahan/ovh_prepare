# import os
# import logging
# from fabric.api import *
# from fabric.contrib.files import append
# from fabric.contrib.files import contains
# from fabric.contrib.files import uncomment
# from fabric.contrib.files import sed
# from fabric.context_managers import shell_env
#
# LOGGER = logging.getLogger('root')
# env.colorize_errors = True
# env.hosts = [os.getenv('REMOTE_HOST')]


# @task
# def local_test():
#     """
#     Check if your environment variables are ready
#     """
#     LOGGER.info('Local test')
#     username = os.getenv('REMOTE_USERNAME')
#     LOGGER.debug('Fabric has REMOTE_USERNAME with the value %s', username)


# @task
# def root_remote_test():
#     """
#     A small test to check if you can access your remote server using a password,
#     it will try to get details about the operating system
#     """
#     LOGGER.info('Root remote test')
#     LOGGER.debug('pass %s', os.getenv('REMOTE_ROOT_PASSWORD'))
#     env.user = os.getenv('REMOTE_ROOT_USERNAME')
#     env.password = os.getenv('REMOTE_ROOT_PASSWORD')
#     run('uname -a')


# @task
# def use_keys():
#     """
#     Setup key access to the remote server
#     """
#     LOGGER.info('Use keys')
#     env.user = os.getenv('REMOTE_USERNAME')
#     private_key_filename = os.getenv('PRIVATE_KEY_FILENAME')
#     docker_ssh_keys_path = os.getenv('DOCKER_SSH_KEYS_PATH')
#     LOGGER.debug('User is %s, private key filename %s, docker key path is %s',
#                  env.user, private_key_filename, docker_ssh_keys_path)
#     env.key_filename = os.path.join('/', docker_ssh_keys_path, private_key_filename)
#     LOGGER.debug('Key filename is %s', env.key_filename)
#
#
# @task
# def key_remote_test():
#     """
#     A small test to check if you can access your remote server using a key,
#     it will try to get details about the operating system
#     """
#     use_keys()
#     LOGGER.info('Key remote test')
#     run('uname -a')

# @task
# def prepare_new_server():
#     """
#     Get a server and make it ready to be used in production
#     """
#     LOGGER.info('Prepare new server')
#     env.user = os.getenv('REMOTE_ROOT_USERNAME')
#     env.password = os.getenv('REMOTE_ROOT_PASSWORD')
#     username = os.getenv('REMOTE_USERNAME')
#     public_key_filename = os.getenv('PUBLIC_KEY_FILENAME')
#     docker_ssh_keys_path = os.getenv('DOCKER_SSH_KEYS_PATH')
#     public_key_path = os.path.join('/', docker_ssh_keys_path, public_key_filename)
#     setup_key_access(username, public_key_path)
#     setup_docker_with_deploy_user()
#
# @task
# def setup_new_server_no_root():
#     """
#     Get a server with key access only and make it ready to be used in production
#     """
#     LOGGER.info('Prepare new server without using password')
#     env.user = os.getenv('REMOTE_ROOT_USERNAME')
#     env.password = os.getenv('REMOTE_ROOT_PASSWORD')
#     username = os.getenv('REMOTE_USERNAME')
#     public_key_filename = os.getenv('PUBLIC_KEY_FILENAME')
#     docker_ssh_keys_path = os.getenv('DOCKER_SSH_KEYS_PATH')
#     public_key_path=os.path.join('/',docker_ssh_keys_path,public_key_filename)
#     setup_key_access(username, public_key_path)
#     setup_docker_with_deploy_user()


# def setup_key_access(username, key_path):
#     """
#     Prepare access using keys instead of password
#     """
#     LOGGER.info('Setup key access')
#     create_user(username)
#     prepare_keys_directory(username)
#     enable_write_authorized_keys(username)
#     upload_key_for_user(username, key_path)
#     disable_write_authorized_keys(username)
#     tell_user_own_key(username)
#     tell_key_does_not_need_password(username)
#     authorize_keys()
#     disable_password_authentication()
#     restart_ssh()


# def disable_write_authorized_keys(username):
#     """
#     Disable to write the SSH keys
#     """
#     LOGGER.info('Disable write authorized keys')
#     sudo('chmod u-w /home/{name}/.ssh/authorized_keys'.format(name=username))
#
#
# def enable_write_authorized_keys(username):
#     """
#     Enable to write the SSH keys
#     """
#     LOGGER.info('Enable write authorized keys')
#     sudo('touch /home/{name}/.ssh/authorized_keys'.format(name=username))
#     sudo('chmod u+w /home/{name}/.ssh/authorized_keys'.format(name=username))


# def enable_password_authentication_settings():
#     """
#     Enable password authentication
#     """
#     LOGGER.info('Enable password authentications settings')
#     if contains('/etc/ssh/sshd_config', 'PasswordAuthentication yes'):
#         uncomment('/etc/ssh/sshd_config', 'PasswordAuthentication yes', use_sudo=True)
#
#
# def disable_password_authentication():
#     """
#     Disable password authentication
#     """
#     LOGGER.info('Disable password authentication')
#     enable_password_authentication_settings()
#     sed('/etc/ssh/sshd_config', 'PasswordAuthentication yes', 'PasswordAuthentication no')


# def tell_key_does_not_need_password(username):
#     """
#     Indicate that the keys does not need a password
#     """
#     LOGGER.info('Tell key does not need password')
#     condition = '{name} ALL=(ALL) NOPASSWD: ALL'.format(name=username)
#     if not contains('/etc/sudoers', condition):
#         append('/etc/sudoers', condition, use_sudo=True)
#
#
# def authorize_keys():
#     """
#     Authorize the use of SSH keys authentication
#     """
#     LOGGER.info('Authorize keys')
#     uncomment('/etc/ssh/sshd_config', '#AuthorizedKeysFile', use_sudo=True)
#
#
# def prepare_keys_directory(username):
#     """
#     Create the SSH keys directory
#     """
#     LOGGER.info('Prepare keys directory')
#     sudo('mkdir -p /home/{name}/.ssh'.format(name=username))
#
#
# def tell_user_own_key(username):
#     """
#     Make the user owner of the SSH key
#     """
#     LOGGER.info('Tell that the user owns the key')
#     sudo('chown {name} /home/{name}/.ssh/authorized_keys'.format(name=username))
#
#
# def upload_key_for_user(username, key_path):
#     """
#     Upload the SSH keys for a username
#     """
#     LOGGER.info('Upload key %s for user %s', key_path, username)
#     # TODO: Instead of overwriting the keys, I should append if not already present
#     put(key_path, '/home/{name}/.ssh/authorized_keys'.format(name=username))


# def create_user(username):
#     """
#     Create a new user in the server
#     """
#     LOGGER.info('Create user')
#     sudo('id -u {name} &>/dev/null || useradd --user-group \
#          --create-home --shell /bin/bash {name} || true'.format(name=username))


# def restart_ssh():
#     """
#     Restart SSH service
#     """
#     LOGGER.info('Restart ssh')
#     sudo('service ssh restart')


# @task
# def setup_docker_with_deploy_user():
#     """
#     Install docker and setup a 'deploy' user
#     """
#     LOGGER.info('Setup Docker with "deploy" user')
#     install_docker()
#     docker_user = 'deploy'
#     create_user(docker_user)
#     setup_docker_user(docker_user)


# def install_docker():
#     """
#     Install Docker
#     """
#     LOGGER.info('Install Docker')
#     sudo('curl -sSL https://get.docker.com/ | sh')

# @task
# def setup_docker_compose():
#     """
#     Install Docker Compose
#     """
#     LOGGER.info('Install Docker-Compose')
#     docker_compose_version = '1.8.0'
#     sudo('sh -c "curl -L https://github.com/docker/compose/releases/download/{0}/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose"'.format(docker_compose_version))
#     sudo('chmod +x /usr/local/bin/docker-compose')
#     sudo('sh -c "curl -L https://raw.githubusercontent.com/docker/compose/{0}/contrib/completion/bash/docker-compose > /etc/bash_completion.d/docker-compose"'.format(docker_compose_version))


# def setup_docker_user(username):
#     LOGGER.info('Setup Docker user')
#     sudo('usermod -aG docker {name}'.format(name=username))

# @task
# def transfer_files():
#     """
#     Pass the files for the proxy to the remote server
#     """
#     put('docker-compose.yml', '')
#     put('./volumes', '')
#
# @task
# def transfer_content():
#     """
#     Pass the content of the website to the remote server
#     """
#     put('./volumes/examples/simple-site/src', './volumes/examples/simple-site/src')
