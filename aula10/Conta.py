from abc import ABC

class Conta:
	def __init__(self, agencia, conta, saldo=0):
		self._agencia = agencia
		self._conta = conta
		self._saldo = saldo

	# @property
	def agencia(self):
		return self._agencia

	# @property
	def conta(self):
		return self._conta

	# @property
	def saldo(self):
		return self._saldo

	def depositar(self, valor):
		if not isinstance(valor, (int, float)):
			raise ValueError("Valor do depósito precisa ser numérico")
		self.saldo += valor
		self.detalhes()

	def detalhes(self):
		print(f'Agência: {self.agencia()}', end=' ')
		print(f'Conta: {self.conta()}', end=' ')
		print(f'Saldo: {self.saldo()}')

	#@abstractmethod
	def sacar(self, valor):
		pass
