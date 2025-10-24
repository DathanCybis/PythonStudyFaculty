#problema two sum
#com estrutura de dados

nums = [2, 9, 11, 7, 15]
alvo = 9
temp = 0
cont = 1
for i in enumerate(nums):
    if i[0] == 0:
        temp = i[1]
    else:
        if temp + i[1] == alvo:
            print(f"{temp} + {i[1]} = {alvo}")
    print(i[1])

print(f"{temp}")

