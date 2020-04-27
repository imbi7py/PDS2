from Cliente import Cliente
from Conta import Conta
from os import system
import random

'''
	Function - handleAlerts
	Arguments:
		none
	Returns:
		none
	Description: uses input to not give a directly clear in the showed message
	Usage: use to user see the messages before going to system clear
'''
def handleAlerts():
	try:
		next = input("Pressione Enter para continuar... ")
	except ValueError:
		print("Sequencia de Teclas invalida.")

'''
	Function - header
	Arguments:
		none
	Returns:
		none
	Description: prints characters creating a header saying the name of the app
	Usage: use after cleaning the prompt for a better user experience
'''
def header(word="Banco de PDS"):
	system("clear")
	print("="*20)
	print(word)
	print("="*20)

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
	options = {1: "Adicionar Conta", 2: "Selecionar Conta", 0: "Sair"}
	header()
	for option in options:
		print("{}: {} ".format(option, options[option]))

'''
	Function - submenu
	Arguments:
		word:
	Returns:
		none
	Description: prints the submenu from an account and the user actions
	Usage: use to show the action for a user account
'''
def submenu():
	# list with all the options from the menu
	options = {1: "Ver Saldo", 2: "Fazer Deposito",
			3: "Fazer Saque", 4: "Ver Titulares", 5: "Ver Detalhes", 0: "Sair"}

	header()
	for option in options:
		print("{}: {} ".format(option, options[option]))

'''
	Function - addAccount
	Arguments:
	Returns:
		object Conta
	Description: returns None or created account
	Usage: use to add a new bank account
'''
def addAccount():
	header("Adicionando Nova Conta")
	owners = []
	numOwner = 1
	try:
		numOwner = int(input("Digite a quantidade de titulares desejados: "))
	except ValueError:
		print("Apenas numeros inteiros sao validos no numero de titulares.")
		return

	for i in range(1, numOwner+1):
		try:
			entireName = input("Nome Completo do Titular {}: ".format(i))
			name = input("Nome que o Titular deseja ser chamado: ")
			cpf = int(input("CPF (somente digitos): "))
			cellNumber = int(input("Telefone Principal com DDD (somente digitos): +"))
			
			if entireName.isalpha() == False or name.isalpha() == False:
				raise ValueError
			client = Cliente(cpf, name, entireName, cellNumber, i)
			owners.append(client)
		except ValueError:
			print("Valores inseridos invalidos. Insira valores validos nos campos.")
			break

	listLength = len(owners)
	if (listLength != numOwner or listLength == 0):
		return

	credEspecial = ""
	try:
		credEspecial = input("Deseja utilizar credito especial na conta? (S) sim ou (N) nao: ")
	except ValueError:
		print("Apenas valores validos nos campos.")

	if (credEspecial == "S" or credEspecial == "N"):
		idLista = random.sample(range(100), 10)
		id = int("".join(str(x) for x in idLista))
		print("ID gerado para Conta: {}".format(id))
		conta = Conta(id, credEspecial, owners)
		return conta
	else:
		print("Opção inválida para o credito especial")
	return

'''
	Function - listAccounts
	Arguments:
		list of accounts
	Returns:
		none
	Description: prints all accounts
	Usage: use to list all bank account
'''
def listAccounts(contas):
	if len(contas) == 0:
		print("Nao existem contas previamente adicionadas")
		return
	for i in contas:
		i.showAccountSimpleDetails()
		print("*"*20)

'''
	Function - gerenciar_conta
	Arguments:
		contas: list of accounts
	Returns:
		none
	Description: selects and them goes to manage an account
	Usage: use to select an account and them managers a account
'''
def manageAccount(conta):
	while (True):
		submenu()
		opcao = 0
		try:
			opcao = int(input("Selecione uma opção da Conta: "))
		except ValueError:
			print("Sequencia de Teclas invalida. Somente os numeros das opçoes sao validos.")
			handleAlerts()
			continue

		if opcao == 1:
			conta.do_saldo()
		elif opcao == 2:
			try:
				value = float(input("Digite o valor do depositado: "))
				conta.do_deposito(value)
			except ValueError:
				print("Valor invalido. Apenas numeros positivos sao aceitos")
		elif opcao == 3:
			try:
				value = float(input("Digite o valor do sacado: "))
				conta.do_saque(value)
			except ValueError:
				print("Valor invalido. Apenas numeros positivos sao aceitos")
		elif opcao == 4:
			conta.showOwners()
		elif opcao == 5:
			conta.showAccountDetails()
		elif opcao == 0:
			print("Saindo da conta...")
			break;
		else:
			print("Opcao inexistente. Somente os numeros das opções sao validos.")
		handleAlerts()

'''
	Function - selectAccount
	Arguments:
		contas: list of accounts
	Returns:
		none
	Description: selects and them goes to manage an account
	Usage: use to select an account and them managers a account
'''
def selectAccount(contas):
	header("Selecionando Conta")
	listAccounts(contas)
	if len(contas) == 0:
		return

	conta = None
	opcao = 0
	try:
		opcao = int(input("Selecione o ID da conta que deseja gerenciar: "))
		for i in contas:
			if opcao == i.id:
				print("FOUND: {}".format(i.id))
				conta = i
				break

	except ValueError:
		print("Sequencia de Teclas invalida. Somente os ID listados sao validos.")

	if conta != None:
		manageAccount(conta)
	else:
		print("Conta nao foi selicionada.")

def main():
	contas = []
	while(True):
		menu()
		opcao = -1
		try:
			opcao = int(input("Digite o opcao no caixa: "))
		except ValueError:
			print("Sequenciade Teclas invalida. Somente os numeros das opçoes sao validos.")
			handleAlerts()
			continue

		if (opcao == 1):
			conta = addAccount()
			if conta in contas:
				print("Conta ja existia. Nao vamos recria-la")
			elif conta == None:
				print("Dados para conta corrompidos. Tente novamente se necessário.")
			else:
				contas.append(conta)
				print("Conta adicionada com Sucesso!")
		elif opcao == 2:
			selectAccount(contas)
		elif opcao == 0:
			print("Saindo...")
			exit(0)
		else:
			print("Opcao inexistente. Somente os numeros das opções sao validos.")
		handleAlerts()

main()
