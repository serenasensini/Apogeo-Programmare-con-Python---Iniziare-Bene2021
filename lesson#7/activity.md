# Lezione #7

## Esercizio n.1

Correggere il seguente esercizio di modo che vengano gestiti eventuali parametri errati.

```
def area_cerchio(raggio):
    print(3.14**raggio**2)

def circonferenza(raggio):
    print(3.14*raggio*2)

area_cerchio(3)
circonferenza(4)
```

## Esercizio n.2

Correggere il seguente esercizio di modo che venga gestita la divisione per zero con un opportuno messaggio.

```
a = 5
b = 0
print(a/b)

```

## Esercizio n.3

Correggere il seguente esercizio di modo che vengano gestiti eventuali parametri errati.
```
import sys
import random

# estrae un numero intero casuale tra 1 e 100
# num_random = random.randint(1, 100)
#
# user_input = int(input("Inserisci un numero tra 1 e 100: "))
#
# flag = False

# Tentativo n.1 azzeccato...
# if num_random == user_input:
#     print("Hai indovinato!")
    # flag = True
    # sys.exit()

#... altrimenti continua a giocare
# while flag == False:
    # user_input = int(input("Inserisci un numero tra 1 e 100: "))
    #
    # if user_input > num_random:
    #     print("Il numero è troppo alto! Ritenta")
    # elif user_input < num_random:
    #     print("Il numero è troppo basso! Ritenta")
    # else:
    #     print("Hai indovinato!")
    #     flag = True


```

## Esercizio n.4

Ricordi il gioco alto-basso? Vediamone una versione leggermente diversa, con delle eccezioni custom:

```
class Errore(Exception):
    """Classe per tutti gli errori"""
    pass


class ValoreTroppoBasso(Error):
    pass


class ValoreTroppoAlto(Error):
    pass


# estrae un numero intero casuale tra 1 e 100
num_random = random.randint(1, 100)

user_input = int(input("Inserisci un numero tra 1 e 100: "))

flag = False

# Tentativo n.1 azzeccato...
if num_random == user_input:
    print("Hai indovinato!")
    flag = True
    sys.exit()

#... altrimenti continua a giocare
while flag == False:
    try:
        user_input = int(input("Inserisci un numero tra 1 e 100: "))

        if user_input > num_random:
            raise ValoreTroppoAlto
        elif user_input < num_random:
            raise ValoreTroppoBasso
        else:
            print("Hai indovinato!")
            flag = True
    except ValoreTroppoAlto:
        print("Il numero inserito è troppo alto. Ritenta!")
    except ValoreTroppoBasso:
        print("Il numero inserito è troppo basso. Ritenta!")

```

## Esercizio n.5

Cosa stampa il seguente codice?

```
x = 500

def numero():
  global x
  x = 150

numero()

print(x) 
```

## Esercizio n.6

Cosa stampa il seguente codice?

```
balance = 0

def addAmount(x):
    global balance
    balance = balance + x

addAmount(5)
print(balance)
```

## Esercizio n.7

Cosa fa il seguente codice?

```
import random
 
list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))
 
string = "striver"
print(random.choice(string))

```

## Esercizio n.8

Cosa fa il seguente codice?

```
import random
 

sample_list = ['A', 'B', 'C', 'D', 'E']
 
print("Original list : ")
print(sample_list)
 
random.shuffle(sample_list)
print("\nAfter the first shuffle : ")
print(sample_list)
```

## Esercizio n.9

Cosa stampa il seguente codice?


```
import platform
  
print(platform.architecture())
print(platform.processor())
print(platform.machine())
print(platform.platform())
print(platform.system())
print(platform.system())

```