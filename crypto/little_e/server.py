import random
from Crypto.Util.number import getPrime

flag = open('./flag').read()


def generate_keypair():
    p = getPrime(256)
    q = getPrime(256)
    n = p*q
    phi = (p - 1) * (q - 1)
    e = 3

    return (e, n)

def encrypt(plaintext, public_key):
    e, n = public_key
    m = int.from_bytes(plaintext.encode(), 'big') 
    c = pow(m, e, n)
    return c


def main():
    public_key = generate_keypair()
    for i in flag :
        encrypted_flag = encrypt(i, public_key)
        print(f"{encrypted_flag}",end=" ")
        
    print()


if __name__ == "__main__":
    main()