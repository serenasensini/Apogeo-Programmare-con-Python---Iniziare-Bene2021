class Zaino:

    NUM_ATTREZZI = 4
    MAX_PESO = 10

    def __init__(self):
        self.attrezzi = []
        self.peso = 0

    def get_attrezzi(self):
        return self.attrezzi

    def get_peso(self):
        for attrezzo in self.attrezzi:
            self.peso += attrezzo.get_peso()
        return self.peso

    def set_attrezzi(self, attrezzi):
        self.attrezzi = attrezzi

    def add_oggetto(self, oggetto):
        peso_attuale = self.get_peso()
        peso_aggiornato = oggetto.get_peso() + peso_attuale
        if peso_aggiornato > self.MAX_PESO or len(self.attrezzi) > self.NUM_ATTREZZI:
            print("Non posso aggiungere l'oggetto perché lo zaino è troppo carico!")
        else:
            self.attrezzi.append(oggetto)
            self.get_peso()

    def remove_oggetto(self, nomeOggetto):
        index = 0
        for oggetto in self.attrezzi:
            if oggetto.get_nome() == nomeOggetto:
                self.attrezzi.pop(index)
            index += 1

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