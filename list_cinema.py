Salas = [10, 2, 1, 3, 0]

sala_escolhida = -1
while sala_escolhida != 0:
	salas = ""
	print("Salas disponiveis: {}".format(len(Salas)))
	try:
		sala_escolhida = int(input("Digite a sala escolhida: "))
		if (sala_escolhida > len(Salas) or sala_escolhida < 0):
			print("Sala escolhida é invalida.")
		elif sala_escolhida != 0:
			print("Cadeiras disponiveis: {}".format(Salas[sala_escolhida-1]))
			numero_cadeiras = int(input("Digite a quantidade de cadeiras escolhida: "))

			if numero_cadeiras > Salas[sala_escolhida-1]:
				print("Numero de cadeiras superior as disponiveis.")
			elif numero_cadeiras <= 0:
				print("Valor nulo ou negativo.")
			else:
				Salas[sala_escolhida - 1] -= numero_cadeiras
				print("Cadeiras escolhidas")

	except ValueError:
		print("Voce digitou uma entrada invalida. Voce so deve digitar numeros inteiros.")

print("Voce saiu do sistema")