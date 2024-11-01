"""
String Compression
Implement a basic compression algorithm that shortens a string by representing repeated characters (e.g., "aaabb" → "a3b2").

"""
def stringCompressor(s):
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    compressed = ""
    seen = set()  # To keep track of characters already added

    for char in s:
        if char not in seen:
            count = s.count(char)  # Count occurrences of the character
            compressed += f"{char}{count}"
            seen.add(char)  # Mark the character as processed

    return compressed

print(stringCompressor("Helloe world")) #output h1e2l3o2w1r1d1

def stringCompressorwSpace(s):
    s=s.lower().split(" ")
    compressed=""
    seen = set()
    compressed_result=[]
    for word in s:
        for char in word:
            if char not in seen:
                count=word.count(char)
                compressed+= f'{char}{count}'
                seen.add(char)
        compressed_result.append(compressed)
        compressed=""
        seen.clear()
    return " ".join(compressed_result[:])

print(stringCompressorwSpace("Helloe world")) #output h1e2l3o2w1r1d1



                
                

        
