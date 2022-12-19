"""This module provides functions to analyze network matters."""

import ipaddress
import socket
import sys
from time import sleep
from urllib.parse import urlparse

import requests
from colorama import Fore as F
from requests.exceptions import Timeout


def __is_cloud_flare(target: str) -> None:
    """Check if the target is protected by CloudFlare.

    Args:
        - target - The URL to be checked in the CloudFlare protection networks

    Returns:
        None
    """
    domain, _ = get_target_domain(target)
    try:
        origin = socket.gethostbyname(domain)
        iprange = requests.get("https://www.cloudflare.com/ips-v4", timeout=10).text
        ipv4 = [row.rstrip() for row in iprange.splitlines()]
        for ip in ipv4:
            if ipaddress.ip_address(origin) in ipaddress.ip_network(ip):
                print(
                    f"\n{F.RED}[!] {F.CYAN}This website is protected by CloudFlare, this attack may not produce the desired results.{F.RESET}"
                )
                sleep(1)
    except (Timeout, socket.gaierror):
        print(
            f"{F.RED}\n[!] {F.CYAN}It was not possible to check for CloudFlare protection!.{F.RESET}"
        )
        sleep(1)


def get_target_address(target: str) -> str:
    """Get target's URL formatted with HTTP protocol and CloudFlare checked.

    Args:
        - target - The target's URL

    Returns:
        - url - The formatted and checked URL
    """
    url = set_target_http(target)
    __is_cloud_flare(url)
    return url


def set_target_http(target: str) -> str:
    """Get target's URL formatted with HTTP protocol.

    Args:
        - target - The target's URL

    Returns:
        - target - The target's URL with HTTP protocol
    """
    if not target.startswith("http"):
        target = f"http://{target}"
    return target


def get_target_domain(target: str) -> str:
    """Get target's domain.

    Args:
        - target - The target's URL

    Returns:
        - domain - The target's domain
    """
    parsed_uri = urlparse(target)
    try:
        domain, port = parsed_uri.netloc.split(":")
    except:
        domain, port = parsed_uri.netloc, 80
    return domain, int(port)


def get_host_ip() -> str:
    """Get host's ip.

    Args:
        None

    Returns:
        - IP - The host's IP
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        s.connect(("8.8.8.8", 80))
        IP = s.getsockname()[0]
    except:
        print(
            f"{F.RED}│   └───{F.MAGENTA}[!] {F.BLUE}Local IP cannot be found!{F.RESET}"
        )
        sys.exit(1)
    s.close()
    return IP
