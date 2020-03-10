import os

vendas = {}
compras = {}

def header(word="Gerenciador de Veiculos"):
    print("="*15)
    print(word)
    print("="*15)

def menu():
    # list with all the options from the menu
    options = { 1: "Comprar Veiculos", 2: "Listar Veiculos", 3: "Atualizar Veiculos", 4: "Vender Veiculos", 5: "Listar Compras", 6: "Listar Vendas", 0: "Sair"}
    header()
    for option in options:
        print("{}: {} ".format(option, options[option]))

def addVeiculo(veiculos):
    header("Comprar Veiculo")
    try:
        nome = input("Digite o nome do Veiculo: ")
        qtd = int(input("Digite a quantidade de Veiculos: "))
        ano = int(input("Digite o ano do Veiculo: "))
        preco = float(input("Digite o preco do Veiculo: "))
        if qtd <= 0 or ano <= 0 or preco <= 0:
            print("Valor invalida")
        if nome in veiculos:
            quant = veiculos[nome][0] - qtd
            veiculos[nome] = [ quant, ano, preco]
            quant = compras[nome][0] + qtd
            compras[nome] = [ qtd, ano, preco]
        else:
            veiculos[nome] = [ qtd, ano, preco]
            compras[nome] = [ qtd, ano, preco]

    except ValueError:
        print("Apenas numeros inteiros sao validos no numero.")
    print("Veiculo Adicionado")
    return veiculos

def listVeiculo(veiculos, title="Listar Veiculo"):
    header(title)
    if len(veiculos) == 0 and title == "Listar Veiculo":
        print("Nenhum Veiculo previamente adicionado")
    for key in veiculos:
        msg = " "
        for el in veiculos[key]:
            msg += "{}, ".format(el)
        print("{}: {}".format(key, msg[:-2]))

def atualizarVeiculo(veiculos):
    listVeiculo(veiculos)
    header("Atualizar Veiculo")
    if len(veiculos) == 0:
        print("Nenhum Veiculo previamente adicionado")
        return veiculos

    try:
        nome = input("Digite o nome de Veiculo para atualizar: ")
        if nome in veiculos:
            qtd = int(input("Digite a quantidade de Veiculos: "))
            ano = int(input("Digite o ano do Veiculo: "))
            preco = float(input("Digite o preco do Veiculo: "))
            veiculos[nome] = [ qtd, ano, preco]
            return veiculos
        else:
            print("Veiculo nao existe.")
            return veiculos

    except ValueError:
        print("Insira um valor valido.")
    return veiculos

def deleteVeiculo(veiculos):
    listVeiculo(veiculos)
    header("Vender Veiculo")
    if len(veiculos) == 0:
        print("Nenhum Veiculo previamente adicionado")
        return veiculos
    try:
        nome = input("Digite o nome de Veiculo para vender: ")
        if nome in veiculos:
            qtd = int(input("Digite a quantidade a vender: "))
            if qtd <= 0:
                print("Quantidade invalida")
            elif qtd > veiculos[nome][0]:
                print("Quantidade superior a em estoque")
                return veiculos
            if nome in vendas.keys():
                print("Had")
                vendas[nome][0] = vendas[nome][0] + qtd
            else:
                print("didn Have")
                vendas[nome] = veiculos[nome]
                vendas[nome][0] = qtd
            veiculos[nome][0] = veiculos[nome][0] - qtd
            print("Veiculo Vendido")

        else:
            print("Veiculo nao existe.")
    except ValueError:
        print("Insira um Veiculo valido")
    return veiculos

def main():
    veiculos= {
        "gol": [20, 2019, 28.900],
        "onix": [30, 2019, 27.800],
        "sandeiro": [22, 2016, 15.700],
        "hb20": [3, 2020, 38.500],
        "siena": [4, 2016, 18.200],
        "prima": [17, 2015, 14.300],
        "voyage": [20, 2020, 38.100],
        "uno": [12, 2019, 28.400]
    }
    aux_veiculos = {}

    while(True):
        menu()
        opcao = 0
        try:
            opcao = int(input("Digite o opcao no gerenciador de veiculos: "))
        except ValueError:
            print("Apenas as opcoes listadas sao validas.")
        if(opcao == 1):
            veiculos = addVeiculo(veiculos)
        elif opcao == 2:
            listVeiculo(veiculos)
        elif opcao == 3:
            veiculos = atualizarVeiculo(veiculos)
        elif opcao == 4:
            veiculos = deleteVeiculo(veiculos)
            
        elif opcao == 5:
            listVeiculo(compras, "Compras")
        elif opcao == 6:
            listVeiculo(vendas, "Vendas")
        elif opcao == 0:
            print("Saindo...")
            exit(0)
        else:
            print("Opcao invalida.")

main()