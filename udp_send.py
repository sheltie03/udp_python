# -*-coding: utf-8 -*-
import socket
import time
import struct


def main():
    host = '127.0.0.1'
    port = 123
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        msg = struct.pack('5c', 'aaaaa')
        sock.sendto(msg, (host, port))
        time.sleep(1)
    return


if __name__ == '__main__':
    main()
