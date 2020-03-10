import os

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
	print("")
	print("="*15)

'''
	Function - menu
	Arguments:
		none
	Returns:
		none
	Description: prints the menu and its options
	Usage: use to show the menu
'''
def menu():
    # list with all the options from the menu
    options = ["Validar CPF", "Gerar CPF", "Sair"]
	header("Menu")

	for index, option in options:
	    print("{}: {} ".format(index, option))

def validarCPF():
    try:
        cpf = int(input("Digite apenas os numeros do CPF"))

    except:
        print("Digite apenas numeros")

def gerarCPF():
    print("Gerou")


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
                print("Opcao invalid")
            elif option == 1:
                validarCPF()
            else:
                gerarCPF();
        except ValueError:
            print("Digite um valor inteiro")

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
