nome = input("Insira seu nome: ")
try:
	idade = int(input("Insira sua idade: "))
except:
	print("Digite apenas numeros inteiros.")

# if idade > 18:
	# print("{}, voce pode pegar emprestimo").format(nome);
if idade < 1:
	print("{}, voce nao possui uma idade valida.".format(nome))
elif idade > 20 and idade < 40:
	print("{}, voce pode pegar emprestimo.".format(nome))
else:
	print("{}, voce nao pode pegar emprestimo.".format(nome))
	