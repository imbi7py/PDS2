def percentual(numero, percentual):
	percentual = numero + (numero * (percentual / 100))
	return percentual

def main():
	try:
		numero = int(input("Digite o numero: "))
		porcento = 0
		while(True):
			porcento = int(input("Digite o percentual: "))
			if (porcento >= 0):
				break
			else:
				print("Voce inseriu um numero invalido. Insira apenas inteiros e positivos")
		resultado = percentual(numero, porcento)
		print("Resultado do numero acrescido de seu percentual: {}".format(resultado))
	except ValueError:
		print("Voce inseriu um numero invalido. Insira apenas inteiros")

main()
