# SOLUZIONE N.1

class Person:

    def __init__(self, p_nome, p_cognome, p_data_nascita):
        self.nome = p_nome
        self.cognome = p_cognome
        self.data_nascita = p_data_nascita

    def __repr__(self):
        print("Il nome della persona è:" + self.nome)
        print("Il cognome della persona è:" + self.cognome)
        print("La data di nascita della persona è:" + self.data_nascita)

    def get_nome(self):
        return self.nome

    def get_cognome(self):
        return self.cognome

    def get_data_nascita(self):
        return self.data_nascita

    def set_nome(self, p_nome):
        self.nome = p_nome

    def set_cognome(self, p_cognome):
        self.cognome = p_cognome

    def set_data_nascita(self, p_data_nascita):
        self.data_nascita = p_data_nascita

    # def get_area(self):
    #     return 3

class Student(Person):

    def __init__(self, p_nome, p_cognome, p_data_nascita, p_matricola):
        # super() si riferisce alla classe padre e istanzia un oggetto di tipo Person
        super().__init__(p_nome, p_cognome, p_data_nascita)
        # self fa riferimento allo Student
        self.matricola = p_matricola

    # def get_area(self):
    #     return 5

    def __repr__(self):
        print(super().__repr__())
        print("Il numero di matricola è: " + str(1542332))

class Professor(Person):

    def __init__(self, p_nome, p_cognome, p_data_nascita, p_materia):
        super().__init__(p_nome, p_cognome, p_data_nascita)
        self.materia = p_materia

    def __repr__(self):
        super().__repr__()
        print("Il professore insegna:" + self.materia)

# s1 = Student("Mario", "Rossi", "23/05/1990", "34567890")
# s1.__repr__()

# per costruire un oggetto, uso una notazione del tipo: NOME_CLASSE(*parametri) =>
tozzi = Professor("Ugo", "Tozzi", "01/04/1964", "Matematica")
# per usare i metodi di un oggetto, uso NOME_OGGETTO.METODO =>
tozzi.__repr__()


