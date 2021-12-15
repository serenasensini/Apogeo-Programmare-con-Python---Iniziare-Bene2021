from Partita import Partita
from Comando import Comando


class Labirinto:
    global elenco_comandi

    def __init__(self):
        self.partita = Partita()
        self.elenco_comandi = ["vai", "aiuto", "fine", "direzioni"]

    def gioca(self):
        print("------------")
        print("Ti trovi nell'Universita', ma oggi e' diversa dal solito...\n" +
              "Meglio andare al piu' presto in biblioteca a studiare. Ma dov'e'?\n" +
              "I locali sono popolati da strani personaggi, " +
              "alcuni amici, altri... chissa!\n" +
              "Ci sono attrezzi che potrebbero servirti nell'impresa:\n" +
              "puoi raccoglierli, usarli, posarli quando ti sembrano inutili\n" +
              "o regalarli se pensi che possano ingraziarti qualcuno.\n" +
              "Per conoscere le istruzioni usa il comando 'aiuto'.")
        print("------------")

        while not self.partita.is_game_over():
            comando = Comando()
            comando.nuovo_comando()
            self.processa_istruzione(comando)

        self.fine()

    def processa_istruzione(self, istruzione):
        if self.partita.is_game_over():
            self.fine()
        elif istruzione.get_nome() == "fine":
            self.fine()
        elif istruzione.get_nome() == "aiuto":
            self.aiuto()
        elif istruzione.get_nome() == "vai":
            self.vai(istruzione.get_parametro())
        elif istruzione.get_nome() == "direzioni":
            self.list_direzioni()
        # STEP 4a - TODO: aggiungere opzione "prendi nomeAttrezzo" (suggerimento: seguire il metodo "vai")
        # scrivi qui

        # STEP 4b - TODO: aggiungere opzione "posa nomeAttrezzo" (suggerimento: seguire il metodo "vai")
        # scrivi qui

        # STEP 5 - TODO: aggiungere opzione "regala nomeAttrezzo" (suggerimento: seguire il metodo "vai")
        # scrivi qui
        # STEP OPZIONALE - TODO: modificare i metodi 'regala' e 'prendi' affinché il personaggio "ringrazi"
        '''
        Quando il giocatore regala un oggetto al personaggio, il personaggio dovrà restituire un messaggio per
         "ringraziare" l'utente, invocando questo metodo ogni volta che il comando 'regala' va a buon fine.
        '''
        # scrivi qui
        # STEP 1 - TODO: aggiungere opzione finale "NON HO CAPITO"
        # scrivi qui

    def aiuto(self):
        print("------------")
        print("Elenco comandi disponibili:", self.elenco_comandi)
        print("------------")

    def fine(self):
        self.partita.game_over = True
        print("------------")
        print("GAME OVER!")
        print("Grazie per aver giocato!")
        print("------------")

    def vai(self, direzione):
        if direzione is None or len(direzione) == 0:
            print("Ma dove pensi di andare? La direzione specificata non è valida!")
            return
        prossima_stanza = self.partita.get_stanza_corrente().get_stanza_adiacente(direzione)
        if prossima_stanza is None:
            print("HEY! Non esiste alcuna stanza in questa direzione!")
        elif prossima_stanza.is_bloccata():
            print("ATTENZIONE! Questa stanza è bloccata... Sicuro che tu abbia preso tutto quello che ti serve?")
            print("Oggetti necessari per entrare:", prossima_stanza.get_oggetto_desiderio().get_nome())
        else:
            self.partita.set_stanza_corrente(prossima_stanza)
            self.partita.passi -= 1

        self.partita.get_stanza_corrente().__repr__()

        # STEP 3 - TODO: MODIFICARE QUESTO METODO AFFINCHé STAMPI IL NUMERO DI PASSI RIMANENTI

    def list_direzioni(self):
        print(self.partita.get_stanza_corrente().get_direzioni())

    # STEP 4a - TODO: aggiungere metodo "prendi" che ha come input il nome di un attrezzo
    '''
    1. Verificare che il nome dell'attrezzo corrisponda ad uno di quelli che il personaggio (se presente nella stanza) o la stanza stessa possiede
    2. Se sì, rimuovere l'oggetto dal personaggio o dalla stanza e aggiungerlo allo zaino (sfruttare i metodi presenti nella classe Zaino)
    3. Altrimenti, restituire un messaggio di errore
    '''
    def prendi(self, nome_oggetto):
        # in primis, verifico se l'oggetto è tra quelli che ha il personaggio
        trovato = False
        # per ogni personaggio nella stanza...
        for personaggio in self.partita.get_stanza_corrente().get_personaggi():
            # per ogni oggetto posseduto dal personaggio...
            for oggetto in personaggio.get_oggetti():
                # se l'oggetto ha lo stesso nome di quello passato come parametro...
                if oggetto.get_nome() == nome_oggetto:
                    # allora lo rimuovo dal personaggio...
                    personaggio.remove_oggetto()
                    # lo aggiungo allo zaino...
                    self.partita.get_zaino().add_oggetto(oggetto)
                    # e mi segno di averlo trovato!
                    trovato = True
                    print("Oggetto preso!")
        # se l'oggetto non è tra quelli del personaggio, allora controllo la stanza
        if not trovato:
            # per ogni oggetto nella stanza corrente...
            for oggetto in self.partita.get_stanza_corrente().list_attrezzi():
                # se l'oggetto ha lo stesso nome di quello passato come parametro..
                if nome_oggetto == oggetto.get_nome():
                    # allora lo rimuovo da quelli presenti nella stanza
                    self.partita.get_stanza_corrente().remove_attrezzo(nome_oggetto)
                    self.partita.get_zaino().add_oggetto(oggetto)
                    print("Oggetto preso!")


    # STEP 4b - TODO: aggiungere metodo "posa" che ha come input il nome di un attrezzo
    '''
    1. Verificare che il nome dell'attrezzo corrisponda ad uno di quelli che sono presenti nello zaino (se presente)
    2. Se sì, rimuovere l'oggetto dallo zaino e aggiungerlo a quelli della stanza (sfruttare i metodi presenti nella classe Stanza)
    3. Altrimenti, restituire un messaggio di errore
    
    Suggerimento: segui il metodo "posa", se ti perdi!
    '''

    # STEP 5 - TODO: aggiungere metodo "regala" che ha come input il nome di un attrezzo
    '''
    1. Verificare che il nome dell'attrezzo corrisponda ad uno di quelli che sono presenti nello zaino (se presente)
    2. Se sì, rimuovere l'oggetto dallo zaino e aggiungerlo a quelli del personaggio (sfruttare i metodi presenti nella classe Personaggio)
    3. Altrimenti, restituire un messaggio di errore
    '''

# INIZIO GIOCO
labirinto = Labirinto()
labirinto.gioca()
