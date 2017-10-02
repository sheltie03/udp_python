# -*- coding: utf-8 -*-
import socket


def main():
    host = '127.0.0.1'
    port = 4000
    bufsize = 4096
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#    sock.bind((host, port))
    sock.bind(('', port))  # All Address of This Host
    while True:
        print (sock.recv(bufsize))
    return

if __name__ == '__main__':
    main()
