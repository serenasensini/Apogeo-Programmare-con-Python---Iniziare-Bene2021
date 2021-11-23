# esempio liste

thislist = ["apple", "banana", "cherry"]
print("Initial list", thislist)

thislist.append("strawberry")
print("Updated list:", thislist)
print("Index of 'banana: ", thislist.index("banana"))
# print("Index of an unknown element: ", thislist.index("dog"))
print("Get element with negative index:", thislist[-2])

new_list = ["mango", "papaya"]
thislist.extend(new_list)
print("Updated list:", thislist)

## esercizi n.15

'''
Scrivi un programma che, passata come parametro una 
lista di interi, fornisce in output il maggiore tra 
i numeri contenuti nella lista.
'''

# lista = [4, 6, 10, 19, 2]
#
# max = 0
#
# # per ogni (for) numero presente nella (in) lista
# for numero in lista:
#     if numero >= max:
#         max = numero
#
# print(max)
#
# lista.sort()
# print(lista)

# tuple

# tupla x
# x = ("apple", "banana", "cherry")
# # trasformo la tupla x in lista y
# y = list(x)
# print(type(y))
# y[1] = "pear"
# y.insert(1, "mango")
# print(y)
# x = tuple(y)
#
# print(x)

prezzi_frutta = {'mela':1.99, 'pera':2.49, 'uva':2.99, 'mela':2.99}
print(prezzi_frutta['mela'])

prezzi_frutta['melone'] = 0.99
prezzi_frutta['fragole'] = 2.29
prezzi_frutta['pera'] = 1.99

del prezzi_frutta['pera']
print(prezzi_frutta)
# print(len(prezzi_frutta))
#
# prezzi_frutta.update({"'mela'": "2.19"})
#
#
#

## set

fruits = {"apple", "banana", "cherry"}
# print(fruits)

fruits = {"apple", "banana", "cherry", "apple"}
# print(fruits)

fruits.add("pear")

# print(fruits)

# fruits.remove("banana")

print(fruits)
