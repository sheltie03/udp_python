# -*- coding:utf-8 -*-
import socket
import base64


def main():
    host = "127.0.0.1"
    port = 4000
    last_msg = '.'
    res_msg = ''

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    client.send('..')
    res_msg = client.recv(4096)
    print res_msg
    
    while True:
        msg = raw_input('> ')
        client.send(base64.b64encode(msg))
        res_msg = client.recv(4096)
        if res_msg == last_msg:
            client.send(last_msg)
            break
        print res_msg
    client.close()


if __name__ == '__main__':
    main()
