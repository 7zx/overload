import ipaddress
import socket
import sys
from time import sleep
from urllib.parse import urlparse

import requests
from colorama import Fore


# Checks if the target is protected by CloudFlare
def __is_cloud_flare(link: str) -> None:
    parsed_uri = urlparse(link)
    domain = f"{parsed_uri.netloc}"
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


# Gets target's IP and port
def __get_address_info(target):
    try:
        ip = target.split(":")[0]
        port = int(target.split(":")[1])
    except IndexError:
        print(
            f"{Fore.RED}[!] {Fore.MAGENTA}You should insert an IP and port!{Fore.RESET}"
        )
        sys.exit(1)
    else:
        return ip, port


# Gets target's Uniform Resource Locator (URL)
def get_target_address(target: str) -> str:
    url = __get_url_info(target)
    __is_cloud_flare(url)
    return url


def __get_url_info(target: str) -> str:
    if not target.startswith("http"):
        target = f"http://{target}"
    return target
