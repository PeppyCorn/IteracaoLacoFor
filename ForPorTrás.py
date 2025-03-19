texto = 'Pedro Costa' # iterável
iterador = texto.__iter__() # iterador

while True:
    try:
        letra = iterador.__next__() # vai para o próximo valor da iteracao
        print(letra)
    except StopIteration:
        break

# Se passar da quantidade de next vai dar problemas de iteracao como StopIteration