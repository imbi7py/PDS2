from Conta import Conta

class ContaCorrente(Conta):
	def __init__(self, agencia, conta, saldo=0, limite=100):
		super().__init__(agencia, conta, saldo)
		self._limite = limite

	@property
	def limite(self):
		return self._limite

	def agencia(self):
		return super().agencia()

	def conta(self):
		return super().conta()

	def saldo(self):
		return super().saldo()

	def detalhes(self):
		super().detalhes()

	def sacar(self, valor):
		# saldo is property in Conta and limite is from ContaCorrente
		if (self.saldo() + self.limite()) < valor:
			print('Saldo insuficiente')
			return
		super()._saldo -= valor
		self.detalhes()
