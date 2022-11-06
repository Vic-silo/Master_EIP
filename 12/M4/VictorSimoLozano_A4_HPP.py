from scapy.all import get_if_addr, get_if_hwaddr, srp, ETHER_BROADCAST
from scapy.layers.l2 import ARP, Ether

NETWORK_ADAPTER = "eth0"

mac_local = get_if_hwaddr(NETWORK_ADAPTER)
ip_local = get_if_addr(NETWORK_ADAPTER)

ip_split = ip_local.split('.')
ip_split = f'{ip_split[0]}.{ip_split[1]}.{ip_split[2]}'
print(f'Escaneo de la red en el siguiente rango {ip_split}.180/255')

arp_finds = 0

for net_prefix in range(180, 256):
    ip = f'{ip_split}.{net_prefix}'
    arp_request = Ether(dst=ETHER_BROADCAST)/ARP(hwsrc=mac_local, hwdst=ETHER_BROADCAST, pdst=ip, psrc=ip_local)
    arp_reply = srp(arp_request, iface=NETWORK_ADAPTER, timeout=1, verbose=False)

    if arp_reply and arp_reply[0]:
        target = arp_reply[0][0][1].hwsrc
        print(f'\tActividad en {ip} // MAC: {target}')
        arp_finds += 1
    else:
        print(f'\tSin actividad en {ip}\r', end='')

print('\t', end=f'{50*" "}\n')
print(f'Total de equipos encontrados: {arp_finds}')
