class Cliente:
	def __init__(self, cpf, nome, nomeCompleto, telefone, numOnwer):
		self.cpf = cpf
		self.nome = nome
		self.nomeCompleto = nomeCompleto
		self.telefone = telefone
		self.numOnwer = numOnwer

	def showOwner(self):
		print("Titular {}: {} - {}".format(self.numOnwer, self.nome, self.cpf))

	def showOwnerDetails(self):
		self.showOwner()
		print("Nome Completo: {}".format(self.numOnwer))
		print("CPF: {}".format(self.cpf))
		print("Telefone: {}".format(self.telefone))
