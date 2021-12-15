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

'''
Scrivere un programma per un gioco che permetta di indovinare un numero pescato casualmente dal computer tramite delle indicazioni basso-alto.
Il gioco ha le seguenti regole: il sistema estrae un numero compreso tra due valori a scelta (ad esempio, 0-100); all'utente viene richiesto di inserire
un numero qualsiasi per cercare di indovinare il numero pensato dal sistema; questo restituirà un messaggio che dice "Il numero è troppo alto"
se il numero inserito è maggiore del numero estratto, oppure "Il numero è troppo basso". Se il numero inserito è corretto, si stampa un messaggio
e il gioco termina.

Esempio di flusso:

1. Il sistema pesca 97.
2. L'utente inserisce in input 3.
3. Il sistema verifica che 3 è inferiore a 97, per cui stampa un messaggio adeguato.

Suggerimento: sfruttare il gioco della palla magica. 
'''

import sys
import random

# estrae un numero intero casuale tra 1 e 100
# num_random = random.randint(1, 100)
#
# user_input = int(input("Inserisci un numero tra 1 e 100: "))
#
# flag = False
#
# Tentativo n.1 azzeccato...
# if num_random == user_input:
#     print("Hai indovinato!")
#     flag = True
#     sys.exit()
#
# ... altrimenti continua a giocare
# while flag == False:
#     user_input = int(input("Inserisci un numero tra 1 e 100: "))
#
#     if user_input > num_random:
#         print("Il numero è troppo alto! Ritenta")
#     elif user_input < num_random:
#         print("Il numero è troppo basso! Ritenta")
#     else:
#         print("Hai indovinato!")
#         flag = True


## esercizio 18

'''
Scrivere una funzione divisibiliPerCinque che, dato il seguente array:
[10, 23, 45, 92, 70, 1020, 71]
stampi solo gli elementi divisibili per cinque.
'''

lista_numeri = [10, 23, 45, 92, 70, 1020, 71]


def divisibiliPerCinque(*lista_numeri):
    lista_divisibili = []

    for numero in lista_numeri:
        if numero % 5 == 0:
            lista_divisibili.append(numero)

    return lista_divisibili

divisibili = divisibiliPerCinque(10,16,5)

print("Stampa dei numeri divisibili", divisibili)