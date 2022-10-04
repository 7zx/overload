import requests
from colorama import Fore

from tools.ipTools import __GetURLInfo


def checkNumbersInput(x):
    y, i = input(f"{Fore.RED}│   ├───{x.upper()}: {Fore.RESET}"), True
    while i:
        try:
            y = int(y)
            if y <= 0:
                raise ValueError
        except ValueError:
            print(
                f"{Fore.GREEN}│   ├─── This value must be a number greater than zero!{Fore.RESET}"
            )
            y = y = input(f"{Fore.RED}│   ├───{x.upper()}: {Fore.RESET}")
        else:
            i = False
            return y


def checkTargetInput():
    y, i = __GetURLInfo(input(f"{Fore.RED}│   └───URL: {Fore.RESET}")), True
    print(y)
    while i:
        try:
            r = requests.get(y, timeout=4)
            if r.status_code != 200:
                raise Exception
        except:
            print(f"{Fore.GREEN}It's not possible to reach this target!{Fore.RESET}")
            y = __GetURLInfo(input(f"{Fore.RED}│   └───URL: {Fore.RESET}"))
            print(y)
        else:
            i = False
            return y
