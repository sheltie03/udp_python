# -*- coding: utf-8 -*-
import socket
import time


def main():
    host = ''
    port = 4000
#    local_addr = '192.168.10.255'
    local_addr = '255.255.255.255'
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind((host, port))

    while True:
        msg = 'Hello Server'.encode('utf-8')
        print(msg)
        sock.sendto(msg, (local_addr, port))
    return


if __name__ == '__main__':
    main()
