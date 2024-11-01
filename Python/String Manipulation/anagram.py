from collections import Counter

# Anagram Checker
# Create a function that checks if two given strings are anagrams of each other.
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
#  using all the original letters exactly once. 
# For example:

# "listen" and "silent" are anagrams because they use the exact same letters in a different order.
# "triangle" and "integral" are also anagrams.

# s1="The Morse Code"
# s2="Here come dots"

#Function 01 
def isAnagram(s1,s2):
    s1=s1.lower().replace(" ","")
    s2= s1.lower().replace(" ","")   
    if(len(s1) != len(s2)): return False
    for x in s1:
        if(x not in s2 and (s1.count(x) != s2.count(x))): return False
    return True

#Function 02
def isAnagram02(s1,s2):
    s1=s1.lower().replace(" ","")
    s2= s1.lower().replace(" ","")  
    return sorted(s1)==sorted(s2)

#Function 03: using collection counter 
"""
Counter Function
it reuturns a dictionary with occurance as value for each element 
"""

def isAnagram03(s1,s2):
    s1=s1.lower().replace(" ","")
    s2=s2.lower().replace(" ","")
    return Counter(s1) == Counter(s2)


# print(isAnagram("Silent","listen")) #true
# print(isAnagram("The Morse Code","Here come dots")) #true
# print(isAnagram("The Morse Code","Here come do ts")) # true

# print(isAnagram02("Silent","listen")) #true
# print(isAnagram02("The Morse Code","Here come dots")) #true
# print(isAnagram02("The Morse Code","Here come do ts")) # true

print(isAnagram03("Silent","listen")) #true
print(isAnagram03("The Morse Code","Here come dots")) #true
print(isAnagram03("The Morse Code","Here come do ts")) # trueprint(isAnagram3())