"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible (divisible with no remainder) by all of the numbers from 1 to 20?

"""

n = 1
subject = 1

while subject != 21:
    if n % subject != 0:
        n += 1
        subject = 1
    else:
        subject += 1

print(n)

"""
Answer: 232792560
"""
