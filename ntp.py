# -*- coding: utf-8 -*-
import socket
import time


def main():
    host = ''
    port = 123
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    msg, addr = sock.recvfrom(8192)
    msg = 'Hello Server'.encode('utf-8')
    f = open('./ntp.res.bin', 'rb')
    msg = f.read()
    sock.sendto(msg, (host, addr[1]))
    f.close()
    return

if __name__ == '__main__':
    main()
