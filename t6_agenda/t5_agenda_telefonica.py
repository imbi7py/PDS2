import os
import Contatos
# import contato

'''
	Function - header
	Arguments:
		none
	Returns:
		none
	Description: prints characters creating a header saying the name of the app
	Usage: use after cleaning the prompt for a better user experience
'''
def header(word="Agenda de Contatos"):
	print("="*15)
	print(word)
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
	options = {1: "Adicionar Contato", 2: "Listar Contatos",
            3: "Deletar Contato", 0: "Sair"}

	header()

	for option in options:
		print("{}: {} ".format(option, options[option]))

'''
	Function - addContato
	Arguments:
	Returns:
		object contato
	Description: returns a list with all the contacts
	Usage: use to add a new contact
'''
def addContato():
	header("Adicionar contato")
	nome = ""
	tipo = ""
	numero = 1
	try:
		nome = input("Digite o nome do contato: ")
		mycontato = Contatos.contato.contato(nome)
		while numero != 0:
			numero = int(input("Digite o numero do contato com DDD: + "))
			if numero == 0:
				break
			tipo = input("Digite o tipo de contato: ")
			mycontato.addTelefone(numero, tipo)
		return mycontato
	except ValueError:
		print("Apenas numeros inteiros sao validos no numero.")

'''
	Function - listarContatos
	Arguments:
		contatos: array de contatos
	Returns:
		none
	Description: shows list of contacts
	Usage: use to list contacts
'''
def listarContatos(contatos):
	header("Listar contatos")
	contatos.listContatos()


'''
	Function - deleteContato
	Arguments:
		contatos: array de contatos
	Returns:
		none
	Description: deletes a contact from list
	Usage: use to delete a contact from list
'''
def deleteContato(contatos):
	header("Deletar contato")
	contatos.listContatos()
	if contatos.getLen() == 0:
		return contatos

	nome = ""
	try:
		nome = input("Digite o nome de contato para deletar: ")
		for contato in contatos.getList():
			if nome == contato.getName():
				contatos.delContato(contato)
				break;
	except ValueError:
		print("Insira um contato valido.")


def main():
	contatos = Contatos.Contatos();
	while(True):
		menu()
		opcao = 0
		try:
			opcao = int(input("Digite o opcao no gerenciador de contatos: "))
		except ValueError:
			print("Apenas as opcoes listadas sao validas.")
		if (opcao == 1):
			contatos.addContato(addContato())
		elif opcao == 2:
			listarContatos(contatos)
		elif opcao == 3:
			deleteContato(contatos)
		elif opcao == 0:
			print("Saindo...")
			exit(0)
		else:
			print("Opcao invalida.")


main()

