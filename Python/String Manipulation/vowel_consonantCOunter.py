st= "Hello I am Tushar!"

def VC_Counter(s):
    vw=['a','e','i','o','u']
    vcount=0
    ccount=0
    for x in s:
        if x in vw:
            vcount+=1
        elif ((x not in vw) and x.isalpha()):
            ccount+=1

    return [vcount,ccount]

print(type(VC_Counter("Hello World!")))