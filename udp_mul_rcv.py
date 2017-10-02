# -*- coding: utf-8 -*-
import socket


def main():
    local_addr = '192.168.10.105'
    multi_gp = '239.255.0.1'  # Multicast Address
    port = 4000
    bufsize = 4096

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', port))
    sock.setsockopt(socket.IPPROTO_IP,
                    socket.IP_ADD_MEMBERSHIP,
                    socket.inet_aton(multi_gp) + socket.inet_aton(local_addr))
    while True:
        print(sock.recv(bufsize))
    return


if __name__ == '__main__':
    main()
