#problema 1 - contém duplicado.

nums = [1, 2, 3, 1]
set1 = set()
resultado = "Não"

for i in nums:
    if i in set1:
        resultado = 'Sim'
    set1.add(i)
print(resultado)
