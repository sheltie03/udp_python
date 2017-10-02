# -*- coding: utf-8 -*-
import socket
import time


def main():
    local_addr = '192.168.10.105'
    multi_gp = '239.255.0.1'  # Multicast Address
    port = 4000
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.IPPROTO_IP,
                    socket.IP_MULTICAST_IF,
                    socket.inet_aton(local_addr))
    while True:
        msg = 'Hello Server'.encode('utf-8')
        print(msg)
        sock.sendto(msg, (multi_gp, port))
        time.sleep(1)
    return


if __name__ == '__main__':
    main()
