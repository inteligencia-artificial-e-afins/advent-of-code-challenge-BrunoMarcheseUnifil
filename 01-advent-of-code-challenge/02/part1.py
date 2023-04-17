with open("input02.txt", encoding='utf-8', mode='r') as arquivo:
    matches = [a.replace("\n", "").split() for a in arquivo.readlines()]
    print(matches)


def draw(match):
    if match[0] == 'A' and match[1] == 'X':
        return (True, 4)
    elif match[0] == 'B' and match[1] == 'Y':
        return (True, 5)
    elif match[0] == 'C' and match[1] == 'Z':
        return (True, 6)
    else:
        return (False,)


def win(match):
    if match[0] == 'A' and match[1] == 'Y':
        return (True, 8)
    elif match[0] == 'B' and match[1] == 'Z':
        return (True, 9)
    elif match[0] == 'C' and match[1] == 'X':
        return (True, 7)
    else:
        return (False,)


def loss(match):
    if match[1] == "X":
        return 1
    elif match[1] == "Y":
        return 2
    else:
        return 3;


soma = 0
for item in matches:
    d = draw(item)
    if d[0]:
        soma += d[1]
    else:
        w = win(item)
        if w[0]:
            soma += w[1]
        else:
            soma += loss(item)

print(soma)