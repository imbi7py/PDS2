from datetime import date

nome = input("Digite seu nome: ")

try:
	idade = int(input("Digite sua idade: "))
	altura = int(input("Digite sua altura em cm: "))
	peso = int(input("Digite seu peso: "))

	altura = altura / 100
	imc = peso / (altura * altura)
	data_nasc = date.today().year - idade - 1;

	print(f"O {nome} tem {peso} quilos, mede {altura} metros, o IMC={imc: .2f} e a data de nascimento e {data_nasc}.")

except:
	print("Failed when using numbers")
