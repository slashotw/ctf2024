# coding:utf8
import os
from Crypto.Cipher import AES
import requests
from pwn import *
r = remote("127.0.0.1", 9008)

def queryFactors(n):
	s=[]
	url="http://factordb.com/api?query="+str(n)
	r = requests.get(url)
	factors=r.json()['factors']
	for f in factors:
		for i in range(f[1]):
			s.append(int(f[0]))
	return s

e = int(r.recvline().strip().partition(b' = ')[2].decode())
n = queryFactors(r.recvline().strip().partition(b' = ')[2].decode())
print(n)
c = r.recvline().strip().partition(b' = ')[2].decode().split()
p,q = n[0],n[1]

# 計算d
def egcd(a, b):
  if a == 0:
    return (b, 0, 1)
  else:
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

d = egcd((p - 1) * (q - 1), e)[2]
if d < 0:
    d += (p - 1) * (q - 1)

for i in c :
	m = hex(pow(int(i),d,p*q))[2:]
	print(bytes.fromhex(m).decode(),end="")

