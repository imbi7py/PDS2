def calculo(n1, n2, n3):
	result = n1 + n2 + n3;
	print("Resultado do calculo: {}".format(result))

def main():
	try:
		numero1 = int(input("Digite o numero 1: "))
		numero2 = int(input("Digite o numero 2: "))
		numero3 = int(input("Digite o numero 3: "))
		calculo(numero1, numero2, numero3)
	except ValueError:
		print("Voce inseriu um numero invalido. Insira apenas numeros inteiros")

main()
