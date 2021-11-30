# Lezione #4

## Soluzione n.1
Creare due tuple che rappresentino i due
elenchi di nomi e cognomi descritti sotto:
* nomi: Numa, Tullo, Anco
* cognomi: Pompilio, Ostilio, Marzio

```
>>> nomi = ('Numa','Tullo','Anco')
>>> cognomi = ('Pompilio','Ostilio','Marzio')
```

## Soluzione n.2
Ottenere una lista in cui ogni elemento è un
dizionario {'nome': nome, 'cognome':
cognome}, che accoppia nomi e cognomi in
base all'ordine.

```
>>> l = []
>>> for nome, cognome in zip(nomi,cognomi):
... l.append({'nome': nome, 'cognome': cognome})
...
>>> l
[{'cognome': 'Pompilio', 'nome': 'Numa'},
{'cognome': 'Ostilio', 'nome': 'Tullo'},
{'cognome': 'Marzio', 'nome': 'Anco'}]
```

## Soluzione n.3
* Creare un dizionario che contenga come
chiavi 'nome' e 'cognome', inserendo i propri
dati come valori
* Aggiungere 'matricola'
* Aggiungere 'esami', provando ad immaginare
che tipi di dato usare per rappresentare sia
nome che voto degli esami
  
```
>>> d = {'nome':'Pinco','cognome':'Pluto'}
>>> d['matricola'] = 258115
>>> d['esami'] = [{'nome':'Informatica','voto': 30},
{'nome':'Analisi','voto': 18}]
>>> d
{'nome':'Pinco','cognome':'Pippo','matricola':
258115,'esami':[{'nome':'Informatica','voto': 30},
{'nome':'Analisi','voto': 18}]}
```

## Soluzione n.4
Scrivere un programma che, dati i due elenchi di
numeri sottostanti, crei la matrice dei loro prodotti:
* v1: 1,2,3,4,5
* v2: 6,7,8,9,10
* mat:
1*6 1*7 1*8 ...
2*6 2*7 2*8 ...
...
Completare il programma con una stampa della
matrice riga per riga.
  
## Soluzione n.5
Scrivere un programma che definisca una funzione
stampa_matrice(mat), che migliori la stampa
dell'Soluzione precedente, fornendo un formato tabellare.
Per fare in modo che i numeri siano stampati allineati,
usare per ogni numero:
`print('%3i' % num)`

```
def stampa_matrice(mat):
    for row in mat:
        for num in row:
            print('%3i' % num)
        print
```

## Soluzione n.6
Aggiungere al programma precedente una funzione
square(val,n), che ritorni una matrice quadrata di
dimensione n con il valore val in ogni cella . Utilizzare la funzione stampa_matrice(mat) per
stampare nella console interattiva una matrice 6x6 con
il valore 0 in ogni cella.

```
def square(val, n):
    mat = []
    for i in range(0,n):
        row = []
        for j in range(0,n):
            row.append(val)
        mat.append(row)
    return mat
```

## Soluzione n.7
Definire una funzione eratostene(n) che ritorni tutti i
numeri primi da 2 a n inclusi, utilizzando il procedimento
del Crivello di Eratostene:
* Si crea un elenco di tutti i numeri naturali da 2 a n,
detto setaccio.
* Si aggiunge il primo numero del setaccio all'elenco dei
numeri primi trovati, e si eliminano dal setaccio tutti i
suoi multipli. Si prosegue in questo modo fino ad
esaurire i numeri nel setaccio.
  
```

def eratostene(n):
    setaccio = range(2, n+1)
    primi = []
    while setaccio: # finche' ci sono numeri nel setaccio
        primi.append(setaccio[0])
        setaccio = filter(lambda x: x%primi[-1], setaccio)
    return primi

```


## Soluzione n.8
Scrivere una funzione conta_caratteri(s) che ritorni un
dizionario contenente il numero di occorrenze per
ciascun carattere presente nella stringa.

```
def conta_caratteri (s):
    conteggio = {}
    for c in s:
        if c in conteggio:
        conteggio[c] += 1
        else:
        conteggio[c] = 1
    return conteggio
```

## Soluzione n.9
Scrivere un programma che stampi tutti i numeri
perfetti inferiori ad un numero n dato in ingresso.
* Un numero naturale è perfetto se è uguale alla somma
dei suoi divisori propri e dell'unità.
Per esempio 6: i divisori propri di 6 sono 2 e 3, e la
somma di 2, 3 e dell'unita' ha come risultato 6.
* 0 non è un numero perfetto.

```
def perfetto(n):
    if n == 0:
        return False
    divisori = []
    for i in range(1,n):
        if n % i == 0:
            divisori.append(i)
    return sum(divisori) == n

n = int(raw_input( 'Inserisci un numero positivo: ' ))
    for i in range(0, n):
        if perfetto(i):
            print(i)
```

## Soluzione n.14
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

## Soluzione n.15
Scrivi un programma che, passata come parametro una lista di interi, fornisce in output il maggiore tra i numeri contenuti nella lista.
```
def max_in_list(list):
    my_max = 0
    for num in list:
        if num > my_max:
            my_max = num
    print(f"Il numero più grande della lista passata è {my_max}")
```

## Soluzione n.16
Scrivi una funzione che data in ingresso una lista A contenente n parole, restituisca in output una lista B di interi che rappresentano la lunghezza delle parole contenute in A.
```
# due possibili soluzioni per l'Soluzione proposto

def char_counter(lista_a):
    lista_b = []
    for parola in lista_a:
        lista_b.append(len(parola))
    return lista_b

def char_counter_pro(lista_a):
    return [len(parola) for parola in lista_a]
```

## Soluzione n.17
Scrivi una funzione a cui passare una stringa come parametro, e che restituisca un dizionario rappresentante la "frequenza di comparsa" di ciascun carattere componente la stringa.
```
def char_freq(str):
    mappa = {}
    for carattere in str:
        if carattere in mappa:
            mappa[carattere] += 1
        else:
            mappa[carattere] = 1
    return mappa
```

## Gioco!
In Svezia, i bambini giocano spesso utilizzando un linguaggio un po' particolare 
detto "rövarspråket", che significa "linguaggio dei furfanti": 
consiste nel raddoppiare ogni consonante di una parola e inserire 
una "o" nel mezzo. Ad esempio la parola "mangiare" diventa "momanongogiarore".

Scrivi una funzione in grado di tradurre una parola o frase passata tramite input in "rövarspråket".

Dopo aver tradotto una frase, il programma dovrà chiedere all'utente 
se intende tradurne un'altra, e in caso di risposta positiva, 
dovrà attendere l'inserimento di una nuova parola da parte dell'utente.

```
def traduttore():
    print("""
    Ciao! questo programma traduce un testo passato in "rövarspråket".
    Ció significa che raddoppia ogni consonante delle parole e ci mette una "o" in mezzo...
    """)

    vocali = "aeiou"

    # volendo puoi ovviamente aggiungere ulteriori caratteri speciali alla lista...
    specials = [" ", ",", ".", "?", "!", '"',"'"]

    while True:
        testo = input("\nInserisci il testo che desideri tradurre: ")
        tradotta = ""
        # mangiare
        for carattere in testo:
            if carattere in vocali or x in specials:
                tradotta += carattere
            else:
                tradotta = tradotta + carattere + "o" + carattere

        print(f"Ecco a te la traduzione! '{tradotta}'")

        if input("\nDesidere tradurre un'altra frase? ") == "no":
            break
```