import re 

# ************************************** Palindrome Check **************************************
# Write a function to check if a given string is a palindrome.

#Function 01
st = "Madam"
def isPalindrom(s):
    for ind in range(0,len(st)-1):
        if (s[ind]!=s[-1-ind]): 
            print("Not Palindrom")
            return False
            break
    print("Is Palindrom") 

#Function 01
def isPalindrom2(s):
    s=s.lower() #considered the case 
    if(s==s[::-1]): return True
    return False
print(isPalindrom2(st))

#Function 03
def isPlaindrome3(s):
    return  s==("".join(reversed(s)))


print(isPlaindrome3("madam"))



