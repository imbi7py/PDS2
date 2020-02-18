def main():
	while True:
		print(("=" * 6) + (" Menu ") + ("=" * 6))
		print("1 - Continuar")
		print("0 - Sair")

		try:
			option = int(input("Digite a opcao: "))
		except:
			print("Digite um valor inteiro.")

		if option < 0 or option > 1:
			print("Invalid option.")
		elif option == 0:
			break;
		elif option == 1:
			calculo = input("Digite o calculo: ")
			manager(calculo)
	
def soma(a, b):
	try:
		print("Result {}".format(a + b))
	except:
		print("Could not execute the soma")

def subtracao(a, b):
	try:
		print("Result {}".format(a - b))
	except:
		print("Could not execute the subtracao")

def divisao(a, b):
	try:
		print("Result {}".format(a / b))
	except:
		print("Could not execute the divisao")

def multiplicacao(a, b):
	try:
		print("Result {}".format(a * b))
	except:
		print("Could not execute the multiplicacao")

def manager(conta):
	final = 0;
	if "+" in conta:
		valor = conta.split("+")
		num1 = int(valor[0])
		num2 = int(valor[1])
		soma(num1, num2)
	if "-" in conta:
		valor = conta.split("-")
		num1 = int(valor[0])
		num2 = int(valor[1])
		subtracao(num1, num2)
	if "/" in conta:
		valor = conta.split("/")
		num1 = int(valor[0])
		num2 = int(valor[1])
		divisao(num1, num2)
	if "*" in conta:
		valor = conta.split("*")
		num1 = int(valor[0])
		num2 = int(valor[1])
		multiplicacao(num1, num2)

main()

