from Cliente import Cliente
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca
from Banco import Banco
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
def header(word="Banco Aula 10"):
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
			3: "Fazer Saque", 4: "Ver Detalhes", 0: "Sair"}
	header("Menu da Conta")
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
def addCliente():
	header("Adicionando Novo Cliente")
	try:
		nome = input("Digite o nome do Cliente: ")
		if nome.isalpha() == False:
			raise ValueError("Nome precisa ser do tipo str")
			return None

		idade = int(input("Digite a Idade do Cliente: "))

		credEspecial = input("Deseja utilizar credito especial na conta? (S) sim ou (N) nao: ")
		conta = int(input("Digite o numero da Conta do Cliente: "))

		myConta = None
		if credEspecial == "S":
			# agencia = int(input("Digite o numero da Agencia: "))
			myConta = ContaCorrente(123, conta)
		elif credEspecial == "N":
			myConta = ContaPoupanca(123, conta)
		else:
			print("Opção inválida para o credito especial")
			return None
		print("Agencia: {}".format(myConta.agencia()))
		return Cliente(nome, idade, myConta)
	except ValueError:
		print("Valores inseridos invalidos. Insira valores validos nos campos.")
	return None

'''
	Function - gerenciar_conta
	Arguments:
		contas: list of accounts
	Returns:
		none
	Description: selects and them goes to manage an account
	Usage: use to select an account and them managers a account
'''
def manageAccount(cliente):
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
			print("Saldo: {}".format(cliente.conta.saldo()))
		elif opcao == 2:
			try:
				value = float(input("Digite o valor do depositado: "))
				cliente.conta.depositar(value)
			except ValueError:
				print("Valor invalido. Apenas numeros positivos sao aceitos")
		elif opcao == 3:
			try:
				value = float(input("Digite o valor do sacado: "))
				cliente.conta.sacar(value)
			except ValueError:
				print("Valor invalido. Apenas numeros positivos sao aceitos")
		elif opcao == 4:
			cliente.completeDetails()
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
def selectAccount(banco):
	header("Selecionando Conta")
	auth = None
	
	if len(banco.clientes()) == 0:
		print("Sem contas previamente adicionadas")
		return

	try:
		agencia = int(input("Digite o numero da agencia do Cliente: "))
		conta = int(input("Digite o numero da conta do Cliente: "))
		nameCliente = input("Digite o nome do Cliente: ")
		auth = banco.autenticacao(agencia, conta, nameCliente)
	except ValueError:
		print("Sequencia de Teclas invalida. Somente os ID listados sao validos.")

	if auth != None:
		manageAccount(auth)

def main():
	banco = Banco()

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
			cliente = addCliente()
			if cliente == None:
				print("Dados para conta corrompidos. Tente novamente se necessário.")
			else:
				banco.addCliente(cliente)
				print("Conta adicionada com Sucesso!")
		elif opcao == 2:
			selectAccount(banco)
		elif opcao == 0:
			print("Saindo...")
			exit(0)
		else:
			print("Opcao inexistente. Somente os numeros das opções sao validos.")
		handleAlerts()

main()
