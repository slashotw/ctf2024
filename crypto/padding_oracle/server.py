#!/usr/bin/env python3
import os
from Crypto.Cipher import AES

KEY = os.urandom(16)
IV = os.urandom(16)
FLAG = open('./flag', 'rb').read()

def pad(data):
    p = 16 - len(data) % 16
    return data + bytes([p]) * p

def unpad(data):
    if not all([x == data[-1] for x in data[-data[-1]:]]):
        raise ValueError
    return data[:-data[-1]]

def main():
    aes = AES.new(KEY, AES.MODE_CBC, IV)
    cipher = aes.encrypt(pad(FLAG))
    print(f"IV+flag = {(IV + cipher).hex()}")
    while True:
        cipher = bytes.fromhex(input('decrypt = ').strip())
        iv, cipher = cipher[:16], cipher[16:]
        try:
            aes = AES.new(KEY, AES.MODE_CBC, iv)
            try: 
                dec = aes.decrypt(cipher)
            except:
                print("decrypt error")
            plain = unpad(dec)
            print('success')
        except ValueError:
            print('padding error')
        print()

try :
    main()
except:
    print("program error!")