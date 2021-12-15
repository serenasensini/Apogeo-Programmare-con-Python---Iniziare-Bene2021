# SOLUZIONE N.1

# class Person:
#
#     def __init__(self, p_nome, p_cognome, p_data_nascita):
#         self.nome = p_nome
#         self.cognome = p_cognome
#         self.data_nascita = p_data_nascita
#
#     def __repr__(self):
#         print("Il nome della persona è:" + self.nome)
#         print("Il cognome della persona è:" + self.cognome)
#         print("La data di nascita della persona è:" + self.data_nascita)
#
#     def get_nome(self):
#         return self.nome
#
#     def get_cognome(self):
#         return self.cognome
#
#     def get_data_nascita(self):
#         return self.data_nascita
#
#     def set_nome(self, p_nome):
#         self.nome = p_nome
#
#     def set_cognome(self, p_cognome):
#         self.cognome = p_cognome
#
#     def set_data_nascita(self, p_data_nascita):
#         self.data_nascita = p_data_nascita
#
#     # def get_area(self):
#     #     return 3
#
# class Student(Person):
#
#     def __init__(self, p_nome, p_cognome, p_data_nascita, p_matricola):
#         # super() si riferisce alla classe padre e istanzia un oggetto di tipo Person
#         super().__init__(p_nome, p_cognome, p_data_nascita)
#         # self fa riferimento allo Student
#         self.matricola = p_matricola
#
#     # def get_area(self):
#     #     return 5
#
#     def __repr__(self):
#         print(super().__repr__())
#         print("Il numero di matricola è: " + str(1542332))
#
# class Professor(Person):
#
#     def __init__(self, p_nome, p_cognome, p_data_nascita, p_materia):
#         super().__init__(p_nome, p_cognome, p_data_nascita)
#         self.materia = p_materia
#
#     def __repr__(self):
#         super().__repr__()
#         print("Il professore insegna:" + self.materia)
#
# # s1 = Student("Mario", "Rossi", "23/05/1990", "34567890")
# # s1.__repr__()
#
# # per costruire un oggetto, uso una notazione del tipo: NOME_CLASSE(*parametri) =>
# tozzi = Professor("Ugo", "Tozzi", "01/04/1964", "Matematica")
# # per usare i metodi di un oggetto, uso NOME_OGGETTO.METODO =>
# tozzi.__repr__()
#
#


## SOLUZIONE N.2

'''
Creare una classe poligono che abbia come attributo il numero di lati e i relativi getter e setter. Creare poi una classe
per il triangolo equilatero e il quadrato, aggiungendo i metodi necessari per calcolare perimetro e area.
'''

# class Poligono:
#
#     def __init__(self, p_num_lati, p_lato):
#         self.num_lati = p_num_lati
#         self.lato = p_lato
#
#     def __repr__(self):
#         print("Il poligono ha", self.num_lati, "lati")
#         print("Il lato del poligono vale:", self.lato)
#
#     def get_num_lati(self):
#         return self.num_lati
#
#     def get_lato(self):
#         return self.lato
#
#     def set_num_lati(self, p_num_lati):
#         self.num_lati = p_num_lati
#
#     def set_lato(self, p_lato):
#         self.lato = p_lato
#
#     def get_perimetro(self):
#         return self.lato * self.num_lati

# poligono = Poligono(5, 50)

# poligono.__repr__()


# class Triangolo(Poligono):
#
#     def __init__(self, p_num_lati, p_lato):
#         super().__init__(p_num_lati, p_lato)
#
#     def __repr__(self):
#         super().__repr__()
#         # print("Il triangolo ha", self.num_lati)
#         # print("Ogni lato del triangolo misura", self.lato)
#
#     def get_area(self):
#         return self.lato * self.lato * 1.71 / 4


# triangolo = Triangolo(3, 10)
# print("L'area del triangolo con lato", triangolo.get_lato(), "ha area", triangolo.get_area())

## SOLUZIONE N.7

'''
Scrivere una classe Personaggio, che fa parte di un gioco con diversi personaggi magici. 
Ognuno di loro ha un nome, un potere ed una citazione preferita. I personaggi possono essere maghi o streghe: 
i maghi, se salutati, restituiscono il saluto, mentre le streghe maledicono chi li saluta.
Inoltre, il mago ha degli oggetti magici da donare che sono contenuti in una sacca. Creare le funzioni 
appropriate a rappresentare i requisiti sopra citati, inizializzando gli opportuni oggetti per testare la classe.
'''


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


class Personaggio:

    def __init__(self, p_nome, p_potere, p_citazione):
        self.nome = p_nome
        self.potere = p_potere
        self.citazione = p_citazione

    def __repr__(self):
        print("Mi chiamo", self.nome)
        print("Il mio potere è", self.potere)
        print("Questa è la mia citazione preferita", self.citazione)

    # TODO
    # definire getter e setter per il personaggio


class Mago(Personaggio):

    def __init__(self, p_nome, p_potere, p_citazione, p_oggetti_magici):
        super().__init__(p_nome, p_potere, p_citazione)
        self.oggetti_magici = p_oggetti_magici

    def __repr__(self):
        super().__repr__()
        print("Nel mio sacco puoi trovare questi oggetti:")
        for oggetto in self.oggetti_magici:
            oggetto.__repr__()


# bacchetta_magica = Attrezzo("Bacchetta", 0.1)
# mantello = Attrezzo("Mantello magico", 0.0001)
#
# strumenti_magici = [bacchetta_magica, mantello]
#
# merlino = Mago("Mago Merlino", "congelare le persone", "Oketi Pocketi Wocketi Wa", strumenti_magici)
#
# merlino.__repr__()

# TODO
class Strega:

    pass