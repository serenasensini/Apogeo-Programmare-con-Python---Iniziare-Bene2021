# Lezione #2

## Soluzione
Definire un programma che valuta i seguenti casi:
* Se il parametro passato è uguale a “piove”, allora viene restituita una stringa che dice “rimanda appuntamento”;
* Se il parametro invece è “sole”, allora viene restituita “puoi partecipare all'evento”;
* Se non avviene nessuno di questi casi, allora stampa “non ho capito”.
```
previsione = "piove"
if (previsione == "piove"):
    print("Rimanda appuntamento")
elif (previsione == "piove"):
    print("Puoi partecipare all'evento")
```

## Soluzione
Cosa stampa?
```
a = 33
b = 200
if b > a:
  print("b is greater than a")
```

## Soluzione
Scrivi un programma che trovi tutti questi numeri che sono divisibili per 7 ma non sono multipli di 5.
```
if(num % 7 == 0 and num % 5 != 0):
    print("Corretto")
else:
    print("Errato")
```

## Soluzione
Scrivere un programma in grado di calcolare il fattoriale di un dato numero.
I risultati dovrebbero essere stampati in una sequenza separata da virgole su una singola riga.
Supponiamo che al programma venga fornito il seguente input:
8
Quindi, l'output dovrebbe essere:
40320
```
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)
```

## Soluzione
Scrivi un programma per cui, se il voto inserito è maggiore del 65, allora l'esame è passato.
```
x = 10
if x >= 65:
    print("Approvato!")
else:
    print("Fallito")
```

## Soluzione
Scrivi un programma che stampi se un numero è pari, dispari o negativo.
```
x = 10
if x >= 0:
    print("x is positive ")
    if (x%2) == 0:
        print("x is even")
    else:
        print("x is odd")
else:
    print("x is negative")
```

## Soluzione
Scrivi un programma che stampi se un numero è pari, dispari o negativo.

## Soluzione
Scrivi un programma che accetti un intero (n) e calcoli il valore di n+nn+nnn.

## Soluzione
Scrivi un programma per verificare se un numero è compreso tra 100 di 1000 o 2000.

## Soluzione
Scrivi un programma per calcolare la somma di tre numeri dati, se i valori sono uguali restituisci tre volte la loro somma.

## Soluzione
Scrivi un programma per sommare tre numeri interi dati. Tuttavia, se due valori sono uguali, la somma sarà zero.

## Soluzione
Scrivi un programma  che restituirà vero se i due valori interi dati sono uguali o la loro somma o differenza è 5.

## Soluzione 
Scrivere un programma  per rimuovere i caratteri che hanno valori di indice dispari di una data stringa.

## Soluzione
Individua le modifiche necessarie al seguente codice affinché sia rispettata la PEP8.
```
>>> # Not recommended
>>> x = 'John Smith'
>>> y, z = x.split()
>>> print(z, y, sep=', ')
'Smith, John'

```

## Soluzione
Individua le modifiche necessarie al seguente codice affinché sia rispettata la PEP8.
```
# Name of the user
username = "John"
```


## Soluzione
Individua le modifiche necessarie al seguente codice affinché sia rispettata la PEP8.
```
l = 1
O = 2
I = 3
```

## Soluzione
Individua le modifiche necessarie al seguente codice affinché sia rispettata la PEP8.
```
# a 79-char ruler:
# 34567891123456789212345678931234567894123456789512345678961234567897123456789123456789123456789123456789123456789123456789123456789123456789
```


## Soluzione
Individua le modifiche necessarie al seguente codice affinché sia rispettata la PEP8.
```
a=1
b=2
c=3
print(a+b+c)
```

## Soluzione
Scrivere un programma che converta il numero del mese nella stringa corrispondente.
```
I.e: 1 => "Gennaio", 2 => "Febbraio", ecc.
```

## Soluzione
Scrivi un programma Python per verificare se un alfabeto è una vocale o una consonante.

## Soluzione
Scrivi un programma Python per verificare che un triangolo sia equilatero, isoscele o scaleno.

## Soluzione
Cosa stampa?

```
x = 'a' if 4 ==  2 + 2 else 'b'  # x è uguale a 
x = 'a' if 4 ==  3 + 2 else 'b'  # x è uguale b
```

## Soluzione
Crea un programma per soli maggiorenni: se la variabile è maggiore di 18, stampa "Puoi entrare", "Non puoi entrare" altrimenti.

```
print('Programma riservato ad utenti maggiorenni')

anni = int ( input('Quanti anni hai? ') )

if anni >= 18:
	delta = anni - 18
	print('sei maggiorenne da', delta, 'anni')
	print('PUOI ENTRARE')
else:
	delta = 18 - anni
	print('sei minorenne ancora per', delta, 'anni')
	print('NON PUOI ENTRARE')
```

## Soluzione
Scrivi un programma Python per verificare che la password inserita dall'utente (salvata precedentemente in una variabile) sia corretta. Sia se è corretta, sia se non lo è, stampare un messaggio.

```
password = input('Enter password ')

if password == "CorsoPython@#29":
    print("Password corretta")
else:
    print("Password sbagliata")
```

## Soluzione
Scrivi un programma Python per trovare il più grande tra due numeri inseriti in input.
```
num1 = int(input('Inserisci il primo numero: '))
num2 = int(input('Inserisci il secondo numero: '))

if num1 >= num2:
    if num1 == num2:
        print(num1, 'e', num2, 'sono uguali')
    else:
        print(num1, 'è più grande di ', num2)
else:
    print(num1, 'è più piccolo di', num2)
```

## Soluzione
Scrivi un programma Python per verificare se il numero inserito contiene due, tre o quattro cifre.

```
n = int(input("Enter any number:"))
if n>0 and n<10:
    print("One digit number")
elif n>10 and n<100:
    print("Two digit number")
elif n>100 and n<1000:
    print("Three digit number")
else:
    print("More than three digit number")
```

## Soluzione
Scrivi un programma Python per verificare se la stringa è scritta tutta in maiuscolo oppure in minuscolo. 

```
word = "LOREM IPSUM"
if word.isLower():
    print("Tutto minuscolo")
elif word.isUpper():
    print("Tutto maiuscolo")
else:
    print("Nessuno dei due casi!")
```
