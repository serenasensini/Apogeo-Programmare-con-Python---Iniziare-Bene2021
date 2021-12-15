class Attrezzo:

    def __init__(self, p_nome, p_peso):
        self.nome = p_nome
        self.peso = p_peso

    def __repr__(self):
        print("Il nome dell'attrezzo è", self.nome)
        print(self.nome, "pesa", self.peso, "kg")

    def get_nome(self):
        return self.nome

    def get_peso(self):
        return self.peso

    def set_nome(self, p_nome):
        self.nome = p_nome

    def set_peso(self, p_peso):
        self.peso = p_peso