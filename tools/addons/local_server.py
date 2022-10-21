"""This module provides a class to create local servers for general testing."""

import os
import socket
import sys

os.chdir(os.getcwd() + "/..")

from tools.crash import CriticalError  # type: ignore[import]


class Server:
    """Used to create local servers."""

    def __init__(self, host: str, port: int):
        """Initialize a local server.

        Keyword arguments:
        host -- the server's IP
        port -- the server's port
        """
        self.host = host
        self.port = port
        self.response = b"HTTP/1.1 200 OK\r\n\r\nIt's all working!!"
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def __enter__(self):
        """Pass IP and port configurations."""
        self.sock.bind((self.host, self.port))
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Close server."""
        self.sock.close()

    def start(self):
        """Start listening for clients."""
        try:
            self.sock.listen()
            while True:
                conn, _ = self.sock.accept()
                print(conn.recv(1024).decode())
                conn.sendall(self.response)
                conn.close()
        except KeyboardInterrupt:
            print("\nCrtl+C detected. Server closed.")
            sys.exit(1)
        except Exception as err:
            CriticalError("An error occured while the server was listening", err)


def main() -> None:
    """Context manager to start server."""
    HOST, PORT = "127.0.0.1", 8080
    with Server(HOST, PORT) as server:
        server.start()


if __name__ == "__main__":
    main()
