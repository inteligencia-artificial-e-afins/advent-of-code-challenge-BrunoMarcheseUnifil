with open("input06.txt", encoding='utf-8', mode='r') as arquivo:
    linha = arquivo.readline().strip()

# PARTE 1
for i in range(len(linha)):
    if len(set(linha[i:i+4]))==4:
        print(i+4)
        break

# PARTE 2
for i in range(len(linha)):
    if len(set(linha[i:i+14]))==14:
        print(i+14)
        break