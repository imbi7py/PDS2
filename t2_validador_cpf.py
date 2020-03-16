import os
import time
import re
from random import randint

'''
	Function - header
	Arguments:
		none
	Returns:
		none
	Description: prints characters creating a header saying the name of the app
	Usage: use after cleaning the prompt for a better user experience
'''
def header(word="CPF App"):
	print("="*15)
	print(" {}".format(word))
	print("="*15)

'''
	Function - menu
	Arguments:
		word: 
	Returns:
		none
	Description: prints the menu and its options
	Usage: use to show the menu
'''
def menu():
	# list with all the options from the menu
	options = ["Validar CPF", "Gerar CPF"] # + Sair
	header("Menu")
	for index, option in enumerate(options):
		print("{}: {} ".format(index + 1 , option))
	print("{}: {} ".format(0 , "Sair"))

'''
	Function - verificaDigito
	Arguments:
		cpf: CPF typed from user to be validated
		digit: 1 or 2 for validating CPF.
	Returns:
		True: when CPF is valid
		False: when CPF is invalid
	Description: returns true when CPF is valid. Latest 2 numbers validate it.
	Usage: latest 2 numbers from CPF defines if is valid or not. Use 1 or 2 to validate the CPF
'''
def verificaDigito(cpf, digit):
	result_multiplication = 0
	cpf_range = 8 + digit
	multiplicator = cpf_range + 1

	for i in range(cpf_range):
		result_multiplication += int(cpf[i]) * multiplicator
		multiplicator -= 1

	result = (result_multiplication * 10) % 11
	if result == 10:
		result = 0

	if str(result) == cpf[cpf_range]:
		return True
	else:
		return False

'''
	Function - validateCPF
	Arguments:
		none
	Returns:
		none
	Description: asks CPF for user and shows if is valid or not
	Usage: use to ask a CPF for a user and validate it
'''
def validateCPF():
	msg_failure = "CPF Invalido."
	msg_success = "CPF Valido."
	try:
		cpf = input("Digite o CPF (xxx.xxx.xxx-xx): ")
		# regexp to accept just the CPF format (also checks if contains 11 numbers)
		if re.match("^\d{3}\.\d{3}\.\d{3}\-\d{2}$", cpf) == None:
			print(msg_failure)
			return;
		# maintain just the numbers
		cpf = re.sub("[^0-9]", '', cpf)
		if verificaDigito(cpf, 1) == False or verificaDigito(cpf, 2) == False:
			print(msg_failure)
		else:
			print(msg_success)

	except ValueError:
		print("Digite apenas valores validos.")

'''
	Function - generateCPF
	Arguments:
		none
	Returns:
		none
	Description: generates random CPF and changes the latest 2 numbers until CPF gets valid
	Usage: use for generate a valid CPF
'''
def generateCPF():
	# função que gera em formato de lista todos os 11 digitos de um CPF válido em ordem
	cpf = []
	cpf_length = 11
	result = True

	for i in range(cpf_length):
		value = randint(0, 9)
		cpf.append(str(value))

	i = 0
	cpf_str = "".join(cpf)
	while (verificaDigito(cpf_str, 1) == False):
		cpf[-2] = str(i)
		cpf_str = "".join(cpf)
		i += 1
		if i > 10:
			result = False
			break

	i = 0
	cpf_str = ''.join(cpf)
	while (verificaDigito(cpf_str, 2) == False):
		cpf[-1] = str(i)
		cpf_str = "".join(cpf)
		i += 1
		if i > 10:
			result = False
			break;
	
	msg = "{}.{}.{}-{}".format(cpf_str[:3], cpf_str[3:6], cpf_str[6:9], cpf_str[9:11])
	if result == True:
		print("Gerou CPF: {}".format(msg))
	else:
		# Should not come here.
		print("Falhou para gerar o CPF: {}".format(msg))

'''
	Function - startsApp
	Arguments:
		none
	Returns:
		none
	Description: manages the app and the options
	Usage: use to control the game
'''
def startsApp():
	while (True):
		# clears prompt
		os.system('clear')
		# shows the available options in the menu
		menu();
		option = -1;
		try:
			option = int(input("Digite uma opcao selecionada: "))
			if option < 0 or option > 2:
				print("Opcao invalida.")
			elif option == 1:
				validateCPF()
			elif option == 2:
				generateCPF();
			else:
				print("Saindo...")
				exit(0)
		except ValueError:
			print("Digite um valor inteiro.")
		# better than a sleep hehe
		wait_line = input("Tecle enter para atualizar pagina...")

'''
	Function - main
	Arguments:
		none
	Returns:
		none
	Description: main function
	Usage: use for starting the App
'''
def main():
	# starts app for generating or validatin cpf
	startsApp()

# calls main function
main()
