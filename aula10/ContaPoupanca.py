from Conta import Conta
	
class ContaPoupanca(Conta):
 
	def agencia(self):
		return super().agencia()

	def conta(self):
		return super().conta()

	def saldo(self):
		return super().saldo()

	def detalhes(self):
		super().detalhes()

	def sacar(self, valor):
		if self.saldo < valor:
			print('Saldo insuficiente')
			return
		self.saldo -= valor
		self.detalhes()

