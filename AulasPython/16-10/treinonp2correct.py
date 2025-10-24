#problema two sum
#com estrutura de dados
#nums = [2, 9, 11, 7, 15]
nums = [3, 2, 4]
vistos = {}
alvo = 6

for i in range(0, len(nums)):
    par = alvo - nums[i]

    if par in vistos:
        print(f"{nums[i]} + {par} = {alvo}")

    vistos[nums[i]] = [i]
    print(vistos)


