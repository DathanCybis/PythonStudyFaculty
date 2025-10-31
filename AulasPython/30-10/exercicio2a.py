#se em um dicionario eu estou somando... no outro? subtraindo,

nums1 = [1, 2, 2, 3]
nums2 = [2, 2, 3, 3, 2]
inter = [] # intersecção = 2 , 2 , 3
freq = {}

for num in nums1:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for num in nums2:
    if num in freq and freq[num] > 0:
        inter.append(num) 
        freq[num] -= 1

print(inter)
