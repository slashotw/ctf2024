import gmpy2
from pwn import *

r = remote("127.0.0.1", 9009)

ans = b''
token = r.recvline().decode().split()
for i in token :
    step = int(i)
    (t1, t2) = gmpy2.iroot(step, 3)
    print(int(t1).to_bytes(1, 'big').decode(),end="")