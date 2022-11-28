"""This module provides functions to check inputs."""

from typing import Union

import requests
from colorama import Fore  # type: ignore[import]

from tools.ip_tools import set_target_http  # type: ignore[import]


def check_method_input() -> str:
    """Check if the method name is valid.

    Args:
        None

    Returns:
        - y - A valid method name
    """
    y = input(f"{Fore.RED}│   ├───METHOD (HTTP or Slowloris): {Fore.RESET}").lower()
    while y not in ["http", "slowloris"]:
        print(
            f"{Fore.RED}│   └───{Fore.MAGENTA}[!] {Fore.BLUE}Type a valid method (HTTP or Slowloris){Fore.RESET}"
        )
        y = input(f"{Fore.RED}│   ├───METHOD (HTTP or Slowloris): {Fore.RESET}")
    return y


def check_number_input(x: str) -> int:
    """Check if an input is a number greater than zero.

    Args:
        - x - The name of the input field

    Returns:
        - y - A valid value
    """
    while True:
        y = input(
            f"{Fore.RED}│   ├───{x.upper()}: {Fore.RESET}"
        )  # type: Union[str, int]
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
    """Check if the URL is valid.

    Args:
        None

    Returns:
        - y - A valid URL target
    """
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


def check_proxy_input() -> bool:
    """Check if proxy input can be converted to binary.

    Args:
        None

    Returns:
        - y - A valid boolean for proxy usage
    """
    y = input(
        f"{Fore.RED}│   ├───USE PROXY: {Fore.RESET}"
    ).lower()  # type: Union[str, int]
    while y not in ["0", "1", "yes", "y", "no", "n"]:
        print(
            f"{Fore.RED}│   └───{Fore.MAGENTA}[!] {Fore.BLUE}Type a valid entry (0 = No | 1 = Yes){Fore.RESET}"
        )
        y = input(f"{Fore.RED}│   ├───USE PROXY: {Fore.RESET}")
    if y in ["yes", "y"]:
        y = 1
    elif y in ["no", "n"]:
        y = 0
    return bool(int(y))
