string1 = input("Digite a String 1: ")
string2 = input("Digite a String 2: ")

position = string1.find(string2)
if position < 0:
	print("String {} not found in {}, position is {}.".format(string2, string1, position))
else:
	print("String {} found in {}, position is {}.".format(string2, string1, position))
