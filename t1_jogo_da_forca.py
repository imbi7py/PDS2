import os

'''
	Function - fimGame
	Arguments:
		situation: true for winning the game and false for gameover
	Returns:
		none
	Description: prints the result of the game
	Usage: use when the game is finished
'''
def fimGame(situation):
	if situation:
		print("Jogo Terminou! Voce Ganhou")
	else:
		print("Jogo Terminou! Voce Perdeu")

'''
	Function - header
	Arguments:
		none
	Returns:
		none
	Description: prints characters creating a header saying the name of the game
	Usage: use after cleaning the prompt for a better user experience
'''
def header():
	print("="*15)
	print(" Jogo da Forca")
	print("="*15)

'''
	Function - showChutes
	Arguments:
		letrasChutadas: array containing the letters that the user tried
	Returns:
		none
	Description: prints the letters the use tried
	Usage: use after the user try a letter
'''
def showChutes(letrasChutadas):
	print("Letras Chutadas: {}".format(", ".join(letrasChutadas)))

'''
	Function - showChances
	Arguments:
		chances: quantity of tries the user still has
	Returns:
		none
	Description: shows the quantity of tries the user still has
	Usage: use to show the user remaining tries
'''
def showChances(chances):
	print("Chances: {}".format(chances))

'''
	Function - showDiscovered
	Arguments:
		letrasChutadas: array containing the letters that the user tried
		word: word for being discovered
	Returns:
		discovered: discovered word
	Description: prints the letter discovered from the user in the word
	Usage: use to show the letters discovered
'''
def showDiscovered(letrasChutadas, word):
	discovered = ""
	for letra in word:
		# if word contains the letra chutada, shows the letter
		if letra in letrasChutadas:
			discovered += " {} ".format(letra)
		# if not the right letter, shows *
		else:
			discovered += " * "
	print("Forca: {} ".format(discovered))
	return discovered

'''
	Function - startGame
	Arguments:
		word: word for being discovered
	Returns:
		none
	Description: shows the game status and asks letter to continue the game
	Usage: use to control the game
'''
def startGame(word):
	chances = 5
	letrasChutadas = []
	resultGame = False

	while (True):
		os.system('clear')
		# next 4 functions to show game status
		header()
		showChutes(letrasChutadas)
		# shows the discovered word until now and returns to the variable
		discovered = showDiscovered(letrasChutadas, word)
		showChances(chances)
		# when the discovered word has no * it means you discovered all the word! You win the game
		if "*" not in discovered:
			resultGame = True
		# in the middle of the code to show the game status before finishing the game
		# game finishs when there's no chance anymore (gameover) or when the resultgame is true (win)
		if (chances == 0 or resultGame):
			break
		# letter from user trying
		letter = input("Digite uma letra: ")
		if letter in letrasChutadas:
			print("Voce ja colocou essa letra.")
		# must be a single letter if not is a word...
		elif len(letter) > 1:
			print("Voce so pode digitar letras, nada de palavras.")
		# just is a new letter tried when not tried before
		else:
			letrasChutadas.append(letter)
			# just lost a chance when letter is not in the word and the user didn't try the letter before
			if letter not in word:
				chances -= 1
	fimGame(resultGame)

'''
	Function - startGame
	Arguments:
		none
	Returns:
		none
	Description: asks the word for the game and starts the game
	Usage: use to create a new instance from the game
'''
def main():
	# clears prompt
	os.system('clear')
	# prints header from game
	header();
	# word to be discovered
	word = input("Insira a palavra para o jogo da forca: ")
	os.system('clear')
	# starts game control
	startGame(word)

# calls main function
main()
