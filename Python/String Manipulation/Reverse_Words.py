def reverseSentence(s):
    reversed = s[::-1]
    return "".join(reversed)

def reverseWords(s):
    words = s.split(" ")
    return " ".join(words[::-1])
    

print(reverseWords("Hello World!"))

