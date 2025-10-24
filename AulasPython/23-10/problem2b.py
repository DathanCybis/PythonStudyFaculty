nums = [9, 0, 1, 7, 8, 15]
set1 = set()
cont=0

while True:
    for i in nums:
        set1.add(i)
        print(set1) 
        if nums[0]-1 in set1 or nums[0]+1 in set1:
            cont+=1
    break

print(cont)

