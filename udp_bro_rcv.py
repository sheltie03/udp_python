# -*- coding: utf-8 -*-
import socket
import time


def main():
    host = ''
    port = 4000
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    while True:
        msg, addr = sock.recvfrom(8192)
        print(msg)
    return

if __name__ == '__main__':
    main()
