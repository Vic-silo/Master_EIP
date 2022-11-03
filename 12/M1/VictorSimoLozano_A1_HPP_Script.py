import shodan
import logging
import time
import nmap


def start_logging(filename: str):
    """
    Configuration logging parameters
    :param filename:
    :return:
    """
    logging.basicConfig(filename=f'''{filename}.log''', encoding='utf-8', level=logging.DEBUG, filemode='a',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def key_information(shodan_api, key):
    """
    Check SHODAN API connection
    :param shodan_api: API KEY from Shodan
    :return:
    """
    try:
        print('\nConectando a servidor SHODAN...')
        shodan_api.info()
        logging.info(msg=f'''SUCCESS: Shodan API connection. Key {key}''')
        print(f'''Conexion completada.\n{50*'.'}''')

        return True

    except shodan.APIError as e:
        logging.error(msg=f'''Shodan API connection: {e}''')
        print(f'''API Key error.\n{50*'.'}''')

        return False


def shodan_query(query: str, n_searches: 10):
    print(f'''LANZANDO BUSQUEDA: "{query}"\n''')
    ip_list = []
    try:
        # Shodan search
        results = shodan_api.search(query)
        print('Resultados encontrados: {}'.format(results['total']))
        print(50 * ".")

        # Get de n_searches values
        if results['total'] > 0:
            print(f'''Geolocalizacion primeros {n_searches} resultados:\n''')
            i = 0
            with open(f'''Search_{query}_{time.asctime()}''', 'w') as f:
                for result in list(results['matches'])[0:n_searches]:
                    i += 1
                    print(f'''\t{i}: {result['location']}''')
                    ip_list.append(result['ip_str'])
                    # print('Resultado {}'.format(i))
                    # N_IPs.append(result['ip_str'])
                    # print('IP: %s' % result['ip_str'])
                    # print(result['data'])
                    f.write(f'''Resultado {i}\n''')
                    f.write(f'''{str(result)}\n''')

        # Search report
        logging.info(msg=f'''Busqueda: {query}''')
        logging.info(msg=f'''Resultados busqueda: {results['total']}''')
        logging.info(msg=f'''IPs vulnerables: {ip_list}''')

    except shodan.APIError as e:
        logging.error(msg=f'''Error en la busqueda: {e}''')
        print('Search Error')

    return ip_list


def network_mapper(scanner, ips: list, ports: str):
    """
    Perform  Network mapper to a list of host and its ports
    :param scanner:
    :param ips:
    :param ports:
    :return:
    """
    print('\nNetwork Mapper para los diferentes HOSTS.\n')

    # Perform search in each IP found
    i = 0
    for host in ips:
        i += 1
        # Host scan
        try:
            scanner.scan(hosts=host, ports=ports, arguments='-A')

            # host information
            print(f'''\t{i}: Host: {host} ({scanner[host].hostname()})\tState: {scanner[host].state()}''')
            # port information
            for protocol in scanner[host].all_protocols():
                print(f'''\t\tProtocolo: {protocol}''')
                list_ports = scanner[host][protocol].keys()
                for port in list_ports:
                    print(f'''\t\t\tPuerto: {port}\tEstado: {scanner[host][protocol][port]['state']}
                    Version: {scanner[host][protocol][port]['version']}\tCPE: {scanner[host][protocol][port]['cpe']}''')
        except Exception as e:
            logging.error(msg=f'''Error en Network Mapper para {host}: {e}''')
            print(f'''{host} Scan Error''')


if __name__ == '__main__':
    start_logging('log')

    # Create Shodan instance and check
    shodan_key = input('Introduce tu SHODAN API KEY:\n')
    shodan_api = shodan.Shodan(shodan_key)
    key_check = key_information(shodan_api, shodan_key)

    # Perform Shodan search
    if key_check:
        # query = input('Busqueda Shodan: ')
        query = 'Apache Server 2.4.49'
        vulnerable_ip = shodan_query(query, 5)

        # Perform Nmap
        if len(vulnerable_ip) > 0:
            nmScan = nmap.PortScanner()
            ports = '80, 443'
            network_mapper(nmScan, vulnerable_ip, ports)
