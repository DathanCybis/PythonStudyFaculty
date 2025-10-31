#se em um dicionario eu estou somando... no outro? subtraindo,

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
inter = [] # intersecção = 9 , 4
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
