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

# class Auto:
#
#     # Proprietà
#     # - marca
#     # - modello
#     # - cilindrata
#     # - colore
#
#     def __init__(self, p_marca, p_modello, p_cilindrata, p_colore):
#         self.marca = p_marca
#         self.modello = p_modello
#         self.cilindrata = p_cilindrata
#         self.colore = p_colore
#
#     def __repr__(self):
#         print("La marca è: ", self.marca)
#         print("Il modello è:", self.modello)
#         print("La sua cilindrata è:", self.cilindrata, "cc")
#         print("Il colore è:", self.colore)
#
#     def get_marca(self):
#         return self.marca
#
#     def get_modello(self):
#         return self.modello
#
#     def get_cilindrata(self):
#         return self.cilindrata
#
#     def get_colore(self):
#         return self.colore
#
#     def set_marca(self, nuova_marca):
#         self.marca = nuova_marca
#
# auto_serena = Auto("Lancia", "Ypsilon", "70", "Blu")
# auto_serena.set_marca("Fiat")
#
# print(auto_serena.get_marca())
# auto_serena.__repr__()

## CORREZIONE ESERCIZI

## Gioco!
#
"Definisci una classe per creare un quiz a punti:"
"come proprietà il quiz ha una serie di domande e risposte"
"(suggerimento: rappresentarli tramite dizionario),"
#"per cui vanno definiti i metodi appropriati, tra cui i getter e setter
#"e un metodo per poter giocare. Usare domande come le seguenti:
#"```
#Quanto fa 5 x 2?": "10",
#Qual è la radice quadrata di 64?": "8",
#Quanti sono stati i re di Roma?": "7"
#"```
#w = {"Come ti chiami?: Nome  "}
# class Gioco01:
#         def __init__(self, prima_domanda, seconda_domanda):
#             self.prima_domanda = prima_domanda
#             self.seconda_domanda = seconda_domanda
# #        come_ti_chiami
#         def __repr__(self):
#             print("Il tuo nome é: ", self.prima_domanda)
#             print("Il tuo cognome é: ",self.seconda_domanda)
#
#         def get_prima_domanda(self):
#             return self.prima_domanda
#
#         def get_seconda_domanda(self):
#             return self.seconda_domanda
#
#         def set_prima_domanda(self, risposta_prima_domanda):
#             self.prima_domanda = risposta_prima_domanda
#
#         def set_seconda_domanda(self, risposta_seconda_domanda):
#             self.seconda_domanda = risposta_seconda_domanda
#
# user = Gioco01("Come ti chiami, Nome? : ", "Cognome ? : ")
#
# user.__repr__()
#
# user.set_prima_domanda("cosa chiede ?")
#
# user.__repr__()


## SOLUZIONE n.8

# Definire una classe che rappresenti un film: includere il regista, l'anno di distribuzione
# , un elenco di attrici e attori, il titolo e il genere. Includere i metodi setter
# e getter per ciascuna proprietà, e definire anche un metodo per stamparne i dettagli.

# class Film:
#
#     def __init__(self):
#         self.regista = "ND"
#         self.anno_distribuzione = 0
#         self.attrici = []
#         self.attori = []
#         self.titolo = "ND"
#         self.genere = "ND"
#
#     def __repr__(self):
#         return "Class Film - Titolo [" + self.titolo + "]; Regista [" + self.regista + "]; Anno [" \
#                + str(self.anno_distribuzione) + "]"
#
#     def set_regista(self, nome_regista):
#         self.regista = nome_regista
#
#     def set_anno_distr(self, p_anno):
#         self.anno_distribuzione = p_anno
#
#     def set_attrici(self, p_attrici):
#         self.attrici = p_attrici
#
#     def set_attori(self, p_attori):
#         self.attori = p_attori
#
#     def set_titolo(self, p_titolo):
#         self.titolo = p_titolo
#
#     def set_genere(self, p_genere):
#         self.genere = p_genere
#
#     def get_regista(self):
#         return self.regista
#
#     def get_anno_distr(self):
#         return self.anno_distribuzione
#
#     def get_attrici(self):
#         return self.attrici
#
#     def get_attori(self):
#         return self.attori
#
#     def get_titolo(self):
#         return self.titolo
#
#     def get_genere(self):
#         return self.genere


# arancia_meccanica = Film()
# arancia_meccanica.set_titolo("Arancia Meccanica")
# arancia_meccanica.set_regista("Stanley Kubrik")
# arancia_meccanica.set_anno_distr(1971)
# arancia_meccanica.set_genere("Distopico")
# arancia_meccanica.set_attori(["Malcolm MacDowell", "Antony Burges", "Patrick Magee"])
# arancia_meccanica.set_attrici(["Adrianne Corri", "Miriam Carlin"])
# print(arancia_meccanica.__repr__())

## SOLUZIONE N.9

# Definire una classe che rappresenti un immobile, con le relative proprietà
# (locali, bagni, garage (si/no), piano, quartiere) e includere i metodi setter
# e getter per ciascuna proprietà; definire anche un metodo per stamparne i dettagli.

class Appartamento:

    def __init__(self, p_locali, p_piano, p_mq, p_classe_energetica, p_prezzo):
        self.locali = p_locali
        self.piano = p_piano
        self.mq = p_mq
        self.classe_energetica = p_classe_energetica
        self.prezzo = p_prezzo
        self.garage = "No"
        self.quartiere = ""
        self.bagni = 1

    def __repr__(self):
        print("Numero di vani: " +str(self.locali))
        print("Piano: " + self.piano)
        print("Metri quadrati: " + str(self.mq))
        print("Classe energetica: " + self.classe_energetica)
        print("Prezzo: " + str(self.prezzo) + " euro")
        print("Garage (si/no):" + self.garage)
        print("Quartiere: " + self.quartiere)
        print("Bagni: " + str(self.bagni))

    def get_locali(self):
        return self.locali

    def get_piano(self):
        return self.piano

    def get_mq(self):
        return self.mq

    def get_classe_energetica(self):
        return self.classe_energetica

    def get_prezzo(self):
        return self.prezzo

    def get_garage(self):
        return self.garage

    def get_quartiere(self):
        return self.quartiere

    def get_bagni(self):
        return self.bagni

    def set_locali(self, p_locali):
        self.locali = p_locali

    def set_piano(self, p_piano):
        self.piano = p_piano

    def set_mq(self, p_mq):
        self.mq = p_mq

    def set_classe_energetica(self, p_classe_energetica):
        self.classe_energetica = p_classe_energetica

    def set_prezzo(self, p_prezzo):
        self.prezzo = p_prezzo

    def set_garage(self, p_garage):
        self.garage = p_garage

    def set_bagni(self, p_bagni):
        self.bagni = p_bagni

    def set_quartiere(self, p_quartiere):
        self.quartiere = p_quartiere

residenza_dorata = Appartamento(3, "T", 450, "A+", 1200000)
residenza_dorata.set_garage("si")
residenza_dorata.set_bagni(4)
residenza_dorata.set_quartiere("Crocetta")

residenza_dorata.__repr__()