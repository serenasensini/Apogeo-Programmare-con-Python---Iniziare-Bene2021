# Lezione #5

## Esercizio n.1
Correggere il seguente codice:

```
list = [10, 20, 30, 40, 50, 60, 70]

counter = 0
for element in list: 
    if element % 5 = 0:
        counter += 1
        
print(counter)
```

## Esercizio n.2

Correggere il seguente codice:

```
lst = ['Alice', 'Bob', 'Carl']
print(lst[3])
```


## Esercizio n.3

Correggere il seguente codice:

```
tupla = ('Alice', 'Bob')
print(tupla[2])
```

## Esercizio n.4

Correggere il seguente codice:

```
def area_cerchio(raggio):
    print(3.14***raggio**2)

def circonferenza(raggio):
    print(3.14*raggio*2)

area_cerchiO(3)
circonfrenza(4)
```

## Esercizio n.5

Correggere il seguente codice:

```
def moltiplicazione(a,b):
    print a*b

moltiplicazione('a',1)

```

## Esercizio n.6

Definire una classe che rappresenti un utente e i relativi attributi, come lo username, la mail e la data di nascita.

## Esercizio n.7 

Definire una classe che rappresenti un auto e i relativi attributi, come la marca, il modello, l'anno di immatricolazione e il numero di porte.

## Esercizio n.8

Definire una classe che rappresenti un film: includere il regista, l'anno di distribuzione, un elenco di attrici e attori, il titolo e il genere. Includere i metodi setter e getter per ciascuna proprietà, e definire anche un metodo per stamparne i dettagli.

## Esercizio n.9

Definire una classe che rappresenti un immobile, con le relative proprietà (locali, bagni, garage (si/no), piano, quartiere) e includere i metodi setter e getter per ciascuna proprietà; definire anche un metodo per stamparne i dettagli.

## Esercizio n.10 

Definire una classe per rappresentare un/a regista, che ne includa le proprietà anagrafiche ed anche i film girati. Includere i metodi setter e getter per ciascuna proprietà, e definire anche un metodo per stamparne i dettagli.

## Gioco!

Definisci una classe per creare un quiz a punti: come proprietà il quiz ha una serie di domande e risposte (suggerimento: rappresentarli tramite dizionario), per cui vanno definiti i metodi appropriati, tra cui i getter e setter e un metodo per poter giocare. Usare domande come le seguenti:

```
"Quanto fa 5 x 2?": "10",
"Qual è la radice quadrata di 64?": "8",
"Quanti sono stati i re di Roma?": "7"
```