import telefone

class Telefones():
	def __init__(self):
		self.telefones = []
	
	def addTelefone(self, telef, tipo):
		self.telefones.append(telefone.telefone(telef, tipo))

	def getTelefones(self):
		tels = ""
		if (len(self.telefones) == 0):
			return tels
		for n in self.telefones:
			tels += n.getNumber + ","
		return tels