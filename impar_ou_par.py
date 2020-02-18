try:
	numero = int(input("Digite um numero inteiro: "));
	if numero == 0:
		print("Number {} is neutro.".format(numero))
	elif (numero % 2) == 0:
		print("Number {} is par.".format(numero))
	else:
		print("Number {} is impar.".format(numero))
except:
	print("Digite apenas numeros inteiros.")
