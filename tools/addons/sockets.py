"""This module provides a function to create sockets instances."""

import json
import random
import socket
import warnings
from typing import Any, Dict, Tuple, Union

import requests
import socks  # type: ignore[import]
from colorama import Fore  # type: ignore[import]

from tools.ip_tools import get_target_domain  # type: ignore[import]

warnings.filterwarnings("ignore", message="Unverified HTTPS request")

with open("tools/L7/user_agents.json", "r") as agents:
    user_agents = json.load(agents)["agents"]

with requests.get(
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all",
    verify=False,
) as proxies:
    proxies_ = list()
    for proxy in proxies.text.split("\r\n"):
        if proxy != "":
            addr, port = proxy.split(":")
            proxies_.append({"addr": addr, "port": port})
    proxies_ = proxies_[:50]


def create_socket(
    target: str, use_proxy: bool
) -> Tuple[Any, Union[Dict[str, str], None]]:
    """Create a socket.

    Args:
        - target - The target's URL
        - use_proxy - Whether or not to use proxy

    Returns:
        - sock - The socket associated with the communication
    """
    while True:
        try:
            sock = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(4)

            if use_proxy:
                while True:
                    proxy = random.choice(proxies_)
                    proxy_port: Union[int, str]
                    proxy_addr, proxy_port = proxy["addr"], proxy["port"]
                    try:
                        proxy_port = int(proxy_port)
                    except TypeError:
                        continue
                    else:
                        sock.set_proxy(socks.PROXY_TYPE_SOCKS5, proxy_addr, proxy_port)
                        break

            try:
                domain, port = get_target_domain(target).split(":")
            except ValueError:
                domain, port = get_target_domain(target), 80

            ip = socket.gethostbyname(domain)
            sock.connect((ip, int(port)))

            sock.send(f"GET /?{random.randint(0, 2000)} HTTP/1.1\r\n".encode("utf-8"))
            sock.send(f"User-Agent: {random.choice(user_agents)}".encode("utf-8"))
            sock.send("Accept-language: en-US,en,q=0.5".encode("utf-8"))
            break
        except (socket.timeout, socket.error):
            proxies_.remove(proxy)
            continue
    if use_proxy:
        return sock, proxy
    else:
        return sock, None
