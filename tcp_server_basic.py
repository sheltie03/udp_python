# -*- coding: utf-8 -*-
import socket
import base64

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 4000
    host = '127.0.0.1'
    last_msg = '.'
    req_msg = ''

    server.bind((host, port))
    server.listen(1)
    sock, addr = server.accept()
    pass_phrase = base64.b64encode('admin:888888')
    
    while True:
        req_msg = sock.recv(4096)
        if req_msg == last_msg:
            sock.send(last_msg)
            break
        elif req_msg == '..':
            sock.send('Input your "user_name:password" and press enter ...')
        elif req_msg == pass_phrase:
            f = open('welcome_banner.txt', 'r')
            banner = f.read()
            sock.send(banner)
        else:
            sock.send('Incorrect username or password. Try agin ...')
    sock.close()


if __name__ == '__main__':
    main()
