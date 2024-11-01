import math
"""
Perfect Number: A number that is equal to the sum of its proper divisors.
Example, 28 is a Perfect number because 1+2+4+7+14=28
"""

def isPerfect(n):
    sum = 0
    for x in range(1,math.ceil(n/2)+1):
        if(n%x==0):
            sum+= x
    return n==sum
print(isPerfect(28))