#!/usr/bin/env python3

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = sys.argv[1]
server_port = int(sys.argv[2])

print("connecting to {} port {}".format(server_addr, server_port))
sock.connect((server_addr, server_port))

try:
    while True:
        message = bytes(input("Print integer number: "), "utf-8")
        sock.sendall(message)
        message = message.decode("utf-8")
        print("sending {}".format(message))

        data = sock.recv(1024)
        data = data.decode("utf-8")
        print("received {}".format(data))
finally:
    sock.close()