nums = [9, 0, 1, 7, 8, 15]
nums.sort()
set1 = set()
cont = 0

for i in nums:
    if i-1 in set1:
        cont+=1
    set1.add(i)

print(set1)
print(cont)
