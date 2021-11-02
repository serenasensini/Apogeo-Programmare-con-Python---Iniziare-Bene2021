# Lezione #1

## Soluzione
Stampa il tuo nome.
```
print("Hello Serena!")
```

## Soluzione
Crea una variabile che contenga un nome e una con un numero di telefono, e stampane il contenuto.

## Soluzione
Crea una variabile che contenga una barzelletta e poi stampane il risultato.
```
print("Qual è il colmo per due divorziati americani? Essere… stati uniti.")
```

## Soluzione
Scrivere un programma che restituisca il risultato di tutte le possibile combinazioni dei valori booleani con l'operatore AND.
```
print(False and False)
print(False and True)
print(True and False)
print(True and True)
```

## Soluzione
Scrivere un programma che restituisca il risultato di tutte le possibile combinazioni dei valori booleani con l'operatore NOT AND.
```
print(!(False and False))
print(!(False and True))
print(!(True and False))
print(!(True and True))
```

## Soluzione
Scrivere un programma che, date due variabili a e b rispettivamente uguali a 58 e 43, ne stampi il risultato.
```
print(58+43)
```

## Soluzione
Scrivere un programma che, date tre variabili x, y, z, rispettivamente uguali a 3, 4 e 5, ne calcoli prima la somma, e poi la moltiplicazione.
```
x = 3
y = 4
z = 5
print(x + y + z)
print(x * y * z)
```

## Soluzione
Stampare il risultato di 
*caldo
*brutto_tempo
*tormenta

dove caldo è vero, brutto_tempo è falso e tormenta è falso.

```
x = True
y = False
z = False
print(x and y and z)
```

## Soluzione
Stampa il risultato della somma tra 328 e 7789.
```
print(328+7789)
```

## Soluzione
Qual è il risultato?
a. True and not False
b. True and not false
c. True or True and False
d. not True or not False
e. True and not 0
f. 52 < 52.3
g. 1 + 52 < 52.3
h. 4 != 4.0

```
a. True
b. Traceback (most recent call last):
  File "./prog.py", line 1, in <module>
NameError: name 'false' is not defined
c. False
d. True
e. True
f. True
g. False
h. False
```

## Soluzione
Scrivi un'espressione che restituisce True solo se tutte e tre le variabili sono vere.

```
x = True
y = True
z = False
x and y and not z
```

## Soluzione 
Scrivi un'espressione per cui viene stampato True solo se la variabile è uguale a False.

```
x = False
print(not x)
```

## Soluzione
Scrivi un'espressione che stampa True se almeno due delle variabili sono uguali a True.

```
x = True
y = True
z = False

print((x and y) or z) or ((x and z) or y) or ((y and z) or x))
```

## Soluzione
Scrivi un commento multiriga.
```
#This is a comment
#written in
#more than just one line
```

```
"""
This is a comment
written in
more than just one line
"""
```

## Esercizio
Cosa stampa?

```
x = 5
y = "Pluto"
print(x)
print(y)
```

```
5
Pluto
```

## Esercizio
Cosa stampa?

```
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
```

```
Sally
```

## Esercizio
Cosa stampa?

```
x = str(3.75)
y = int(3.75)
z = float(3.75) 
print(x)
print(y)
print(z)
```

```
3.75
3
3.75
```

## Esercizio
Sono la stessa cosa?
x = "Pippo"
x = 'Pippo'


## Esercizio
Cosa stampa?

```
a = 4
A = "Pluto" 
print(a)
print(A)
```

## Esercizio
Quali di questi nomi variabili sono corretti?
```
myvar = "Pluto"
my_var = "Pluto"
_my_var = "Pluto"
myVar = "Pluto"
MYVAR = "Pluto"
myvar2 = "Pluto"
2myvar = "Pluto"
my-var = "Pluto"
my var = "Pluto"
```

## Esercizio
Quale di questi è un esempio di Camel Case?
* my_variable = "Paperino"
* myVariableName = "Paperino"
* MyVariableName = "Paperino"

## Esercizio
Quale di questi è un esempio di Snake Case?
* my_variable = "Paperino"
* myVariableName = "Paperino"
* MyVariableName = "Paperino"

## Esercizio
Quale di questi è un esempio di Pascal Case?
* my_variable = "Paperino"
* myVariableName = "Paperino"
* MyVariableName = "Paperino"

## Esercizio
Crea tre variabili e assegna loro i nomi di 3 personaggi di Topolino in una sola riga.

## Esercizio
Crea tre variabili e assegna loro "Paperon de Paperoni".

## Esercizio
Cosa stampa?

```
print(5 + 'a')
```

## Esercizio
Qual è il tipo delle seguenti variabili?
```
x = "Paperino"
y = 20.5
z = 1j
a = True
b = b"Hello"
c = ("a", "b", "c")
```

## Esercizio
Rendi tutta in maiuscolo la seguente stringa: "Index".

## Esercizio
Rendi tutto in minuscolo la seguente stringa: "Index".

## Esercizio
Rimuovi tutti gli spazi dalla seguente stringa.
```
Lorem ipsum dolor sit amet.
```

## Esercizio
Sostituisci il placeholder XYZ con un nome.
```
"Ciao XYZ, benvenuti al corso di Python."
```

## Esercizio
Cosa stampa?
```
a = "Hello"
b = "World"
c = a + b
```

## Esercizio
Cosa stampa?
```
a = "Hello"
b = "World"
c = a + " " + b
```

## Esercizio 
Stampa una stringa che sia esattamente uguale a questa: Un tempo l'Iran si chiamava "Persia".

```
print('Un tempo l\'Iran si chiamava "Persia".')
```


## Esercizio
Fai di modo che il risultato della seguente stringa sia come riportato successivamente.
```
Input:
C’è un’ape che se posa su un bottone de rosa: lo succhia e se ne va… Tutto sommato, la felicità è una piccola cosa.

Output:
C’è un’ape che se posa
su un bottone de rosa:
lo succhia e se ne va…
Tutto sommato, la felicità
è una piccola cosa.
```

```
print("C’è un’ape che se posa" + "\n" + "su un bottone de rosa:")
```

## Esercizio
Rendi l'intera stringa in Camel Case:
```
prova a mettere ogni lettera iniziale in maiuscolo.
```

```
s = "prova a mettere ogni lettera iniziale in maiuscolo."
s = s.title()
print(s)
```

## Esercizio
Cosa stampa?
```
a = "Roma"
a.islower()
a.isdecimal()
a.isnumeric()
a.isspace()
a.alnum()
```

## Esercizio
Stampa la lunghezza della seguente stringa.
```
Test Yourself With Exercises
```

```
s = "Test Yourself With Exercises"
print(len(s))
```

## Esercizio
Cosa stampa?
```
print(10 > 9)
print(10 == 9)
print(10 < 9) 
```

## Esercizio
Cosa stampa?
```
print(10%2)
```

## Esercizio
Cosa stampa?
```
print(10/2)
```

## Esercizio
Cosa stampa?
```
print(10**2)
```

## Esercizio
Cosa stampa?
```
print(11//2)
```

## Esercizio
Scrivi un programma che, dati la base e l'altezza di un triangolo, ne calcoli l'area.

```
base = 2
altezza = 3
area = base * altezza / 2
```

## Esercizio
Scrivere un programma  per convertire le temperature da e verso Celsius, Fahrenheit.

```
# (temperature °C × 9/5) + 32 = 50 °F
c_temperature = 20
formula = c_temperature * (9/5) + 32
print(formula)
```