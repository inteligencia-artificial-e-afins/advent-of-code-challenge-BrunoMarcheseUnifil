elements = []

with open("input05.txt", encoding='utf-8', mode='r') as arquivo:
    for x in range(8):
        elements.append(arquivo.readline().replace('\n', ''))
    stack_numbers = arquivo.readline()
    arquivo.readline() # pulando linha em branco

    moves = []
    for x in arquivo.readlines():
        x = x.replace('\n', '').split(' ')
        moves.append({ 'move': int(x[1]), 'from': int(x[3]), 'to': int(x[5]) })


stacks = []
stacks_part2 = []
for x in range(9):
    idx = stack_numbers.index(str(x+1))
    aux = []
    for y in elements[:8]:
        if not y[idx] == ' ':
            aux.append(y[idx])
    stacks.append(aux.copy())
    stacks_part2.append(aux.copy())
    aux.clear()

for m in moves:
    stack_from = stacks[m['from'] -1]
    stack_to = stacks[m['to'] -1]

    for n in range(m['move']):
        stack_to.insert(0, stack_from.pop(0))

for s in stacks:
    print(s)


# PARTE 2
for m in moves:
    stack2_from = stacks_part2[m['from'] -1]
    stack2_to = stacks_part2[m['to'] -1]
    sf_reversed = stack2_from.copy()[0:m['move']]
    sf_reversed.reverse()

    for n in sf_reversed:
        stack2_to.insert(0, n)
    
    del stack2_from[:m['move']]

for s in stacks_part2:
    print(s)