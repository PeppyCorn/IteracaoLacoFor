texto = iter('Pedro Costa') # iterável (Pedro Costa) e Iterador (iter)

while True:
    try:
        print(next(texto)) # aqui mostra na tela e também vai para o próximo valor da iteracao
    except StopIteration:
        break

# Se passar da quantidade de next vai dar problemas de iteracao como StopIteration
