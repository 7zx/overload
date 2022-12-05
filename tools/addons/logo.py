"""This module provides a function that prints the logo's application."""

from colorama import Fore


def show_logo() -> None:
    """Print the application logo.

    Args:
        None

    Returns:
        None
    """
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

    print(Fore.RED + logo)
    print(f"{Fore.LIGHTRED_EX}├─── DOS TOOL LAYER 7")
    print("├─── AVAILABLE METHODS: HTTP | HTTP-PROXY | SLOWLORIS | SLOWLORIS-PROXY")
