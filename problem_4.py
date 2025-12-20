"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

n = 12
n = str(n)
print(n[::-1])


def validPalindrome(n):
    n = str(n)
    return n == n[::-1]
        
print(validPalindrome(9009))

# ------

palindromes = []

high = 999
low = 999

while high != 1:
    result = high * low
    if validPalindrome(result) == True:
        palindromes.append(result)
    low -= 1
    if low == 1:
        high -= 1
        low = high
    
print(palindromes)

max = palindromes[0]

for i in range(len(palindromes)):
    if max < palindromes[i]:
        max = palindromes[i]
    
print(max)

"""
Answer: 906609
"""

