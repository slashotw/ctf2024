#!/usr/bin/env python3
import random

flag = open('./flag').read().strip()

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(limit):
    return [n for n in range(2, limit) if is_prime(n)]

def main():
    print("""
<<<================================>>>
Remote Crypto Miner v1.0

rule:
Factor the number into two primes
Enter the two prime factors (separated by space)

example:  
problem: 143
prime numbers: 11 13

example: 
problem: 77
prime numbers: 7 11

solve 1 number to get 1 point
win a flag by 50 point !
<<<================================>>>
""")
    points = 0
    primes = generate_primes(100)  # 生成100以內的質數
    
    while points < 50:
        p1, p2 = random.sample(primes, 2)
        product = p1 * p2
        print(f"problem: {product}")
        
        user_input = input("prime numbers: ")
        user_p1, user_p2 =  int(user_input.split()[0]) ,  int(user_input.split()[1] )
        
        if user_p1 * user_p2 == product and is_prime(user_p1) and is_prime(user_p2):
            points += 1
            print(f"Correct! Points: {points}")
        else:
            print("Incorrect. Try again.")
        
        print()  # Empty line for readability
    
    print(f"Thanks ! Here's your flag: {flag}")

try :
    main()
except : 
    print("error detected")