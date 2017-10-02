# -*- coding: utf-8 -*-
import socket
import time


def main():
    host = ''
    bro_addr = '192.168.1.255'
    port = 4000
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.bind((host, port))
    while True:
        msg, addr = sock.recvfrom(8192)
        msg_ans = 'Hello Client'.encode('utf-8')
        sock.sendto(msg_ans, (bro_addr, addr[1]))
        print(sock.recvfrom(8192))
        print(msg)
    return

if __name__ == '__main__':
    main()
