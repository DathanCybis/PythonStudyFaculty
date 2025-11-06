s = "egg" 
t = "add"
vistos1 = {}
vistos2 = {}

for i in range(len(s)):
    a = s[i]
    b = t[i]
    if a in vistos1 and vistos1[a] != b:
        print("false") #return False
    vistos1[a] = b
    vistos2[b] = a

print("true") #return True
