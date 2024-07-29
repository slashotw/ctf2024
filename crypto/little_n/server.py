import random
from Crypto.Util.number import getPrime

flag = open('./flag').read()

def generate_keypair():
    p = getPrime(16)
    q = getPrime(16)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    d = pow(e, -1, phi)

    return (e, n), (d, n)


def encrypt(plaintext, public_key):
    e, n = public_key
    m = int.from_bytes(plaintext.encode(), 'big')  
    c = pow(m, e, n)
    return c

def decrypt(ciphertext, private_key):
    d, n = private_key
    m = pow(ciphertext, d, n)
    return m.to_bytes((m.bit_length() + 7) // 8, 'big').decode()  



def main():
    public_key, private_key = generate_keypair()
    c = []
    print(f"e = {public_key[0]}")
    print(f"n = {public_key[1]}")
    print(f"c = ",end="")
    for i in flag :
        print(encrypt(i, public_key),end=" ")
    print(f"\n")

if __name__ == "__main__":
    main()
