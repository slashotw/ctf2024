from pwn import *

r = remote('127.0.0.1', 9003)


r.sendlineafter('user = ', 'A' * 11 + 'A' * 16 + '1' * 9 )
token = r.recvline().strip().partition(b' = ')[2].decode()
token = bytes.fromhex(token)
token = token[:16] + token[32:48] + token[16:32] + token[48:]
print("mytoken==>",token)
r.sendlineafter('cookie = ', token.hex())

r.interactive()



"""
user=11111111111
1111111111111111
111111111&admin=
0&00000000000000
"""