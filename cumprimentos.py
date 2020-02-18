try:
	hora = int(input("Que horas sao: "))
	if hora < 0 or hora > 23:
		print("Invalid time.")
	elif hora < 12:
		print("Bom Dia.")
	elif hora < 17:
		print("Boa Tarde.)
	elif hora < 23:
		print("Boa Noite.")
except:
	print("Digite apenas numeros inteiros.")