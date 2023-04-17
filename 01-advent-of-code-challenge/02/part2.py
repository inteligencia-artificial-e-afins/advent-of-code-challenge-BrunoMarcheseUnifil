with open("input02.txt", encoding='utf-8', mode='r') as arquivo:
    matches = [a.replace("\n", "").split() for a in arquivo.readlines()]


def win(shape):
    if shape == 'A':
        return 2
    elif shape == 'B':
        return 3
    else:
        return 1


def draw(shape):
    if shape == 'A':
        return 1
    elif shape == 'B':
        return 2
    else:
        return 3


def lost(shape):
    if shape == 'A':
        return 3
    elif shape == 'B':
        return 1
    else:
        return 2


soma = 0
for item in matches:
    if item[1] == 'X':
        soma += lost(item[0])
    elif item[1] == 'Y':
        soma += draw(item[0]) + 3
    else:        
        soma += win(item[0]) + 6


print(soma)