# Lezione #3

## Soluzione n.1
Calcolare la somma dei primi 500 numeri naturali (da 0 a 500 escluso)

```
n = 0
for i in range(0,500):
    n += i
```

## Soluzione n.2
Data la stringa 'abcdefghi', scrivere
un programma che analizzi la stringa e
stampi a video:
Lettera 1: a
Lettera 2: b
...
E così via.

```
for i, letter in enumerate('abcdefghi'):
    print('Lettera %d: %s' % (i+1, letter)

```

## Soluzione n.3
Scrivere una funzione area_cerchio che, dato un raggio, calcola la sua area. Scrivere anche una funzione circonferenza, che calcola in maniera analoga il suo perimetro.

```
def area_cerchio(raggio):
    print(3.14*raggio**2)

def circonferenza(raggio):
    print(3.14*raggio*2)

area_cerchio(3)
circonferenza(4)
```

## Soluzione
Definire un programma che valuta i seguenti casi:
*Se il parametro passato è uguale a “piove”, allora viene restituita una stringa che dice “rimanda appuntamento”;
*Se il parametro invece è “sole”, allora viene restituita “puoi partecipare all'evento”;
*Se non avviene nessuno di questi casi, allora stampa “non ho capito”.

```
def whatIf(parametro):
    if(parametro == "piove"):
        print("Rimanda appuntamento")
    elif(parametro == "sole"):
        print("Puoi partecipare all'evento")
    else:
        print("Non ho capito")
        
whatIf("piove") #primo caso
whatIf("sole")  #secondo caso
whatIf("Testo di prova")    #terzo caso
```

## Soluzione  n.4
Completare il codice del gioco della palla magica presente nella cartella dei file per gli esercizi, usando le condizioni elif per quelle in eccesso: usare risposte del tipo
Meglio non dirlo ora.
Ne sei sicuro?
Direi proprio di sì.
La mia risposta è no.
Chiedimelo più tardi.
Dovresti rifletterci di più.
Ci puoi contare.
Le mie fonti dicono di sì.

```

#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 15 mar 2018

@author: Serena Sensini
'''

import sys
import random

ans = True

while ans:
    question = raw_input("Chiedi alla palla magica qualunque cosa. Per uscire, premi invio" +"\n")
    
    answers = random.randint(1,8)
    
    if question == "":
        sys.exit()
    
    elif answers == 1:
        print("Meglio non dirlo ora.")
    
    elif answers == 2:
        print("Ne sei sicuro?")
    
    elif answers == 3:
        print("Direi proprio di sì.")
    
    elif answers == 4:
        print("La mia risposta è no.")
    
    elif answers == 5:
        print("Chiedimelo più tardi.")
    
    elif answers == 6:
        print("Ci puoi contare.")
    
    elif answers == 7:
        print("Le mie fonti dicono di sì.")
    
    elif answers == 8:
        print("Dovresti rifletterci di più.")
```

## Soluzione  n.5
Scrivi un programma Python che stampi tutti i numeri da 0 a 6 tranne 3 e 6.
```
for x in range(6):
    if (x == 3 or x==6):
        continue
    print(x,end=' ')
print("\n")
```

## Soluzione n.6
Scrivi un programma Python per stampare il modello alfabetico 'P'.
```
result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or ((row == 0 or row == 3) and column > 0 and column < 5) or ((column == 5 or column == 1) and (row == 1 or row == 2))):  
            result_str=result_str+"*"    
        else:      
            result_str=result_str+" "    
    result_str=result_str+"\n"    
print(result_str);
```

## Soluzione n.7
Scrivi un programma che stampi il countdown, che dato come parametro di ingresso un numero, restituisce il countdown a partire da quel numero, fino a zero. Usare il ciclo for.

```
for element in range(number,0,-1):
    print element
```

## Soluzione n.9
Scrivi una funzione che prende due numeri come parametro e manda in print il più grande tra i due. Per quanto Python disponga di una funzione max(), sei invitato a utilizzare le istruzioni If, Elif ed Else per la scrittura dell'algoritmo.
```
def my_max(a, b):
    if a == b:
        print("I numeri sono identici")
    elif a > b:
        print("Il numero più grande tra i due è " + str(a))
    else:
        print("Il numero più grande tra i due è " + str(b))
```

## Soluzione n.10
Scrivi una funzione che prende stavolta tre numeri come parametro e restituisce il più grande tra loro!
```
def my_max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b:
        return c
```

## Soluzione n.11
Scrivi una funzione "sommatrice" che somma tra loro tutti gli elementi di una lista di numeri.
```
def sommatrice(lista):
    risultato = 0
    for numero in lista:
        risultato += numero
    print("Il risultato della somma è... " + str(risultato))
```

## Soluzione  n.12
Scrivi una funzione che, dato in ingresso un valore espresso in metri, mandi in print l'equivalente in miglia terrestri, iarde, piedi e pollici.
```
def americana(metri):
    conversions = dict()
    conversions["miglia"] = metri / 1609.344
    conversions["piedi"] = metri * 3.280840
    conversions["pollici"] = metri * 39.37008
    conversions["iarde"] = metri * 1.093613

    print(f"{metri} metri corrispondono a:")
    for key, value in conversions.items():
        print(f"{key}: {value}")
```

## Soluzione n.14

```
def equalTo(num, *args):
    counter = 0
    for element in args:
        if element == num:
            counter += 1
    return counter

print(equalTo(4,2,3,4,5,4,4,4))

```

# Soluzione n.15
Analoga al n.14.

# Soluzione n.16
Analoga al n.14.

# Soluzione n.17:
```
def reverse(str):
    for carattere in range(len(str)-1, -1, -1):
        print(str[carattere])

```

# Soluzione n.18

```
def divisibiliPerCinque(*args):
    for element in args:
        if element % 5 == 0:
            print(element)

print(divisibiliPerCinque(10, 23, 45, 92, 70, 1020, 71))
```

# Gioco!

```
import random

# estrae un numero intero casuale tra 1 e 100
guess = random.randint(1,100)

# STEP 1: chiedi all'utente di inserire una domanda per la palla magica
num = int(input("Inserisci un numero"))

# STEP 2: tramite le istruzioni condizionali, scrivi delle possibili risposte per l'utente

flag = True
while flag:
    num = int(input("Inserisci un numero: "))

    if num == guess:
        print("Hai indovinato!")
        flag = False
    elif num > guess:
        print("Il numero è troppo alto!")
    else:
        print("Il numero è troppo basso!")
```