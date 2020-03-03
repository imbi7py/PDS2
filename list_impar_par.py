L_total = [9, 5, 6, 4, 8, 12, 11, 15, 0, 1, 3, 2]
L_par = []
L_impar = []

for number in L_total:
	if (number % 2) == 0:
		L_par.append(number)
	else:
		L_impar.append(number)
		
		
print("Lista impar: {}".format(L_impar))
print("Lista par: {}".format(L_par))