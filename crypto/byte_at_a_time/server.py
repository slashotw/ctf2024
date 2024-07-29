#!/usr/bin/env python3
import os
from Crypto.Cipher import AES

KEY = os.urandom(16)
flag =  open('./flag','rb').read()

def pad(m):
    padlen = -len(m) % 16
    return m + bytes([0] * padlen)

def main():
    aes = AES.new(KEY, AES.MODE_ECB)
    while True:
        message = bytes.fromhex(input('message = ').strip())
        cipher = aes.encrypt(pad(message+flag))
        print(f'message+flag = {cipher.hex()}')

try:
    main()
except:
    print("error occurred \nnote: HEX input only")
