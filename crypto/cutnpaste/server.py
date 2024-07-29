#!/usr/bin/env python3
import os
from Crypto.Cipher import AES

KEY = os.urandom(16)
FLAG = open('./flag').read()

def pad(m):
    padlen = -len(m) % 16
    return m + bytes([0] * padlen)

def main():
    aes = AES.new(KEY, AES.MODE_ECB)
    
    # encrypt token
    user = input('user = ').strip()
    if '&' in user:
        raise ValueError

    token = f'user={user}&admin=0&'.encode()


    token = aes.encrypt(pad(token))
    print(f'cookie = {token.hex()}')
    
    # decrypt token
    token = bytes.fromhex(input('cookie = ').strip())
    token = aes.decrypt(token)
    user, role, _ = token.split(b'&')
    permission = role.split(b'=')[1]
    print(f"\nuser:{user.split(b'=')[1].decode()} , admin permission:{permission.decode()}")
    if permission == b"0" :
        print(f'only admin can get flag')
    else :
        print(FLAG)

try:
    main()
except:
    print("error@@")