
nome = input("Digite seu nome: ")
qtd_char = len(nome)

if qtd_char <= 0:
	print("{} seu nome é nulo e invalido".format(nome))
elif qtd_char <= 4:
	print("{} seu nome é curto".format(nome))
elif qtd_char <= 6:
	print("{} seu nome é normal".format(nome))
else:
	print("{} seu nome é muito grande".format(nome))
