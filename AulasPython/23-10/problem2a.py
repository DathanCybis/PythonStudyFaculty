nums = [9, 0, 1, 7, 8, 15]
set1 = set()
set2 = set()

for i in nums:
    set1.add(i)
    print(set1)

cont = 0
for i in set1:
    if i-1 in set2:
        cont+=1
    set2.add(i)

print(cont)
