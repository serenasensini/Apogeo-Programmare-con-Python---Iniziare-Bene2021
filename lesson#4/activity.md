# Lezione #4

## Esercizio n.1
Creare due tuple che rappresentino i due
elenchi di nomi e cognomi descritti sotto:
* nomi: Numa, Tullio, Anco
* cognomi: Pompilio, Ostilio, Marzio

## Esercizio n.2
Ottenere una lista in cui ogni elemento è un
dizionario {'nome': nome, 'cognome':
cognome}, che accoppia nomi e cognomi in
base all'ordine.

## Esercizio n.3
* Creare un dizionario che contenga come
chiavi 'nome' e 'cognome', inserendo i propri
dati come valori
* Aggiungere 'matricola'
* Aggiungere 'esami', provando ad immaginare
che tipi di dato usare per rappresentare sia
nome che voto degli esami

## Esercizio n.4
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
  
## Esercizio n.5
Scrivere un programma che definisca una funzione
stampa_matrice(mat), che migliori la stampa
dell'esercizio precedente, fornendo un formato tabellare.
Per fare in modo che i numeri siano stampati allineati,
usare per ogni numero:

```print('%3i' % num)```

## Esercizio n.6
Aggiungere al programma precedente una funzione
square(val,n), che ritorni una matrice quadrata di
dimensione n con il valore val in ogni cella . Utilizzare la funzione stampa_matrice(mat) per
stampare nella console interattiva una matrice 6x6 con
il valore 0 in ogni cella.

## Esercizio n.7
Definire una funzione eratostene(n) che ritorni tutti i
numeri primi da 2 a n inclusi, utilizzando il procedimento
del Crivello di Eratostene:
* Si crea un elenco di tutti i numeri naturali da 2 a n,
detto setaccio.
* Si aggiunge il primo numero del setaccio all'elenco dei
numeri primi trovati, e si eliminano dal setaccio tutti i
suoi multipli. Si prosegue in questo modo fino ad
esaurire i numeri nel setaccio.

## Esercizio n.8
Scrivere una funzione conta_caratteri(s) che ritorni un
dizionario contenente il numero di occorrenze per
ciascun carattere presente nella stringa.

## Esercizio n.9
Scrivere un programma che stampi tutti i numeri
perfetti inferiori ad un numero n dato in ingresso.
* Un numero naturale è perfetto se è uguale alla somma
dei suoi divisori propri e dell'unità.
Per esempio 6: i divisori propri di 6 sono 2 e 3, e la
somma di 2, 3 e dell'unita' ha come risultato 6.
* 0 non è un numero perfetto.

## Esercizio n.10
Stampa i caratteri tra la terza e la sesta posizione della stringa "Hello world!".

## Esercizio n.11
Stampa i caratteri dalla terza posizione in poi della stringa "Hello wolrd!".

## Esercizio n.12
Stampa i caratteri tra la quinta e la seconda posizione della stringa "Hello world!".

## Esercizio n.13
Scrivere una funzione reverse(s) che ritorni la stringa passata come parametro al contrario.

## Esercizio n.14
Scrivere un programma in grado di calcolare il fattoriale di un dato numero.
I risultati dovrebbero essere stampati in una sequenza separata da virgole su una singola riga.
Supponiamo che al programma venga fornito il seguente input:
8
Quindi, l'output dovrebbe essere:
40320

## Esercizio n.15
Scrivi un programma che, passata come parametro una lista di interi, fornisce in output il maggiore tra i numeri contenuti nella lista.

## Esercizio n.16
Scrivi una funzione che data in ingresso una lista A contenente n parole, restituisca in output una lista B di interi che rappresentano la lunghezza delle parole contenute in A.

## Esercizio n.17
Scrivi una funzione a cui passare una stringa come parametro, e che restituisca un dizionario rappresentante la "frequenza di comparsa" di ciscun carattere componente la stringa.

## Gioco!
In Svezia, i bambini giocano spesso utilizzando un linguaggio un po' particolare detto 
"rövarspråket", che significa "linguaggio dei furfanti": consiste nel raddoppiare ogni 
consonante di una parola e inserire una "o" nel mezzo. Ad esempio la parola "mangiare" diventa 
"momanongogiarore".

Scrivi una funzione in grado di tradurre una parola o frase passata tramite input in 
"rövarspråket".

Dopo aver tradotto una frase, il programma dovrà chiedere all'utente se intende tradurne
un'altra, e in caso di risposta positiva, dovrà attendere l'inserimento di una nuova 
parola da parte dell'utente.