#!/usr/bin/env python3
import string
from pwn import *
from base64 import *

def xor(a,b) :
    return bytes([x^y for x, y in zip(a,b)])

r = remote('127.0.0.1', 9005)
r.recvuntil('enc = ')
cipher = b64decode(r.recvline().strip())
print(cipher)

flag = bytearray(cipher)
flag[:10] = xor(xor(b'user=guest',flag[:10]), b'user=admin')

print(bytes(flag))

r.sendlineafter('your cookie = ',b64encode(bytes(flag)))
r.interactive()