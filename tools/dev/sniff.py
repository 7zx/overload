"""Sniff the packets that are passing through the host."""

from sys import argv

from scapy.all import sniff


def start_sniff(filter: str = "tcp", count: int = 50) -> None:
    capture = sniff(filter=filter, count=count)
    capture.summary()


if "__main__" == __name__:
    try:
        start_sniff(argv[1], int(argv[2]))
    except IndexError:
        start_sniff()
