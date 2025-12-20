"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""


n = 600851475143
i = 1
factors = []

while n != 1:

    if n % i == 0:
        n = n / i
        factors.append(i)
        print(n)
        print(factors)

    i += 1

"""
Answer: 6857
"""
