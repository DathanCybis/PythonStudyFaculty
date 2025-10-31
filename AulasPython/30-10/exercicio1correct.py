freq_s = {}
freq_t = {}

s = 'rato'
t = 'tora'

for letra in s:
    if letra in freq_s:
        freq_s[letra] += 1
    else:
        freq_s[letra] = 1

for letra in t:
    if letra in freq_t:
        freq_t[letra] += 1
    else:
        freq_t[letra] = 1

if freq_s == freq_t:
    print("Sim")
else:
    print("Não")
