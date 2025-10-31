#Anagrama válido.

s = {}
t = {}

s = str(input("Digite a primeira palavra: ")).strip().lower()
t = str(input("Digite a segunda palavra: ")).strip().lower()
qnt = 0

for i in s:
    for j in t:
        if i == j:
            qnt+=1

if len(s) == qnt:
    print("Sim")
else:
    print("Não")
