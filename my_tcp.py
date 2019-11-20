#!/usr/bin/env python3

import socket


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', 8080))
    sock.listen(1)

    while True:
        print("waiting for a connection...")
        connection, client_address = sock.accept()
        try:
            print("connection from {}".format(client_address))
            while True:
                data = connection.recv(1024)
                print("received {!r}".format(data))
                if data:
                    print("sending data back")
                    connection.sendall(data)
                else:
                    print("no data from {}".format(client_address))
                    break
        finally:
            connection.close()