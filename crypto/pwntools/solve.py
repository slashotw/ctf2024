from pwn import *

r = remote("127.0.0.1", 9001)

r.recvuntil(b"<<<================================>>>")
r.recvuntil(b"<<<================================>>>")

for _ in range(50):
    r.recvuntil(b"problem: ")
    n = int(r.recvline().strip())
    
    for i in range(2, n):
        if n % i == 0:
            j = n // i
            print(n,"->",i,j)
            r.sendlineafter(b"prime numbers: ", f"{i} {j}".encode())
            break
    
    r.recvline()  # Correct! Points: X

r.interactive()