"""This module provides functions to check inputs."""

from typing import Union

import requests
from colorama import Fore

from tools.addons.ip_tools import set_target_http


def check_method_input() -> str:
    """Check if the method name is valid.

    Args:
        None

    Returns:
        - method - A valid method name
    """
    while (method := input(f"{Fore.RED}│   ├───METHOD: {Fore.RESET}").lower()) not in [
        "http",
        "http-proxy",
        "slowloris",
        "slowloris-proxy",
    ]:
        print(
            f"{Fore.RED}│   └───{Fore.MAGENTA}[!] {Fore.BLUE}Type a valid method!{Fore.RESET}"
        )
    return method


def check_number_input(x: str) -> int:
    """Check if an input is an integer number greater than zero.

    Args:
        - x - The name of the input field

    Returns:
        - y - A valid value
    """
    while True:
        y: Union[str, int]
        y = input(f"{Fore.RED}│   ├───{x.upper()}: {Fore.RESET}")
        try:
            y = int(y)
            if y <= 0:
                raise ValueError
        except ValueError:
            print(
                f"{Fore.RED}│   └───{Fore.MAGENTA}[!] {Fore.BLUE}This value must be an integer number greater than zero!{Fore.RESET}"
            )
        else:
            return y


def check_target_input() -> str:
    """Check if the URL is valid.

    Args:
        None

    Returns:
        - target - A valid URL target
    """
    while True:
        target = input(f"{Fore.RED}│   └───URL: {Fore.RESET}")
        try:
            requests.get("https://google.com", timeout=4)
            try:
                requests.get(set_target_http(target), timeout=4)
            except Exception as exc:
                raise requests.exceptions.InvalidURL from exc
        except requests.exceptions.ConnectionError:
            print(
                f"{Fore.RED}│   └───{Fore.MAGENTA}[!] {Fore.BLUE}The device is not connected to the internet!{Fore.RESET}"
            )
        except requests.exceptions.InvalidURL:
            print(
                f"{Fore.RED}│   └───{Fore.MAGENTA}[!] {Fore.BLUE}Invalid URL!{Fore.RESET}"
            )
        else:
            return target
