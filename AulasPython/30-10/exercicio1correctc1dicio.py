freq_unique = {}

s = 'rato'
t = 'tora'

for letra in s:
    if letra in freq_unique:
        freq_unique[letra] += 1
    else:
        freq_unique[letra] = 1

for letra in t:
    if letra in freq_unique:
        freq_unique[letra] += 1
    else:
        freq_unique[letra] = 1
cont = 0
for i in freq_unique:
    if freq_unique[i] == 2:
        cont+=1
    
if cont == len(freq_unique):
    print("Sim")
else:
    print("Não")
