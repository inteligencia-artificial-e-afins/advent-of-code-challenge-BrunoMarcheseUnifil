with open("input08.txt", encoding='utf-8', mode='r') as arquivo:
    arvores = [a.strip() for a in arquivo.readlines()]

linhas = len(arvores)
colunas = len(arvores[0])

scores = []
for x in range(1, linhas-1):
    for y in range(1, colunas-1):
        arvore = arvores[x][y]

        cima = [arvores[x][y-i] for i in range(1, y+1)]
        baixo = [arvores[x][y+i] for i in range(1, colunas-y)]
        direita = [arvores[x-i][y] for i in range(1, x+1)]
        esquerda = [arvores[x+i][y] for i in range(1, linhas-x)]

        score = 1
        for z in (esquerda, direita, cima, baixo):
            tracker = 0
            for w in range(len(z)):
                if z[w] < arvore:
                    tracker += 1
                elif z[w] == arvore:
                    tracker += 1
                    break
                else:
                    break
            score *= tracker
        scores.append(score)

max(scores)