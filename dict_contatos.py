import os

def header(word="Gerenciador de Contatos"):
	print("="*15)
	print(word)
	print("="*15)

def menu():
    # list with all the options from the menu
    options = { 1: "Adicionar Contato", 2: "Listar Contatos", 3: "Atualizar Contato", 4: "Deletar Contato", 0: "Sair"}

    header()

    for option in options:
        print("{}: {} ".format(option, options[option]))

def addContato(contatos):
    header("Adicionar contato")
    nome = ""
    numero = 0
    try:
        nome = input("Digite o nome do contato: ")
        numero = int(input("Digite o numero do contato com DDD: +"))
    except ValueError:
        print("Apenas numeros inteiros sao validos no numero.")
    
    contatos[nome] = numero
    print("Contato Adicionado")
    return contatos

def listContatos(contatos):
    header("Listar contatos")
    if len(contatos) == 0:
        print("Nenhum contato previamente adicionado")

    for key in contatos:
        print("{}: {}".format(key, contatos[key]))
    print("Contatos Listados")

def atualizarContatos(contatos):
    listContatos(contatos)
    header("Atualizar Contato")
    if len(contatos) == 0:
        print("Nenhum contato previamente adicionado")
        return contatos

    try:
        nome = input("Digite o nome de contato para atualizar: +")
        if nome in contatos.keys():
            numero = int(input("Digite o numero de contato para atualizar: "))
            contatos[nome] = numero
            print("Contato Atualizado")
            return contatos
        else:
            print("Contato nao existe.")
            return contatos

    except ValueError:
        print("Insira um valor valido")

    return contatos

def deleteContatos(contatos):
    listContatos(contatos)
    header("Deletar contato")
    nome = ""
    if len(contatos) == 0:
        print("Nenhum contato previamente adicionado")
        return contatos

    try:
        nome = input("Digite o nome de contato para deletar: ")
    except ValueError:
        print("Insira um contato valido")
    if nome in contatos.keys():
        del contatos[nome]
        print("Contato Deletado")
    else:
        print("Contato nao existe.")
    return contatos

def main():
    contatos= {}

    while(True):
        menu()
        opcao = 0
        try:
            opcao = int(input("Digite o opcao no gerenciador de contatos: "))
        except ValueError:
            print("Apenas as opcoes listadas sao validas.")
        if(opcao == 1):
            contatos = addContato(contatos)
        elif opcao == 2:
            listContatos(contatos)
        elif opcao == 3:
            contatos = atualizarContatos(contatos)
        elif opcao == 4:
            contatos = deleteContatos(contatos)
        elif opcao == 0:
            print("Saindo...")
            exit(0)
        else:
            print("Opcao invalida.")

main()