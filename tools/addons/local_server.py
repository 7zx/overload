import os
import socket
import sys

os.chdir(os.getcwd() + "/..")

from tools.crash import CriticalError  # type: ignore[import]


class Server:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

        # The server will respond with a 200 HTTP status code and a message
        self.response = b"HTTP/1.1 200 OK\n\nIt's all working!!"

        # Establishing IPv4 and TCP protocols for the server
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Allowing the server to use the same address when needed
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def __enter__(self):

        # Passing IP and port configurations
        self.sock.bind((self.host, self.port))
        return self

    def __exit__(self, exc_type, exc_value, traceback):

        # Closes server
        self.sock.close()

    def start(self):

        try:
            # Starts listening
            self.sock.listen()
            while True:
                # Accepts client connection creating another socket entity for the communication
                conn, _ = self.sock.accept()

                # Decoding client's payload
                print(conn.recv(1024).decode())

                # Sends response and closes socket connection
                conn.sendall(self.response)
                conn.close()
        except KeyboardInterrupt:
            print("\nCrtl+C detected. Server closed.")
            sys.exit(1)
        except Exception as err:
            CriticalError("An error occured while the server was listening", err)


def main():

    # Default HTTP loopback interface
    HOST, PORT = "127.0.0.1", 8080
    with Server(HOST, PORT) as server:
        server.start()


if __name__ == "__main__":
    main()
