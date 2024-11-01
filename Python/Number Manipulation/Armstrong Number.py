"""
Armstrong Number: A number where the sum of its digits each raised to the power of the number of 
digits equals the number itself.
Example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 =153.
"""
def isArmstrong(n):
    ns=str(n)
    power= len(ns)
    sum=0
    for x in ns:
        sum+= pow(int(x),3)
    return sum==n
print(isArmstrong(1531))