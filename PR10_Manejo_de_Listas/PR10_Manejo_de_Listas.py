print(" ")
print("Dylan Aaron Elicserio Marínez 3°W")
print(" ")
thislist = ["apple", "banana", "cherry"]
print(thislist)


#cuando usamos (len( )) te despliega
#el numero de elementos de la lista
thislist2 = ["apple", "banana", "cherry"]
print(len(thislist))


#Separa con un espacio
print(" ")
#Da valores a varias listas
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]


#Muestra los miembros de cada lista
print(list1)
print(list2)
print(list3)
print(list4)
print(" ")
thislist = ["apple", "banana", "cherry"]


#Muestra el miembro 1 y comienza en Cero 0
print(thislist[1])

#Muestra el ultimo miembro de la lisa
print(thislist[-1])

# el 2:5 muestra a patir de la posicion 2 a la 5 de los miembros de la lista
# entendiendo que la posicion que tiene apple es 0 cero
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


#Agregando miembros
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


#Agregando en la segunda posicion
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)




#Quitando banana de la lista
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Quitando una de las dos bananas de la lista
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#borrando al segundo miembro
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Borrando al ultimo miembro
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#Borrando al primer miembro
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#Agregando en la segunda posicion un miembro
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#Agregando elementos de tropical a la lista
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


#Agregando Tuplas a lista
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
