def findLongestWord(s):
    words=s.split(" ")
    length= 0
    longestWord = ""
    for word in words:
        if len(word) > length: 
            length= len(word)
            longestWord =word
    return longestWord 
print(findLongestWord("helloe World"))
