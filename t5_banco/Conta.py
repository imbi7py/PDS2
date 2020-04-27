class Conta:

	def __init__(self, id, credEspecial, onwers):
		self.id = id
		self.credEspecial = credEspecial
		self.onwers = onwers
		self.saldo = 0.0

	def getId(self):
		self.id

	def do_saque(self, value):
		if value <= 0:
			print("Valor de saque invalido.")
		else:
			if(self.credEspecial == "S" or self.saldo >= value):
				self.saldo -= value
				print("Saque realizado com sucesso.")
			elif(self.credEspecial == "N"):
				print("Saldo Insuficiente.")
		self.do_saldo()

	def do_deposito(self, value):
		if value <= 0:
			print("Valor de deposito invalido.")
		else:
			self.saldo += value
			print("Deposito realizado")
		self.do_saldo()

	def do_saldo(self):
		print("Saldo atual: R$ {}".format(round(self.saldo, 2)))

	def showIdAccount(self):
		print("ID da Conta: {}".format(self.id))

	def showOwners(self):
		for i in self.onwers:
			i.showOwner()

	def showAccountSimpleDetails(self):
		self.showIdAccount()
		self.showOwners()

	def showAccountDetails(self):
		self.showIdAccount()
		self.showOwners()
		self.do_saldo()
