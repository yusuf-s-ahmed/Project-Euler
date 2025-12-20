"""
A number is a perfect square, or a square number, if it is the square of a positive integer.
For example, 25 is a square number because 5^2 = 5 * 5 = 25; it is also an odd square.

The first 5 square numbers are: 1, 4, 9, 16, 25, and the sum of the odd squares is 
1 + 9 + 25 = 35

Among the first 141 thousand square numbers, what is the sum of all the odd squares?
"""

squares = []
i = 1

while len(squares) != 141000:
    x = i**2
    squares.append(x)
    i += 1

print(squares)

sum = 0

for j in range(len(squares)):
    if squares[j] % 2 != 0:
        sum += squares[j]

print(sum)

"""
Answer: 467203499976500
"""