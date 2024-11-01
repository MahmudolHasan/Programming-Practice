"""Remove Duplicates
Create a function that removes duplicate characters from a string while preserving the order.
"""
def removeDup(s):
    words=s.split(" ")
    modified=""
    seen=set()
    mWords=[]
    for word in words:
        for char in word:
            if char not in seen:
                modified+=f'{char}'
                seen.add(char)
        mWords.append(modified)
        seen.clear()
        modified=""
    return " ".join(mWords[:])
print(removeDup("hello world"))
                
