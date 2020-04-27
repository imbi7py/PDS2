import contato

class Contatos:
	def __init__(self):
		self.contatos = []

	def addContato(self, contato):
		self.contatos.append(contato)

	def listContatos(self):
		if len(self.contatos) == 0:
			print("Nenhum contato previamente adicionado.")

		for contact in self.contatos:
			tel = contact.getTelefones()
			print("{}: {}".format(contact.getName(), ",".join(tel)))
		print("Contatos Listados")

	def delContato(self, contato):
		self.contatos.remove(contato)

	def getLen(self):
		return len(self.contatos)

	def getList(self):
		return self.contatos
