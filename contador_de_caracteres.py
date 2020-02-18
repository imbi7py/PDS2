nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu sobrenome: ")

qtd = len(nome) + len(sobrenome)
print("Quantidade de caracteres em '{} {}': {} caracteres".format(nome, sobrenome, qtd))