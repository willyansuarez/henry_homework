## Iteradores e iterables

# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1
# num_negativos = []
# contador = -15
# while contador < 0:
#     num_negativos.append(contador)
#     contador += 1
# print(num_negativos)


# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?
# Si


# 3) Resolver el punto anterior sin utilizar un ciclo while
# for x in num_negativos:
#     if x % 2 == 0:
#         print(x)


# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos
# prim_tres = iter(num_negativos)
# print(next(prim_tres))
# print(next(prim_tres))
# print(next(prim_tres))


# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento
# for i, c in enumerate(prim_tres):
#     # print(i, c)
#     if i == 2:
#         break

# for i, c in enumerate(prim_tres):
#     # print(i, c)
#     if i != 3:
#         print(i, c)
#     else:
#         break


# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula:
# La sucesión de Fibonacci es un listado de números que sigue la fórmula:
# n0 = 0
# n1 = 1
# ni = ni-1 + ni-2
# Crear una lista con los primeros treinta números de la sucesión.


# 8) Realizar la suma de todos elementos de la lista del punto anterior

# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:
# Donde i es la cantidad total de elementos
# ni-1 / ni
# ni-2 / ni-1
# ni-3 / ni-2
# ni-4 / ni-3
# ni-5 / ni-4



# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"
cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
enes = [i for i in cadena if i == 'n']
# print(enes)
# print(len(enes))


# 11) Crear un diccionario e imprimir sus claves utilizando un iterador



# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 



# 13) Crear dos listas y unirlas en una tupla utilizando la función zip



# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es
