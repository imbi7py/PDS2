numeros = []

print("Digite 5 numeros.")
while len(numeros) < 5:
	try:
		numero = int(input("Digite o proximo numero: "))
		numeros.append(numero)
	except ValueError:
		print("Voce inseriu um numero invalido. Tente novamente")

# for numero in numeros:
	# media += numero

media = sum(numeros) / len(numeros)
print("A media dos numeros inseridos foi: {}".format(media))
