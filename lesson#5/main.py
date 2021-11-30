# n.1

# Definire una classe che rappresenti un utente
# e i relativi attributi, come lo username,
# la mail e la data di nascita.

# class Utente:
#     # Proprietà:
#     # - username
#     # - mail
#     # - data_nascita
#
#     def __init__(self, username, email, data):
#         self.username = username
#         self.mail = email
#         self.data_nascita = data
#
#     def __repr__(self):
#         print("Lo username dell'utente è:", self.username)
#         print("La sua email è:", self.mail)
#         print("La sua data di nascita è il:", self.data_nascita)
#
#     def get_username(self):
#         return self.username
#
#     def get_email(self):
#         return self.mail
#
#     def get_data_nascita(self):
#         return self.data_nascita
#
#     def set_username(self, nuovo_username):
#         self.username = nuovo_username
#
#     def set_mail(self, nuova_email):
#         self.mail = nuova_email
#
#     def set_data_nascita(self, nuova_data_nascita):
#         self.data_nascita = nuova_data_nascita
#
#
# user = Utente("mick89", "mick89@gmail.com", "30/05/1989")
# user.__repr__()
#
# user.set_username("pippo89")
# user.__repr__()
#
# print(user.get_email())


# n.2

# Definire una classe che rappresenti un auto
# e i relativi attributi, come la marca, il modello,
# l'anno di immatricolazione e il numero di porte.

class Auto:

    # Proprietà
    # - marca
    # - modello
    # - cilindrata
    # - colore

    def __init__(self, p_marca, p_modello, p_cilindrata, p_colore):
        self.marca = p_marca
        self.modello = p_modello
        self.cilindrata = p_cilindrata
        self.colore = p_colore

    def __repr__(self):
        print("La marca è: ", self.marca)
        print("Il modello è:", self.modello)
        print("La sua cilindrata è:", self.cilindrata, "cc")
        print("Il colore è:", self.colore)

    def get_marca(self):
        return self.marca

    def get_modello(self):
        return self.modello

    def get_cilindrata(self):
        return self.cilindrata

    def get_colore(self):
        return self.colore

    def set_marca(self, nuova_marca):
        self.marca = nuova_marca

auto_serena = Auto("Lancia", "Ypsilon", "70", "Blu")
auto_serena.set_marca("Fiat")

print(auto_serena.get_marca())
auto_serena.__repr__()


