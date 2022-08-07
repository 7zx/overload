import os
import sys
import wget
from colorama import Fore
import requests

if os.name == "nt":

    # Executable URL
    ws_url = "https://2.na.dl.wireshark.org/win64/Wireshark-win64-3.4.15.exe"

    # Searching for Wireshark paths
    ws_dir_1, ws_dir_2 = os.environ["ProgramFiles"] + "\\Wireshark", os.environ["ProgramFiles(x86)"] + "\\Wireshark"

    # If it doesn't exist, ask user to download it
    if not (os.path.exists(ws_dir_1) or os.path.exists(ws_dir_2)):
        print(
            f'{Fore.MAGENTA}[!] {Fore.YELLOW}WireShark Network Protocol Analyzer not found! \nWould you like to download it to monitor the package traffic? (y/n)\n'
        )

        # Response
        r = input(f"{Fore.MAGENTA} >>> {Fore.BLUE}").lower()

        # Loop to make sure the response is valid
        while r not in ('y', 'yes', '1', 'n', 'no', '0'):
            print(f"{Fore.MAGENTA}[!] {Fore.YELLOW}Enter a valid value (y/n)\n")
            r = input(f"{Fore.MAGENTA} >>> {Fore.BLUE}").lower()

        # If response is yes, then download it
        if r in ("y", "yes", "1"):
            print(f"{Fore.YELLOW}[~] {Fore.CYAN}Downloading it...{Fore.BLUE}\n")

            # Changing CWD to Downloads
            os.chdir(os.environ["USERPROFILE"] + "\\Downloads")

            # Downloading it
            ws_installer = wget.download(ws_url)

            try:
                # Asking for installing it
                os.startfile(ws_installer)

            # If the user doesn't install it, then go back to the overload.py
            except OSError:
                print(f"\n\n{Fore.MAGENTA}WireShark was not installed!!{Fore.BLUE}\n")
    else:
        print(f"{Fore.MAGENTA}WireShark Network Protocol Analyzer detected!!{Fore.BLUE}\n") 