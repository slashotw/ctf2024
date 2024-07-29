from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
import gmpy2

def generate_rsa(bits):
    p = getPrime(bits)
    q = getPrime(bits)
    n = p * q
    e = 3
    return n, e

def encrypt(m, n, e):
    return pow(m, e, n)

# 生成 flag
flag =  open('./flag','rb').read()
m = bytes_to_long(flag)

# 生成 RSA 公鑰
num_keys = 3
n = [generate_rsa(512)[0] for _ in range(num_keys)]
e = 3

# 使用相同的明文和指數加密
c = [encrypt(m, n[i], e) for i in range(num_keys)]

print(f"e = {e}")
print(f"n = {n}")
print(f"c = {c}")
