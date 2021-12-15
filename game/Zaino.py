class Zaino:

    def __init__(self):
        self.attrezzi = []
        self.peso = 0

    def add_oggetto(self, oggetto):
        self.attrezzi.append(oggetto)

# STEP 0 - TODO: creare uno zaino che contenga degli attrezzi.
'''
Attenzione però: il numero di attrezzi che lo zaino può contenere è al massimo di 4 e il loro peso non può superare
i 10 chili, altrimenti il nostro giocatore non riuscirà a sopportarne il peso!

Modificare quindi questa classe affinché definisca le proprietà necessarie a contenere degli attrezzi, con relativi
metodi getter e setter.

Aggiornare anche i comandi 'prendi', 'posa' e 'regala' (vedi STEP 4 e 5) affinché valutino le dimensioni e il peso dello zaino 
prima di permettere al giocatore di prendere altri oggetti.

Definire quindi anche dei metodi per aggiungere e rimuovere un attrezzo da quelli presenti nello 
zaino sulla base del nome passato come parametro.
'''