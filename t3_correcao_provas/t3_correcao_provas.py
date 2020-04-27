#! /usr/bin/env python3
import os
import csv

'''
	Function - header
	Arguments:
		none
	Returns:
		none
	Description: prints characters creating a header saying the name of the app
	Usage: use after cleaning the prompt for a better user experience
'''
def header(word="Corrigidor de Provas App"):
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
	options = ["Listar Alunos que Fizeram a Prova", "Gerar Relatorio Boletims", "Gerar Relatorio Detalhado"]
	header("Menu")
	for index, option in enumerate(options):
		print("{}: {} ".format(index + 1, option))
	print("{}: {} ".format(0, "Sair"))

'''
	Function - listaAlunosProva
	Arguments:
		file_prova: filename to read the gabarito
		file_respostas: filename to read answers from students
	Returns:
		none
	Description: shows a list o students from the test
	Usage: use to have  a list to know the students from the test
'''
def listStudentFromTest(file_prova, file_respostas):
	prova = getProva(file_prova)
	questoes = len(prova)

	line_count = 0
	with open(file_respostas) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')

		print("Alunos:")
		for aluno in sorted(csv_reader, key=lambda item: item[0].lower()):
			print("{}".format(aluno[0].lower()))
			line_count += 1
	print("Quantidade de alunos: {}".format(line_count))

'''
	Function - generateReport
	Arguments:
		file_prova: filename to read the gabarito
		file_respostas: filename to read answers from students
	Returns:
		none
	Description: shows the report from students test
	Usage: use to generate the report when the user selects the option
'''
def generateReport(file_prova, file_respostas):
	prova = getProva(file_prova)
	questoes = len(prova)

	line_count = 0
	with open(file_respostas) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')

		for aluno in sorted(csv_reader, key=lambda item: item[0].lower()):
			acertos = 0
			for questao in prova:
				if prova[questao][1] == aluno[questao + 1]:
					acertos += 1

			media = (acertos / questoes) * 10
			situacao = ""
			if media >= 6:
				situacao = "aprovado"
			else:
				situacao = "reprovado"
			print("Aluno '{}' acertou '{}' questoes. Media {} na qual considera-se {}. ".format(
				aluno[0].lower(), acertos, media, situacao))
			line_count += 1
	print("Quantidade de provas corrigidas: {}".format(line_count))

'''
	Function - generateReportEspecificado
	Arguments:
		file_prova: filename to read the gabarito
		file_respostas: filename to read answers from students
	Returns:
		none
	Description: shows the report with questions from students test
	Usage: use to generate the report when the user selects the option
'''
def generateReportEspecificado(file_prova, file_respostas):
	prova = getProva(file_prova)
	questoes = len(prova)

	line_count = 0
	with open(file_respostas) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')

		# print(sorted(csv_reader, key=lambda item: item[0].lower()))
		# print(csv_reader[0][0])
		for aluno in sorted(csv_reader, key=lambda item: item[0].lower()):
			acertos = 0
			name = aluno[0].lower()
			print("Aluno: {}".format(name))

			for questao in prova:
				print()
				print("Questao {}: {}".format(questao+1, prova[questao][0]))
				# for opcoes in prova[questao][:2]:
				# 	print("Opcao {}: {}".format(questao, prova[questao][opcoes]))
					
				print("Gabarito: {}".format(prova[questao][1]))

				print("Resposta: {}".format(aluno[questao + 1]))
				if prova[questao][1] == aluno[questao + 1]:
					print("Acertou")
					acertos += 1
				else:
					print("Errou")

			media = (acertos / questoes) * 10
			situacao = ""
			if media >= 6:
				situacao = "aprovado"
			else:
				situacao = "reprovado"

			print("Aluno '{}' acertou '{}' questoes. Media {} na qual considera-se {}. ".format(
				name, acertos, media, situacao))
			print("="*30)
			line_count += 1

	print("Quantidade de provas corrigidas: {}".format(line_count))

'''
	Function - getProva
	Arguments:
		file_gabarito: filename to read the test and its gabarito
	Returns:
		dictionary: dictionary containing the questions and answers from each question
	Description: opens gabarito file and gets its content
	Usage: use to get the test and compare with the student answer
'''
def getProva(file_prova):
	output = {}
	line_count = 0

	with open(file_prova) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')

		for index, row in enumerate(csv_reader):
			# print('Column names are {}'.format(", ".join(row)))
			output[index] = row
			line_count += 1
	return output

'''
	Function - startsApp
	Arguments:
		none
	Returns:
		none
	Description: manages the app and the options
	Usage: use to control the app
'''
def startsApp():
	file_prova = "prova.csv"
	file_respostas = "respostas.csv"

	while (True):
		# clears prompt
		os.system('clear')
		# shows the available options in the menu
		menu()
		option = -1
		try:
			option = int(input("Digite uma opcao selecionada: "))
			if option < 0 or option > 3:
				print("Opcao invalida.")
			elif option == 1:
				listStudentFromTest(file_prova, file_respostas)
			elif option == 2:
				generateReport(file_prova, file_respostas)
			elif option == 3:
				generateReportEspecificado(file_prova, file_respostas)
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
