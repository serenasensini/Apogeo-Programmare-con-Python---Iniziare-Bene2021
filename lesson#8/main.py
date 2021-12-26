import os

## path assoluto (True/False)
out = os.path.isabs("lesson#1")
print(out)

## isdir
out = os.path.isdir("C:\\Users")
print(out)

## isfile
out = os.path.isfile("C:\\Users\\serena.sensini\\python.zip")
print(out)

## Get the current working directory (CWD)
cwd = os.getcwd()
print(cwd)


## Function to get the current working directory
def current_path():
    print("Current working directory:")
    print(os.getcwd())
    print()


current_path()

os.chdir('../')

current_path()

## CREATE A DIR

directory = "test"

# Parent Directory path
parent_dir = ".\\"

# Path
path = os.path.join(parent_dir, directory)

os.mkdir(path)
print("Directory '% s' created" % directory)

## Get the list of all files and directories in the specified  directory
path = "C:\\Users\\serena.sensini\\Documents"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")

# print the list
print(dir_list)

val = input("Inserisci un valore: ")
print(val)

num = input("Inserisci un numero :")
print(num)

print("Tipo della variabile:", type(num))
