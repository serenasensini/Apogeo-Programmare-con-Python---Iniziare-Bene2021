class Comando:

    global nome
    global parametro

    def __init__(self):
        pass

    def __repr__(self):
        print("------------")
        print("Comando inserito:", self.nome)
        print("Parametro inserito:", self.parametro)
        print("------------")

    def get_nome(self):
        return self.nome

    def get_parametro(self):
        return self.parametro

    def nuovo_comando(self):
        istruzione = input(">>> ")
        comandi = istruzione.split()
        self.nome = comandi[0]
        if len(comandi) > 1:
            self.parametro = comandi[1]
        else:
            self.parametro = ""
