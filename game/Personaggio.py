import Attrezzo

class Personaggio:

    def __init__(self, p_nome, p_potere, p_citazione):
        self.nome = p_nome
        self.potere = p_potere
        self.citazione = p_citazione
        self.oggetti = []
        self.oggetto_desiderio = None

    def __repr__(self):
        print("Mi chiamo", self.nome)
        print("Il mio potere è", self.potere)
        print("Dico sempre che:", self.citazione)

    def get_oggetti(self):
        return self.oggetti

    def remove_oggetto(self, nome_oggetto):
        index = 0
        for oggetto in self.oggetti:
            if nome_oggetto == oggetto.get_nome():
                self.oggetti.pop(index)
                break

    def add_oggetto(self, oggetto):
        self.oggetti.append(oggetto)

    def get_oggetto_desiderio(self):
        return self.oggetto_desiderio

    def set_oggetto_desiderio(self, oggetto):
        self.oggetto_desiderio = oggetto

    def has_oggetto_desiderio(self):
        oggetto_desiderato = self.get_oggetto_desiderio()
        for oggetto in self.oggetti:
            if oggetto.get_nome() == oggetto_desiderato.get_nome():
                return True
        return False
