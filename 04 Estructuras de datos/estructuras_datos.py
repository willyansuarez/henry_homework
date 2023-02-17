
## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla
ciudades = ['Caracas', 'Tokio', 'París', 'Bankok', 'Munich', 'Roma']
# print(ciudades)


# 2) Imprimir por pantalla el segundo elemento de la lista
# print(ciudades[1])


# 3) Imprimir por pantalla del segundo al cuarto elemento
# print(ciudades[1:4])


# 4) Visualizar el tipo de dato de la lista
# print(type(ciudades))


# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento
# print(ciudades[2:])


# 6) Visualizar los primeros 4 elementos de la lista
# print(ciudades[:4])


# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?
ciudades.append('Tokio')
ciudades.append('Praga')
# print(ciudades)
# No arroja error, si el elemento existe, sale duplicado


# 8) Agregar otra ciudad, pero en la cuarta posición
ciudades.insert(3, 'Taiwan')
# print(ciudades)


# 9) Concatenar otra lista a la ya creada
mas_ciudades = ['Toronto', 'Moscow', '', 'Lisboa']
ciudades.extend(mas_ciudades)
# print(ciudades)
# mas_ciudades = ['Toronto', 'Moscow', '', 'Lisboa']


# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?
# print(ciudades.index('Tokio'))
# Arroja la primera coincidencia no el índice que se agregó duplicado


# 11) ¿Qué pasa si se busca un elemento que no existe?
# print(ciudades.index('El Cairo'))
# Buscando por el índice, arroja un error si no existe
# print('El Cairo' in ciudades)


# 12) Eliminar un elemento de la lista
# ciudades.remove('Moscow')
# print(ciudades)


# 13) ¿Qué pasa si el elemento a eliminar no existe?
# Arroja un error


# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo
# borrado = ciudades.pop()
# print(borrado)


# 15) Mostrar la lista multiplicada por 4
# print(ciudades * 4)
# print(ciudades)

# 16) Crear una tupla que contenga los números enteros del 1 al 20
# numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 10, 5, 150, -45, 5)
# print(numeros)
# print(type(numeros))
# tupla = range(1, 21)
# print(tupla)
# print(type(tupla))


# 17) Imprimir desde el índice 10 al 15 de la tupla
# print(numeros[10:16])


# 18) Evaluar si los números 20 y 30 están dentro de la tupla
# print(20 in numeros)
# print(30 in numeros)


# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.
# ciudad = 'Grecia'
# if ciudad in ciudades:
#     print(f"El elemento existe en la lista")
# else:
#     ciudades.append(ciudad)
#     print(f"Se agregó la ciudad {ciudad}")
# print(ciudades)


# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista
# print(ciudades.count('Tokio'))
# print(numeros.count(5))


# 21) Convertir la tupla en una lista
# nueva_lista = list(numeros)
# print(nueva_lista)

# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables
# num1, num2, num3 = numeros[:3]
# print(num1)
# print(num2)
# print(num3)


# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".
dict_mundo = {
    'Ciudades' : ciudades,
    'Pais' : ['Venezuela', 'Francia', 'Tailandia', 'Rusia', 'Italia', 'Alemania'],
    'Continente' : ['América', 'Oceanía', 'Europa', 'Äfrica', 'Asia']
}


# 24) Imprimir las claves del diccionario
# print(dict_mundo.keys())


# 25) Imprimir las ciudades a través de su clave
print(dict_mundo['Ciudades'])


# 24) Imprimir los valores del diccionario
# print(dict_mundo.values())