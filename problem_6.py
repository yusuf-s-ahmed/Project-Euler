"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sumOfSquares(n):
    total = 0
    for i in range(1, n + 1):
        total += i**2
    return total




def squareOfSums(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    total = total**2
    return total

print(squareOfSums(100) - sumOfSquares(100))

"""
Answer: 25164150
"""