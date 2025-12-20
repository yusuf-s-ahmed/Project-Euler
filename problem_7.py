"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10,001st prime number?
"""

primes = []
number = 2

while len(primes) != 10002:
    
    #print(f"Number: {number}")
    sqrt = int(number ** 0.5) + 1
    prime = True

    #print(f"Looping from 2 to {sqrt}")
    for x in range(2, sqrt):
        if number % x == 0:
            #print(f"Number is not prime, as it can be divided by {x}.")
            prime = False
            break
        
    #print(f"{number} is prime\n")
    if prime:
        primes.append(number)

    number += 1


print(primes[10000])