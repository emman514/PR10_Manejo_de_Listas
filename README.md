# PR10_Manejo_de_Listas
actividad en clase

print(" ")

print("Castruita Soto Emmanuel 3°W")

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
![image](https://github.com/user-attachments/assets/1b93ad10-be20-4531-ac15-04d720374cc2)
![image](https://github.com/user-attachments/assets/b43351fb-abfa-4099-90bb-b09a33e2de4f)
![image](https://github.com/user-attachments/assets/1915983c-1bfd-497d-a3db-1d4e271c0f74)
![image](https://github.com/user-attachments/assets/2c0e79a8-c74c-4126-939e-ec65610a26a9)

#Codigo 2

print(" ")

print("Dylan Aaron Elicserio Marínez 3°W")

print(" ")

# Manejo de listas en Python

# 1. Creación de una lista

frutas = ['manzana', 'naranja', 'plátano', 'fresa']

print("Lista inicial de frutas:", frutas)

# 2. Acceso a elementos de la lista

primera_fruta = frutas[0]  # Accede al primer elemento

print("La primera fruta es:", primera_fruta)

# 3. Modificación de elementos

frutas[1] = 'kiwi'  # Cambia 'naranja' por 'kiwi'

print("Lista de frutas después de la modificación:", frutas)

# 4. Agregar elementos

frutas.append('mango')  # Agrega 'mango' al final de la lista

print("Lista de frutas después de agregar un elemento:", frutas)

# 5. Insertar elementos en una posición específica

frutas.insert(2, 'piña')  # Inserta 'piña' en la posición 2

print("Lista de frutas después de insertar un elemento:", frutas)

# 6. Eliminar elementos

frutas.remove('fresa')  # Elimina 'fresa' de la lista

print("Lista de frutas después de eliminar un elemento:", frutas)

# 7. Eliminar un elemento por su índice

fruta_eliminada = frutas.pop(0)  # Elimina y devuelve el primer elemento

print("Elemento eliminado:", fruta_eliminada)

print("Lista de frutas después de eliminar por índice:", frutas)

# 8. Longitud de la lista

longitud = len(frutas)  # Obtiene la longitud de la lista

print("Número de frutas en la lista:", longitud)

# 9. Iterar sobre la lista

print("Frutas en la lista:")

for fruta in frutas:

    print(fruta)

# 10. Ordenar la lista

frutas.sort()  # Ordena la lista alfabéticamente

print("Lista de frutas ordenada:", frutas)

# 11. Invertir la lista

frutas.reverse()  # Invierte el orden de la lista

print("Lista de frutas invertida:", frutas)

# 12. Copiar una lista

frutas_copia = frutas.copy()  # Crea una copia de la lista

print("Copia de la lista de frutas:", frutas_copia)

# 13. Comprobar la existencia de un elemento

if 'mango' in frutas:

    print("El mango está en la lista.")
    
else:

    print("El mango no está en la lista.")

![image](https://github.com/user-attachments/assets/6a6fdd8d-1e0c-4364-a02b-c090887a61f3)
![image](https://github.com/user-attachments/assets/abb39f8d-c18c-42b1-9a4b-ecc06b65df1d)
![image](https://github.com/user-attachments/assets/5a1f2c78-e931-4a09-8651-1a5e63521e01)


