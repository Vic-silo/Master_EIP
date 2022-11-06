from paramiko import SSHClient, AutoAddPolicy
from paramiko.ssh_exception import NoValidConnectionsError, AuthenticationException
from paramiko.util import log_to_file
import os

# Join paths
current_directory = os.getcwd()
HOSTS_DIR = os.path.join(current_directory, 'ssh_hosts')


def ssh_client():
    client = SSHClient()
    # log_to_file('client.log')
    client.set_missing_host_key_policy(AutoAddPolicy())

    return client


def ssh_connection(ssh_client_: SSHClient):
    for line in open(HOSTS_DIR, 'r').readlines():
        ip, user, password = line.strip().split(' ')
        print(f'IP\t"{ip}"\nUSER\t"{user}"\nPASSWORD\t"{password}"')
        try:
            ssh_client_.connect(ip, username=user, password=password)
            print('\tConexion establecida.')
            # Perform the same command for each SSH Server
            execute_command(ssh_client_, command='whoami & ls -a')

        except AuthenticationException:
            print('\tCredenciales erroneas.')

        except NoValidConnectionsError as e:
            print('\t', e)

        finally:
            # log_to_file(f'client_{ip}.log')
            print('\n', 50*'=')


def execute_command(ssh_client_: SSHClient, command: str):
    # Split possible multicommand line
    command_list = command.strip().split(' & ')
    for i in command_list:
        print(f'\tEjecutando comando:\t{i}')
        stdin, stdout, stderr = ssh_client_.exec_command(i)
        print('\tRespuesta:')
        for line in stdout.readlines():
            print('\t\t', line)

    ssh_client_.close()


if __name__ == '__main__':
    client = ssh_client()
    ssh_connection(client)
