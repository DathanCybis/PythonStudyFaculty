#Dados duas listas, uma com nomes e outra com idades(na mesma ordem), crie um dicionário onde as chaves #19:17
#São os nomes e os valores são as idades.
#Exemplo: nomes = ["Ana", "João", "Maria"]
#         idades = ["25, 33, 21"]
#         saída: {"Ana": 25, "João": 33, "Maria": 21} 
#NP2: Vai cair dicionário.


nomes = ["Ana", "João", "Maria"]
idades = [25, 33, 21]
nomes_idade = {}

for i, v in enumerate(nomes):
    nomes_idade[nomes[i]] = idades[i]
    

print(nomes_idade)
