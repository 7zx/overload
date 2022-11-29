"""This module provides a function to create sockets instances."""

import json
import random
import socket
import sys
import warnings
from typing import Dict, List, Tuple, Union

import requests
import socks
from colorama import Fore
from requests.exceptions import Timeout

from tools.addons.ip_tools import get_target_domain

warnings.filterwarnings("ignore", message="Unverified HTTPS request")

with open("tools/L7/user_agents.json", "r", encoding="utf-8") as agents:
    user_agents = json.load(agents)["agents"]


def get_socks_proxies() -> List[Dict[str, str]]:
    """Return a dictionary of avaliable proxies using socks protocol.

    Args:
        None

    Returns:
        - proxies - A dictionary containing socks proxies in the form of address:port paired values
    """
    try:
        with requests.get(
            "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all",
            verify=False,
            timeout=10,
        ) as proxy_list:
            proxies = []  # type: List[Dict[str, str]]
            for proxy in proxy_list.text.split("\r\n"):
                if proxy != "":
                    addr, port = proxy.split(":")
                    proxies.append({"addr": addr, "port": port})
    except Timeout:
        print(
            f"\n{Fore.RED}[!] {Fore.CYAN}It was not possible to connect to the proxies.{Fore.RESET}"
        )
        sys.exit(1)

    return proxies


proxies = get_socks_proxies()


def create_socket(
    target: str, use_proxy: bool
) -> Tuple[socket.socket, Union[Dict[str, str], None]]:
    """Create a socket.

    Args:
        - target - The target's URL
        - use_proxy - Whether or not to use proxy

    Returns:
        - sock - The socket associated with the communication
    """
    global proxies
    while True:
        try:
            sock = socks.socksocket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(4)

            if use_proxy:
                while True:
                    proxy = random.choice(proxies)
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
            try:
                proxies.remove(proxy)
            except ValueError:
                proxies = get_socks_proxies()
            continue
    if use_proxy:
        return sock, proxy
    return sock, None
