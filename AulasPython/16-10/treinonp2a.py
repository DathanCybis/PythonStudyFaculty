#problema two sum
#com estrutura de dados
nums = [2, 9, 11, 7, 15]
vistos = {}
alvo = 9

for i in range(0, len(nums)):
    if nums[i] < alvo:
        vistos = {'indice': {i}, 'num': {nums[i]}}

    if i == len(nums):
        ...
        

print(vistos)