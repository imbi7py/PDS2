from Cliente import Cliente

class Banco:
	def __init__(self):
		self._clientes = []

	#@property
	def clientes(self):
		return self._clientes

	# @clientes.setter
	def addCliente(self, cliente):
		if not isinstance(cliente, (Cliente)):
			raise ValueError("Cliente precisa ser do tipo Cliente")
		self._clientes.append(cliente)

	def autenticacao(self, agencia, conta, nameCliente):
		if not isinstance(agencia, (int)):
			raise ValueError("Agencia precisa ser do tipo int")
			return None
		if not isinstance(conta, (int)):
			raise ValueError("Conta precisa ser do tipo int")
			return None
		if not isinstance(nameCliente, (str)):
			raise ValueError("Cliente precisa ser do tipo str")
			return None
		for cliente in self.clientes():
			print(cliente.conta.agencia())
			print(cliente.conta.conta())
			print(cliente.nome())
			if (cliente.conta.agencia() != agencia or cliente.conta.conta() != conta or cliente.nome() != nameCliente):
				print("Autenticacao Falhou. Dados fornecidos nao correspondem a nenhuma conta")
			else:
				print("Autenticacao bem sucedida")
				return cliente
		return None
