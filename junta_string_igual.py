string1 = input("Digite a String 1: ")
string2 = input("Digite a String 2: ")
newstring = ""

for character in string1:
	if character in string2:
		newstring += character

print("Generated string from characters in string '{}' and string '{}' is '{}'.".format(string1, string2, newstring))
