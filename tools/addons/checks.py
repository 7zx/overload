import requests
from colorama import Fore

from tools.ip_tools import set_target_http


def check_number_input(x: str) -> int:
    while True:
        y = input(f"{Fore.RED}│   ├───{x.upper()}: {Fore.RESET}")
        try:
            y = int(y)
            if y <= 0:
                raise ValueError
        except ValueError:
            print(
                f"{Fore.RED}│   └───{Fore.MAGENTA}[!] {Fore.BLUE}This value must be a number greater than zero!{Fore.RESET}"
            )
        else:
            return y


def check_target_input() -> str:
    while True:
        y = input(f"{Fore.RED}│   └───URL: {Fore.RESET}")
        try:
            requests.get("https://google.com", timeout=4)
            try:
                requests.get(set_target_http(y), timeout=4)
            except:
                raise requests.exceptions.InvalidURL
        except requests.exceptions.ConnectionError:
            print(
                f"{Fore.RED}│   └───{Fore.MAGENTA}[!] {Fore.BLUE}The device is not connected to the internet!{Fore.RESET}"
            )
        except requests.exceptions.InvalidURL:
            print(
                f"{Fore.RED}│   └───{Fore.MAGENTA}[!] {Fore.BLUE}Invalid URL!{Fore.RESET}"
            )
        else:
            return y
