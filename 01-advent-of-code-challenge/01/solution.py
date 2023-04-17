calorias = []

with open("input01.txt", encoding='utf-8', mode='r') as arquivo:
    lines = [ (a.replace('\n', " ")) if a =="\n" else int(a.replace('\n', "")) for a in arquivo.readlines() ]

arr = []
for x in lines:
    if not x == " ":
        arr.append(x)
    else:
        calorias.append(arr)
        arr.clear()

arr = []
for n in calorias:
    arr.append(sum(n))

arr.sort()
print("O maior número de calorias é:", max(arr)) # PARTE 1
print('A soma das 3 maiores quantidades de calorias é igual a:', sum(arr[len(arr)-3:len(arr)])) # PARTE 2