"""This module provides functions to analyze network matters."""

import ipaddress
import json
import random
import socket
from time import sleep
from typing import Union
from urllib.parse import urlparse

import requests
from colorama import Fore  # type: ignore[import]

with open("tools/L7/user_agents.json", "r") as agents:
    user_agents = json.load(agents)["agents"]


def __is_cloud_flare(link: str) -> None:
    """Check if the target is protected by CloudFlare.

    Args:
        - link - The URL to be checked in the CloudFlare protection networks

    Returns:
        None
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
    domain = parsed_uri.netloc
    return domain


def create_socket(target: str) -> socket.SocketType:
    """Create a socket.

    Args:
        - target - The target's URL

    Returns:
        - sock - The socket associated with the communication
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(4)
        try:
            port: Union[str, int]
            protocol, domain, port = target.split(":")
        except ValueError:
            (protocol, domain), port = target.split(":"), 80

        ip = socket.gethostbyname(domain[2:])
        sock.connect((ip, int(port)))

        sock.send(f"GET /?{random.randint(0, 2000)} HTTP/1.1\r\n".encode("utf-8"))
        sock.send(f"User-Agent: {random.choice(user_agents)}".encode("utf-8"))
        sock.send("Accept-language: en-US,en,q=0.5".encode("utf-8"))
    except socket.timeout:
        print(f"{Fore.RED}[-] {Fore.MAGENTA}Time's up...{Fore.RESET}")
    except socket.error:
        print(
            f"{Fore.RED}[-] {Fore.MAGENTA}There was an error creating socket{Fore.RESET}"
        )
    return sock
