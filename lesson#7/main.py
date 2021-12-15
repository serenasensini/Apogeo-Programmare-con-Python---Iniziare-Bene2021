# a = 5
# b = 0
#
# try:
#     if b == 0:
#         raise FileNotFoundError
#     divisione = a/b
# except ZeroDivisionError:
#     print("La divisione di un numero per 0 non è possibile")
# except TypeError:
#     print("Non è possibile effettuare la divisione tra un numero e un non-numero")
# except:
#     print("C'è stato un errore")
# else:
#     print(a/b)
#
#
#
# class Utente:
#
#     global nickname
#
#     def __init__(self, mail, data_nascita):
#         self.nickname = ''
#         self.mail = mail
#         self.data_nascita = data_nascita
#
#     def __repr__(self):
#         print("--------------")
#         print("Nome utente:", self.nickname)
#         print("Mail:", self.mail)
#
# utente = Utente("pippo@gmail.com", "02/01/1970")
# utente.__repr__()

import platform

print(platform.platform())
print(platform.system())
print(platform.release())
print(platform.version())

import math

print(math.sqrt(16))