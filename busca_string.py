username = input("Digite seu usuario: ")
password = input("Digite sua senha: ")

if "ricardo.vargas" in username and ".MyP4ssw0rd!" in password:
	print("{} you logged in.".format(username))
elif "ricardo.vargas" not in username:
	print("{} is an invalid username".format(username))
else:
	print("Invalid password")