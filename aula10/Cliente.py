from Pessoa import Pessoa 

class Cliente(Pessoa):
	def __init__(self, nome, idade, conta):
		super().__init__(nome, idade);
		self._conta = conta

	@property
	def conta(self):
		return self._conta

	def completeDetails(self):
		print("Nome: {}".format(super().nome()))
		print("Idade: {}".format(super().idade()))
		self.conta.detalhes()
