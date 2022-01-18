# I/O

# leggere tutte le righe di un file
# file = open("filename.txt", "r")
# print(file.readlines())
# file.close()

# leggere il contenuto
# file = open("filename.txt", "r")
# cont = file.read()
# print(cont)
# print(cont[1])
# file.close()

# leggere riga per riga con un for
# file = open("filename.txt", "r")
# cont = file.read()
# print(cont)
# for line in file:
#     print(line)
# file.close()

# leggere delle righe specifiche
# file = open("filename.txt", "r")
# lines = [2, 3]
#
# for position, line in enumerate(file):
#     if position in lines:
#         print(line)

# scrittura: esempi

# file = open("filename.txt", "r")
# print("Reading contents")
# print(file.read())
# file.close()

# file = open("filename.txt", "a")
# file.write("Some bla bla bla")
# file.close()

# file = open("filename.txt", "r")
# print("Reading new contents")
# print(file.read())
# file.close()


import os

## path assoluto (True/False)
# out = os.path.isabs("C:\\Test")
# print(out)
#
# ## isdir
# out = os.path.isdir("C:\\Users")
# print(out)
#
# ## isfile
# out = os.path.isfile("C:\\Users\\seren\\Documents\\icon.png")
# print(out)
#
# ## Get the current working directory (CWD)
# cwd = os.getcwd()
# print(cwd)
#
#
# ## Function to get the current working directory
# def current_path():
#     print("Current working directory:")
#     print(os.getcwd())
#     print()
#
#
# current_path()
#
# os.chdir('../')
#
# current_path()
#
# ## CREATE A DIR
#
# directory = "test"

# Parent Directory path
# parent_dir = "./"

# Path
# path = os.path.join(parent_dir, directory)
# print(path)

# os.mkdir(path)
# print("Directory '% s' created" % directory)
#
## Get the list of all files and directories in the specified  directory
# path = "../lesson"
# dir_list = os.listdir(path)
#
# print("Files and directories in '", path, "' :")
#
# print the list
# print(dir_list)
#
# val = input("Inserisci un valore: ")
# print(val)

# num = input("Inserisci un numero: ")
# print(num)

# print("Tipo della variabile:", type(num))

# print(num.isnumeric())
# print(num.isdigit())
# print(num.isdecimal())

# real_num = int(num)
# print(real_num)
# print(type(real_num))

# frase = "Lorem ipsum"
# print(frase)
# print(frase.split())
#
# x, y = input("Inserisci due valori: ").split()
# print("Numero di gatti: ", x)
# print("Numero di cani: ", y)
# print()


# Soluzione n.1
'''
Aprire il file nella cartella data/lorem.txt,
scriverci dentro una frase e poi chiuderlo.
'''

# miofile = open("./data/lorem.txt", "w+")
# miofile.write("lorem ipsum")
# miofile.close()

# Soluzione n.2
'''
Aprire il file creato in precedenza, 
leggerne il contenuto e stamparlo.
'''
# myfile = open("./data/lorem.txt", "r")
# out = myfile.read()
# myfile.close()
# print(out)

# Soluzione n.5

'''
Aprire il file nella cartella data/test.txt... Ops! Non esiste. Gestire l'eccezione in maniera opportuna usando try/catch.
'''

# try:
#     myfile = open("./data/test.txt", "r")
# except FileNotFoundError:
#     print("Il file non esiste! Te lo creo")
#     myfile = open("./data/test.txt", "w+")
# except:
#     print("Si è verificato un errore")

# Soluzione n.3

'''
Aprire il file nella cartella data/cupcake.txt, leggerlo e contare il numero di 
occorrenze delle seguenti parole, inserendole all'interno di un dizionario:
- cupcake
- chocolate
- donut
'''

# SOLUZIONE a
myfile = open("./data/cupcake.txt", "r")

contenuto = myfile.read()
print(contenuto)

myfile.close()

contenuto = contenuto.lower()

num_cupcake = contenuto.count("cupcake")
num_chocolate = contenuto.count("chocolate")
num_donut = contenuto.count("donut")

print(num_cupcake)
print(num_chocolate)
print(num_donut)

dizionario = {"cupcake": num_cupcake, "chocolate": num_chocolate, "donut": num_donut}
print(dizionario)

# SOLUZIONE b

myfile = open("./data/cupcake.txt", "r")

contenuto = myfile.read()
myfile.close()

contenuto = contenuto.lower().replace(".", " ").split()

lista_parole = ["cupcake", "chocolate", "donut"]

diz = {"cupcake": 0, "chocolate": 0, "donut": 0}

for k in contenuto:
    print(k)
    if k in lista_parole:
        # diz[k] = diz[k] + 1
        diz[k] += 1

print(diz)
