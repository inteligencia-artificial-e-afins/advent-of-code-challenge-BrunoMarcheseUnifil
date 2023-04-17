with open("input03.txt", encoding='utf-8', mode='r') as arquivo:
    rucksack = [a.replace("\n", "") for a in arquivo.readlines()]

compartments = [ [r[0:len(r)//2], r[len(r)//2:]] for r in rucksack ]

letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
prioridade = {}
for i, x in enumerate(letras):
    prioridade[x] = i + 1


soma = 0
for c in compartments:
    for x in c[0]:
        if x in c[1]:
            soma += prioridade[x]
            break

print(soma)