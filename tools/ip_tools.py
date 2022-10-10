"""This module provides functions to analyze network matters."""

import ipaddress
import socket
from time import sleep
from urllib.parse import urlparse

import requests
from colorama import Fore  # type: ignore[import]


def __is_cloud_flare(link: str) -> None:
    """Check if the target is protected by CloudFlare.

    Keyword arguments:
    link -- the URL to be checked in the CloudFlare protection networks
    """
    domain = get_target_domain(link)
    try:
        origin = socket.gethostbyname(domain)
        iprange = requests.get("https://www.cloudflare.com/ips-v4").text
        ipv4 = [row.rstrip() for row in iprange.splitlines()]
        for i in range(len(ipv4)):
            if ipaddress.ip_address(origin) in ipaddress.ip_network(ipv4[i]):
                print(
                    f"{Fore.RED}[!] {Fore.CYAN}This website is protected by CloudFlare, this attack may not produce the desired results.{Fore.RESET}"
                )
                sleep(1)
    except socket.gaierror:
        print(
            f"{Fore.RED}[!] {Fore.CYAN}It was not possible to check for CloudFlare protection!.{Fore.RESET}"
        )
        sleep(1)


def get_target_address(target: str) -> str:
    """Get target's URL formatted with HTTP protocol and CloudFlare checked.

    Keyword arguments:
    target -- the target's URL
    """
    url = set_target_http(target)
    __is_cloud_flare(url)
    return url


def set_target_http(target: str) -> str:
    """Get target's URL formatted with HTTP protocol.

    Keyword arguments:
    target -- the target's URL
    """
    if not target.startswith("http"):
        target = f"http://{target}"
    return target


def get_target_domain(target: str) -> str:
    """Get target's domain.

    Keyword arguments:
    target -- the target's URL
    """
    parsed_uri = urlparse(target)
    return parsed_uri.netloc
