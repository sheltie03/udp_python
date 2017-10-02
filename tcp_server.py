# -*- coding: utf-8 -*-
import socket
import time


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 4000
    host = '127.0.0.1'
    last_msg = '.'
    req_msg = ''

    server.bind((host, port))
    server.listen(1)
    sock, addr = server.accept()

    while True:
        req_msg = sock.recv(4096)
        if req_msg == last_msg:
            sock.send(last_msg)
            break
        print(req_msg)
        sock.send(req_msg)
    sock.close()


if __name__ == '__main__':
    main()
