# -*- coding:utf-8 -*-
import socket
import hashlib #hashlib.md5('').hexdigest()
import nonceGen


def main():
    host = "127.0.0.1"
    port = 4000
    last_msg = 'quit'
    res_msg = ''

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    first_header = 'GET:http://127.0.0.1'
    client.send(first_header)
    a2 = hashlib.md5(first_header).hexdigest()
    res_arr = client.recv(4096).split('.')
    realm = res_arr[0]  # "localhost"
    nonce = res_arr[1]
    print res_arr[2]

    cnonce = nonceGen.nonceGen(10)
    while True:
        msg = raw_input('> ')
        if msg == last_msg:
            client.send(last_msg)
            break
        act = msg.split(':')
        if len(act) == 2:
            a1 = hashlib.md5(act[0] + ':' + realm + ':' + act[1]).hexdigest()
            response = hashlib.md5(a1 + ':' + nonce
                                      + ':' + cnonce + ':' + a2).hexdigest()
            client.send(response + '.' + cnonce)
            res_msg = client.recv(4096)
            print res_msg
        else:
            pass
    client.close()


if __name__ == '__main__':
    main()
