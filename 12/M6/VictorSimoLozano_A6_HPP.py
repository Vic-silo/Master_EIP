import binascii
import hashlib
import sys


def get_hashes():
    # Multiple iterations over user accounts and tried passwords for them
    for account in open(sys.argv[1]).readlines():
        print(f'\tUSER:\t{account.split(":")[0]}')
        for pwd in open(sys.argv[2], 'r').readlines():
            pwd = pwd.replace('\n', '')
            hash_account = account.split(':')[3]
            ntlm_hash = binascii.hexlify(hashlib.new('md4', pwd.encode('utf-16le')).digest())

            # Compare between the hash generated (ntlm_hash) and the hash from file (hash_account)
            if ntlm_hash.decode('utf-8') == hash_account:
                print(f'\t\t[+] Hash encontrado! Password: {pwd}')
            else:
                print(f'\t\t[-] Contraseña "{pwd}" erronea.')


if __name__ == '__main__':
    # Execution parameters handler
    PARAMETERS_NUM = 3
    if sys.argv[1] == '-h':
        print('\tPARAMETROS:\n\t\t[-] <hases>\n\t\t[-] <passwords>')
        exit()

    if len(sys.argv) != PARAMETERS_NUM:
        print('\tError: numero de parámetros incorrectos.\n')
        print('\tPARAMETROS:\n\t\t[-] <hases>\n\t\t[-] <passwords>')
        exit()

    # Run code to match hashes with passwords file
    get_hashes()
