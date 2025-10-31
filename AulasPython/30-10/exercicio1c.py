s = 'rato'
t = 'tora'
freq_s = {}
freq_t = {}

for i in s:
    #freq_s[i] = 1
    if freq_s[i] != 0:
        freq_s[i] += 1
    else:    
        freq_s[i] = 1

    print(freq_s[i])
