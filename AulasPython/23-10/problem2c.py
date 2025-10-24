nums = [100, 5, 90, 2, 4, 3]
meu_set = set(nums)
tamanho_max = 0
for n in meu_set:
    if n-1 not in meu_set:
        tamanho_sequencia = 1
        while n+1 in meu_set:
            tamanho_sequencia += 1
            n = n+1
        if tamanho_sequencia > tamanho_max:
            tamanho_max = tamanho_sequencia

print(tamanho_max)
