with open("input03.txt", encoding='utf-8', mode='r') as arquivo:
    rucksack = [a.replace("\n", "") for a in arquivo.readlines()]

groups = [rucksack[n:n+3] for n in range(0, len(rucksack), 3)]

letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
prioridade = {}
for i, x in enumerate(letras):
    prioridade[x] = i + 1

soma = 0
for x in groups:
    for y in x[0]:
        if y in x[1] and y in x[2]:
            soma += prioridade[y]
            break

print(soma)