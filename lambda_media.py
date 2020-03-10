media = lambda x, y: (x + y)/2
try:
    numero1 = int(input("Digite o numero 1: "))
    numero2 = int(input("Digite o numero 1: "))
    result = media(numero1, numero2)

    msg = ""
    if result < 5:
        msg = "Aluno Reprovado."
    elif result < 6:
        msg = "Aluno Em Recuperacao."
    else:
        msg = "Aluno Aprovado."
    print("{} Media dos numeros is {}.".format(msg, result))

except ValueError:
    print("Digite um numero inteiro.")
