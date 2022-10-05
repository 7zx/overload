import requests
from colorama import Fore

from tools.ip_tools import __get_url_info


def check_number_input(x: str) -> int:
    y, i = input(f"{Fore.RED}│   ├───{x.upper()}: {Fore.RESET}"), True
    while i:
        try:
            y = int(y)
            if y <= 0:
                raise ValueError
        except ValueError:
            print(
                f"{Fore.RED}│   └───{Fore.MAGENTA}[!] {Fore.BLUE}This value must be a number greater than zero!{Fore.RESET}"
            )
            y = input(f"{Fore.RED}│   ├───{x.upper()}: {Fore.RESET}")
        else:
            i = False
            return y


def check_target_input() -> str:
    y, i = __get_url_info(input(f"{Fore.RED}│   └───URL: {Fore.RESET}")), True
    while i:
        try:
            requests.get("https://google.com", timeout=4)
            try:
                requests.get(y, timeout=4)
            except:
                raise requests.exceptions.InvalidURL
        except requests.exceptions.ConnectionError:
            print(
                f"{Fore.RED}│   └───{Fore.MAGENTA}[!] {Fore.BLUE}The device is not connected to the internet!{Fore.RESET}"
            )
            y = __get_url_info(input(f"{Fore.RED}│   └───URL: {Fore.RESET}"))
        except requests.exceptions.InvalidURL:
            print(
                f"{Fore.RED}│   └───{Fore.MAGENTA}[!] {Fore.BLUE}Invalid URL!{Fore.RESET}"
            )
            y = __get_url_info(input(f"{Fore.RED}│   └───URL: {Fore.RESET}"))
        else:
            i = False
            return y
