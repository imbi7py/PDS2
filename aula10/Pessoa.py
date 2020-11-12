class Pessoa:
	def __init__(self, nome, idade):
		self._nome = nome
		self._idade = idade

	#@property
	def nome(self):
		return self._nome

	#@property
	def idade(self):
		return self._idade

	# # @nome.setter
	# def setnome(self, nome):
	# 	if not isinstance(nome, (str)):
	# 		raise ValueError("Nome precisa ser str")
	# 	self._nome = nome

	# # @idade.setter
	# def setidade(self, idade):
	# 	if not isinstance(idade, (int)):
	# 		raise ValueError("Idade precisa ser int")
	# 	self._idade = idade
