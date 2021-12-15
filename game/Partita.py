from Stanza import Stanza
from Attrezzo import Attrezzo
from game.Personaggio import Personaggio
from game.Zaino import Zaino


class Partita:

    global stanza_corrente
    global stanza_vincente

    def __init__(self):
        self.game_over = False
        self.passi = 20
        self.zaino = Zaino()
        self.crea_stanze()

    def crea_stanze(self):
        print("------------")
        print("Sto creando le stanze...")
        # STEP 1: CREARE LE STANZE
        biblioteca = Stanza("Biblioteca")
        aula_magna = Stanza("Aula Magna")
        laboratorio_chimica = Stanza("Laboratorio chimica")
        segreteria = Stanza("Segreteria")
        mensa = Stanza("Mensa")
        cucina = Stanza("Cucina")
        aula_a = Stanza("Aula A")
        aula_b = Stanza("Aula B")
        laboratorio_informatica = Stanza("Laboratorio di Informatica")
        sala_server = Stanza("Sala server")

        # STEP 2: IMPOSTARE LE STANZE ADIACENTI

        biblioteca.set_stanza_adiacente("est", aula_magna)
        aula_magna.set_stanza_adiacente("est", laboratorio_chimica)
        aula_magna.set_stanza_adiacente("sud", segreteria)
        laboratorio_chimica.set_stanza_adiacente("ovest", aula_magna)
        laboratorio_chimica.set_stanza_adiacente("sud", mensa)
        segreteria.set_stanza_adiacente("nord", aula_magna)
        segreteria.set_stanza_adiacente("est", mensa)
        segreteria.set_stanza_adiacente("sud", aula_a)
        mensa.set_stanza_adiacente("ovest", segreteria)
        mensa.set_stanza_adiacente("nord", laboratorio_chimica)
        mensa.set_stanza_adiacente("est", cucina)
        mensa.set_stanza_adiacente("sud", aula_b)
        cucina.set_stanza_adiacente("ovest", mensa)
        cucina.set_stanza_adiacente("sud", laboratorio_informatica)
        aula_a.set_stanza_adiacente("nord", segreteria)
        aula_a.set_stanza_adiacente("est", aula_b)
        aula_b.set_stanza_adiacente("ovest", aula_a)
        aula_b.set_stanza_adiacente("est", laboratorio_informatica)
        aula_b.set_stanza_adiacente("nord", mensa)
        laboratorio_informatica.set_stanza_adiacente("nord", cucina)
        laboratorio_informatica.set_stanza_adiacente("ovest", aula_b)
        laboratorio_informatica.set_stanza_adiacente("sud", sala_server)
        sala_server.set_stanza_adiacente("nord", laboratorio_informatica)

        # STEP 3: CREARE GLI OGGETTI

        cacciavite = Attrezzo("Cacciavite", 4)
        chiavi = Attrezzo("Chiavi", 2)
        osso = Attrezzo("Osso", 5)
        libro = Attrezzo("Analisi", 3)

        # STEP 4: CREARE I PERSONAGGI E AGGIUNGERE LORO GLI OGGETTI
        scienziato_pazzo = Personaggio("Frankestein", "Essere uno scienziato pazzo", "Si... può... fareee!")
        cane_tre_teste = Personaggio("Cane a tre teste", "Sbranare in un sol boccone", "Roarrr! Ho una gran fame!!!")
        professor_tozzi = Personaggio("Professor Tozzi", "Uccidere a colpi di 2", "I ragazzi non si applicano abbastanza! Mi serve proprio un buon libro di Analisi per fare un bel ripasso...")
        sistemista = Personaggio("Sistemista", "Aggiusto cose", "Spengi e riaccendi. Funziona sempre")

        professor_tozzi.add_oggetto(osso)

        # STEP 5: AGGIUNGERE I PERSONAGGI NELLE STANZE
        laboratorio_chimica.add_personaggio(scienziato_pazzo)
        laboratorio_informatica.add_personaggio(sistemista)
        sala_server.add_personaggio(cane_tre_teste)
        aula_b.add_personaggio(professor_tozzi)

        # STEP 6: POSARE GLI OGGETTI NELLE STANZE SECONDO INDICAZIONI

        laboratorio_chimica.add_attrezzo(cacciavite)
        segreteria.add_attrezzo(chiavi)
        biblioteca.add_attrezzo(libro)

        # STEP 7: IMPOSTARE LA STANZA INIZIALE E LA STANZA VINCENTE

        self.stanza_vincente = sala_server
        self.stanza_corrente = biblioteca

        # STEP 8: ASSEGNARE GLI OGGETTI DESIDERATI AI PERSONAGGI E ALLE STANZE
        cane_tre_teste.set_oggetto_desiderio(osso)
        professor_tozzi.set_oggetto_desiderio(libro)
        sistemista.set_oggetto_desiderio(chiavi)
        mensa.set_oggetto_desiderio(cacciavite)

        # STEP 8: BLOCCARE LE STANZE CHE RICHIEDONO CHE IL PERSONAGGIO ABBIA UN OGGETTO
        mensa.blocca()
        laboratorio_informatica.blocca()
        sala_server.blocca()

        print("Fatto! Sei pronto per giocare.")
        print("------------")

    def get_stanza_vincente(self):
        return self.stanza_vincente

    def get_stanza_corrente(self):
        return self.stanza_corrente

    def set_stanza_corrente(self, stanza):
        self.stanza_corrente = stanza

    def has_vinto(self):
        return self.stanza_vincente == self.stanza_corrente

    def is_game_over(self):
        return self.has_vinto() or self.game_over or self.passi == 0

    def get_passi(self):
        return self.passi

    def get_zaino(self):
        return self.zaino
