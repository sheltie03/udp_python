import random
def nonceGen(size):
    nonce = ''
    while len(nonce) != size:
        flg = random.randint(0, 99) % 3
        if flg == 0:
            nonce += chr(random.randint(48, 57))
        elif flg == 1:
            nonce += chr(random.randint(65, 90))
        elif flg == 2:
            nonce += chr(random.randint(97, 122))
    return nonce
