import Telefones

class contato:
	def __init__(self, nome):
		self.nome = nome
		self.telefones = []

	def addTelefone(self, telef, tipo):
		tel = Telefones.Telefones().addTelefone(telef, tipo)
		self.telefones.append(tel)

	def getName(self):
		return self.nome

	def getTelefones(self):
		numeros = []
		for n in self.telefones:
			print(n)
			numeros.append(n.getNumber)
		return numeros
