#problema two sum
#com estrutura de dados
nums = [2, 9, 11, 7, 15]
#nums = [3, 2, 4]
vistos = {}
alvo = 9

for i in range(0, len(nums)):
    if nums[i] > alvo:
        par = nums[i] - alvo
    else:
        par = alvo - nums[i]

    if par in vistos:
        print(f"{nums[i]} + {par} = {alvo}")

    vistos[i] = i
    vistos[i] = nums[i]

print(vistos)
    
