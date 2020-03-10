lista = [["p1", 42], ["p1", 52], ["p1", 37], ["p1", 22], ["p1", 26], ["p1", 12]]

# lista.sort(key=lambda item:item[1])

print(sorted(lista, key=lambda item:item[1]))
print(lista)
