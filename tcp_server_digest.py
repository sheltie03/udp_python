# -*- coding: utf-8 -*-
import socket
import hashlib
import nonceGen


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 4000
    host = '127.0.0.1'
    last_msg = '.'
    req_msg = ''

    server.bind((host, port))
    server.listen(1)
    sock, addr = server.accept()
    realm = 'localhost'
    nonce = nonceGen.nonceGen(10)
    a1 = '5308eb9067f9bc672f724e310ad0efeb'  # hashlib.md5('admin:localhost:888888').hexdigest()
    a2 = hashlib.md5('GET:http://127.0.0.1').hexdigest()
    order = 'Input your "user_name:password" and press enter ...'
    
    while True:
        req_msg = sock.recv(4096)
        if req_msg == last_msg:
            sock.send(last_msg)
            break
        elif req_msg == 'GET:http://127.0.0.1':
            sock.send(realm + '.' + nonce + '.' + order)
        elif req_msg.count('.') == 1:
            req_arr = req_msg.split('.')
            response = req_arr[0]
            cnonce = req_arr[1]
            ans = a1 + ':' + nonce + ':' + cnonce + ':' + a2
            if response == hashlib.md5(ans).hexdigest():
                f = open('welcome_banner.txt', 'r')
                banner = f.read()
                sock.send(banner)
            else:
                sock.send('Incorrect username or password. Try agin ...\n')
        sock.send(order)
    sock.close()


if __name__ == '__main__':
    main()
