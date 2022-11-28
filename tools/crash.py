"""This module provides a function to print a custom message error."""

import os
import platform
import sys
from time import ctime

from colorama import Fore  # type: ignore[import]


def CriticalError(message: str, error: Exception) -> None:
    """Print a custom message error.

    Args:
        - message - The message to be printed
        - error - The error object itself

    Returns:
        None
    """
    print(
        f"""\n
    {Fore.RED}:=== Critical error:
    {Fore.MAGENTA}MESSAGE: {message}.
    {Fore.MAGENTA}ERROR: {error}
    {Fore.RED}:=== Python info:
    {Fore.MAGENTA}PYTHON VERSION: {platform.python_version()}
    {Fore.MAGENTA}PYTHON BUILD: {'{}, DATE: {}'.format(*platform.python_build())}
    {Fore.MAGENTA}PYTHON COMPILER: {platform.python_compiler()}
    {Fore.MAGENTA}SCRIPT LOCATION: {os.path.dirname(os.path.realpath(sys.argv[0]))}
    {Fore.MAGENTA}CURRENT LOCATION: {os.getcwd()}
    {Fore.RED}:=== System info:
    {Fore.MAGENTA}SYSTEM: {platform.system()}
    {Fore.MAGENTA}RELEASE: {platform.release()}
    {Fore.MAGENTA}VERSION: {platform.version()}
    {Fore.MAGENTA}ARCHITECTURE: {'{} {}'.format(*platform.architecture())}
    {Fore.MAGENTA}PROCESSOR: {platform.processor()}
    {Fore.MAGENTA}MACHINE: {platform.machine()}
    {Fore.MAGENTA}NODE: {platform.node()}
    {Fore.MAGENTA}TIME: {ctime()}
    {Fore.RED}:=== Report:
    {Fore.MAGENTA}Report error here: https://github.com/7zx/overload/issues/new
    {Fore.RESET}
    """
    )
    sys.exit(1)
