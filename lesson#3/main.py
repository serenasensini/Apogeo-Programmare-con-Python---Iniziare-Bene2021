# esercizio cicli
countdown = 10
# while countdown >= 0:
#     print(countdown)
#     countdown = countdown - 1

# ciclo for
# for number in range(0, 10):
#     print(number)

# per ogni numero presente tra 0,10:
# stampa il numero
# for number in range(countdown, -1, -1):
#     print(number)

# liste

# fruit_list = ['apple', 'pear', "grapes"]
# print(fruit_list[0]) # primo elemento
# print(fruit_list[1]) # secondo element
# print(fruit_list[5])
# print(fruit_list[-2])
# print(fruit_list[-5])

# gira_stringa = "i topi non avevano nipoti"


# gira_stringa_list = ["i", "t", "o"...]

# length = len(gira_stringa)
# print(length)
# reverse_stringa = ""

# for cursore in range(length-1, -1, -1):
#     reverse_stringa = reverse_stringa + gira_stringa[cursore]

# print(reverse_stringa)

# print(gira_stringa[::-1])

testo = "i topi non avevano nipoti"
# stampa tutti i caratteri della stringa
# for carattere in testo:
#     print(carattere)

# slicing notation
testo = "Lorem ipsum dolor sit amet"
# print(testo[5:])

# funzioni
# def somma(x, y):
#     return x + y


# num = somma(3, 5)
# print(num)

# def countdown(start):
    # per ogni numero inferiore al countdown
    # per ogni numero presente nell'insieme tra il countdown e 0
    # for numero in range(start, -1, -1):
    #     print(numero)

# countdown(9)

def somma_parametri_variabili(*lista_parametri):
    somma = 0
    for elemento in lista_parametri:
        somma = somma + elemento
    return somma

# lista_numeri = [1,2,3,4,5,6,9,10]
# per ogni numero nella lista, somma il primo, il secondo...
# per ogni numero nella lista, somma l'elemento in posizione 0, 1,...
# somma = 0
# for elemento in lista_numeri:
#     somma = somma + elemento
#
# print(somma)

# result = somma_parametri_variabili(2,3,4,10,54854)
# print(result)
#
# def concatena(*args):
#     result = ""
#     for stringa in args:
#         result = result + stringa
#     return result
#

# testo = concatena("world ", "hello")
# print(testo)
#
# def somma_kwargs(**kwargs):
#     somma = 0
#     print(kwargs.items())
#     for key, value in kwargs.items():
#         print("Sto sommando il numero ", key)
#         print("Il valore è: ", value)
#         somma = somma + value
#
#
# somma_kwargs(num1=10, num2=5, num3=10)
#
# def frazione(**kwargs):
#     denominatore = kwargs["den"]
#     numeratore = kwargs["num"]
#     return numeratore/denominatore
#
# print(frazione(den=5, num=10))
#
# print("hello", "world", "!")

