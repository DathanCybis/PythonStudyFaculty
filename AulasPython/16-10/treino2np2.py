nums = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0]
cont = 0
max = 0
for i in nums:
    if i == 0:
        cont = 0
    else:
        cont += 1
        if max < cont:
            max = cont        

print(f"a contagem máxima foi de {max}")
