def saudacao(nome, sobrenome):
	print("Hi, {} {}!".format(nome, sobrenome))
	
def main():
	nome = input("Digite seu primeiro nome: ")
	sobrenome = input("Digite seu sobrenome: ")
	saudacao(nome, sobrenome)
	
main()