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
