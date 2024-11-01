"""
Disarium Number: A number where the sum of its digits each raised to the power of its position
equals the number itself. Example, 135 is a Disarium number because 1^1 + 3^2 + 5^3 =135

"""
def isdisariumNumber(n):
    ns=str(n)
    power=1
    sum=0
    for x in ns:
        sum+= pow(int(x),power)
        power+=1
    return sum==n
print(isdisariumNumber(135))
