# Lezione #3

## Esercizio n.1
Calcolare la somma dei primi 500 numeri naturali (da 0 a 500 escluso)

## Esercizio n.2
Data la stringa 'abcdefghi', scrivere
un programma che analizzi la stringa e
stampi a video:
Lettera 1: a
Lettera 2: b
...
E così via.
Modificare poi il programma in modo da
leggere la stringa da tastiera.

## Esercizio n.3
Scrivere una funzione area_cerchio che, dato un raggio, calcola la sua area. Scrivere anche una funzione circonferenza, che calcola in maniera analoga il suo perimetro.

## Esercizio n.4
Modificare il codice del gioco della palla magica presente nella cartella dei file per gli esercizi, usando le condizioni elif per quelle in eccesso: usare risposte del tipo
* Meglio non dirlo ora.
* Ne sei sicuro?
* Direi proprio di sì.
* La mia risposta è no.
* Chiedimelo più tardi.
* Dovresti rifletterci di più.
* Ci puoi contare.
* Le mie fonti dicono di sì.

Far sì che il gioco non finisca finché l'utente non digita una stringa uguale a "exit".

## Esercizio n.5
Scrivi un programma Python che stampi tutti i numeri da 0 a 6 tranne 3 e 6.

## Esercizio n.6
Scrivi un programma Python per stampare il modello alfabetico 'P'.
```
 ****                                                                   
 *   *                                                                  
 *   *                                                                  
 ****                                                                   
 *                                                                      
 *                                                                      
 *  
```

## Esercizio n.7
Scrivi un programma che stampi il countdown, che dato come parametro di ingresso un numero, restituisce il countdown a partire da quel numero, fino a zero. Usare il ciclo for.

## Esercizio n.8
Ripetere l'esercizio precedente e usare il ciclo while.

## Esercizio n.9
Scrivi una funzione che prende due numeri come parametro e manda in print il più grande tra i due. Per quanto Python disponga di una funzione max(), sei invitato a utilizzare le istruzioni If, Elif ed Else per la scrittura dell'algoritmo.

## Esercizio n.10
Scrivi una funzione che prende stavolta tre numeri come parametro e restituisce il più grande tra loro!

## Esercizio n.11
Scrivi una funzione "sommatrice" che somma tra loro tutti gli elementi di una lista di numeri.

## Esercizio n.12
Scrivi una funzione che, dato in ingresso un valore espresso in metri, mandi in print l'equivalente in miglia terrestri, iarde, piedi e pollici.

## Esercizio n.13
Correggi il seguente codice:
```
paragrafo = "Viviamo in un mondo che ci disorienta con la sua complessità. Vogliamo comprendere ciò che vediamo attorno a noi e chiederci: Qual è la natura dell'universo? Qual è il nostro posto in esso? Da che cosa ha avuto origine l'universo e da dove veniamo noi? "

def stampaParagrafo(testo):
print testo
	
stampaPararrafo()
```

## Esercizio n.14
Scrivere una funzione “equalTo” che, dato un array di numeri qualsiasi e un numero scelto, conti quante volte il numero scelto compare nell'array.
Esempio: [1,2,4,8,12,4,3]
NumeroScelto = 4
Suggerimento: usare una variabile contatore, dove “contare” quante volte viene trovato il numero scelto...

## Esercizio n.15
Scrivere un programma che conti le occorrenze
della “a” nelle seguenti parole:
- Banana;
- Aiuola;
- Abracadrabra;
- Elfo.

## Esercizio n.16
Scrivere un programma che conti i numeri pari presenti in un array.

## Esercizio n.17
Scrivere una funzione “reverse” che, data una stringa, la stampi carattere per carattere al contrario.

## Esercizio n.18
Scrivere una funzione divisibiliPerCinque che, dato il seguente array:
[10, 23, 45, 92, 70, 1020, 71]
stampi solo gli elementi divisibili per cinque.

## Esercizio n.19
Per calcolare il volume di alcune figure solide, è utile prima calcolare l'area di base e poi utilizzarla nel calcolo seguente: prendiamo in esempio una piramide a base quadrata. Scrivere una funzione
che calcola prima l'area di base e poi un'altra che usa il calcolo per calcolare il volume.
Area base = lato x lato
Volume piramide = (Abase x altezza) / 3

## Esercizio n.20
Per calcolare la media di alcune misurazioni, è utile prima calcolare la somma e poi fare la divisione in base agli input. Per semplicità, si
definisca una funzione che calcola la somma di 3 input (con ritorno) e un'altra che ne calcola la media (con ritorno).

## Gioco!

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