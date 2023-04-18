with open("input08.txt", encoding='utf-8', mode='r') as arquivo:
    arvores = [a.replace('\n', '') for a in arquivo.readlines()]

linhas = []
for a in arvores:
    lin = []
    for x in a:
        lin.append(int(x))
    linhas.append(lin.copy())

colunas = []
for i in range(len(arvores[0])):
    col = []
    for a in arvores:
        col.append(int(a[i]))
    colunas.append(col.copy())

# verificar visibilidade das arvores do meio
# separar linha / coluna em antes e depois da arvore (a arvore pode ser visivel só de 1 lado)
# antes = [:i] | depois = [i+1:]

def visibilidade_coluna(item, pos, coluna):
    altura = int(item)
    antes = coluna[:pos]
    depois = coluna[pos+1:]
    return not (max(antes) >= altura and max(depois) >= altura)

def visibilidade_linha(item, pos, linha):
    altura = int(item)
    antes = linha[:pos]
    depois = linha[pos+1:]
    return not (max(antes) >= altura and max(depois) >= altura)


ultimo_index = len(arvores[0]) -1
soma = 0

for i in range(1, len(arvores)-1):
    for idx, x in enumerate(arvores[i]):
        if not (idx == 0 or idx == ultimo_index):
            vc = visibilidade_coluna(x, i, colunas[idx])
            vl = visibilidade_linha(x, idx, linhas[i])
            if vc or vl:
                soma += 1


# contabilizar as arvores das bordas (primeira e ultima linha e coluna)
bordas_hor = len(arvores[0]) * 2 # o tamanho das linhas é igual
bordas_vert = (len(arvores) - 2) * 2 # numero de arvores nas laterais tirando primeira e ultima linha

print(soma + bordas_hor + bordas_vert)