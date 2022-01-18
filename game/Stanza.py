class Stanza:

    global NUMERO_MASSIMO_DIREZIONI
    global NUMERO_MASSIMO_ATTREZZI

    def __init__(self, nome):
        self.NUMERO_MASSIMO_ATTREZZI = 2
        self.NUMERO_MASSIMO_DIREZIONI = 4
        self.nome = nome
        self.attrezzi = []
        self.stanzeAdiacenti = {}
        self.numeroStanzeAdiacenti = len(self.stanzeAdiacenti)
        self.direzioni = []
        self.bloccata = False
        self.personaggio = None
        self.oggetto_desiderio = None

    def __repr__(self):
        print("------------")
        print("Ti trovi nella stanza:", self.nome)
        if self.attrezzi and len(self.attrezzi) > 0:
            print("Il numero di attrezzi presenti nella stanza è", len(self.attrezzi))
            print("Questi sono gli attrezzi presenti:", self.list_attrezzi())
        if self.personaggio:
            print("In questa stanza c'è uno strano personaggio...")
            print("'''")
            print(self.personaggio.__repr__())
            print("'''")

        print("------------")

    '''
    Imposta una stanza adiacente.
    @param direzione direzione in cui sara' posta la stanza adiacente.
    @param stanza stanza adiacente nella direzione indicata dal primo parametro.
    '''
    def set_stanza_adiacente(self, direzione, stanza):
        # aggiornato = False
        self.stanzeAdiacenti[direzione] = stanza
        self.direzioni = []
        for dir in self.stanzeAdiacenti.keys():
            self.direzioni.append(dir)

    '''
    Restituisce la stanza adiacente nella direzione specificata
    @param direzione
    '''
    def get_stanza_adiacente(self, direzione):
        stanza = None
        for dir in self.stanzeAdiacenti.keys():
            if dir == direzione:
                stanza = self.stanzeAdiacenti[dir]

        return stanza

    '''
    Mette un attrezzo nella stanza.
    @param attrezzo l'attrezzo da mettere nella stanza.
    @return true se riesce ad aggiungere l'attrezzo, false altrimenti.
    '''
    def add_attrezzo(self, attrezzo):
        if len(self.attrezzi) < self.NUMERO_MASSIMO_ATTREZZI:
            self.attrezzi.append(attrezzo)
            print("Attrezzo aggiunto nella stanza!")
            return True
        else:
            return False

    '''
    Controlla se un attrezzo esiste nella stanza (uguaglianza sul nome).
    @return true se l'attrezzo esiste nella stanza, false altrimenti.
    '''
    def has_attrezzo(self, nome_attrezzo):
        flag = False
        for element in self.attrezzi:
            if element.nome == nome_attrezzo:
                flag = True
        return flag

    '''
    Permette di prendere l'attrezzo con nomeAttrezzo, se presente nella stanza.
    @param nome_attrezzo
    @return l'attrezzo presente nella stanza, None se non è presente
    '''
    def get_attrezzo(self, nome_attrezzo):
        attrezzo = None
        for element in self.attrezzi:
            if element.nome == nome_attrezzo:
                attrezzo = element
        return attrezzo

    '''
    Rimuove un attrezzo dalla stanza (ricerca in base al nome).
    @param nome_attrezzo
    @return true se l'attrezzo e' stato rimosso, false altrimenti
    '''
    def remove_attrezzo(self, nome_attrezzo):
        index = 0
        for oggetto in self.attrezzi:
            if nome_attrezzo == oggetto.get_nome():
                self.attrezzi.pop(index)
                break
            index += 1

    def get_direzioni(self):
        return self.direzioni

    def get_nome(self):
        return self.nome

    def get_attrezzi(self):
        return self.attrezzi

    def get_personaggio(self):
        return self.personaggio

    def list_attrezzi(self):
        attrezzi = []
        for attrezzo in self.attrezzi:
            attrezzi.append(attrezzo.get_nome())

        return attrezzi

    def is_bloccata(self):
        return self.bloccata

    def sblocca(self):
        self.bloccata = False

    def blocca(self):
        self.bloccata = True

    def add_personaggio(self, personaggio):
        self.personaggio = personaggio

    def get_oggetto_desiderio(self):
        return self.oggetto_desiderio

    def set_oggetto_desiderio(self, oggetto):
        self.oggetto_desiderio = oggetto

    def has_oggetto_desiderio(self):
        oggetto_desiderato = self.get_oggetto_desiderio()
        if oggetto_desiderato is None:
            return True
        for oggetto in self.attrezzi:
            if oggetto.get_nome().lower() == oggetto_desiderato.get_nome().lower():
                return True
        return False
