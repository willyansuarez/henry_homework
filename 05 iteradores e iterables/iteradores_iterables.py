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
# i = 0
# while i < len(num_negativos):
#     if num_negativos[i] % 2 == 0:
#         print(f"{num_negativos[i]} es par")
#     i += 1  


# Otra solución
# contador = -15
# while contador < 0:
#     if contador % 2 == 0:
#         print(f"{contador} es par")
#         contador += 1
#     else:
#         contador += 1
    

# 3) Resolver el punto anterior sin utilizar un ciclo while
# for x in num_negativos:
#     if x % 2 == 0:
#         print(x)


# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos
# prim_tres = iter(num_negativos)
# print(next(prim_tres))
# print(next(prim_tres))
# print(next(prim_tres))
# for numero in num_negativos[:3]:
#     print(numero)


# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento
# for i, c in enumerate(prim_tres): ó (prim_tres[:3])
#     # print(i, c)
#     if i == 2:
#         break

# for i, c in enumerate(prim_tres): ó (prim_tres[:3])
#     # print(i, c)
#     if i != 3:
#         print(i, c)
#     else:
#         break

# for i, c in enumerate(num_negativos):
#     print(i, c)



# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]
# lista = [1,2,5,7,8,10,13,14,15,17,20]
# aux = 1
# while aux <= 20:
#     if aux not in lista:
#         lista.insert((aux - 1), aux)
#     aux = aux + 1
# print(lista)

# lista = [1,2,5,7,8,10,13,14,15,17,20]
# for aux in range(1, 20):
#     if aux not in lista:
#         lista.insert((aux - 1), aux)
# print(lista)


# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula:
# n0 = 0
# n1 = 1
# ni = ni-1 + ni-2
# Crear una lista con los primeros treinta números de la sucesión.
# a = 0
# b = 1
# total = 0
# lista_fib = []
# for n in range(29):
#     # print(n)
#     a = b
#     b = total
#     total = a + b
#     lista_fib.append(total)
#     # print(total)
# print(lista_fib)

# fibo = [0, 1]
# n = 2
# while n < 30:
#     fibo.append(fibo[n-1] + fibo[n-2])
#     n += 1
# print(fibo)


# 8) Realizar la suma de todos elementos de la lista del punto anterior
# print(sum(lista_fib))
# print(sum(fibo))
      

# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:
# Donde i es la cantidad total de elementos
# ni-1 / ni
# ni-2 / ni-1
# ni-3 / ni-2
# ni-4 / ni-3
# ni-5 / ni-4
# primeros = 15
# n = primeros - 5
# while n < primeros:
#     print(fibo[n] / fibo[n-1])
#     n += 1

# n = 2
# while n < len(fibo):
#     print(fibo[n] / fibo[n-1])
#     n += 1


# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
# enes = [i for i in cadena if i == 'n']
# for l, e in enumerate(enes):
#     print(f"{l} - {e}")
# print(enes)
# print(len(enes))
# for indice, letra  in enumerate(cadena):
#     if letra == 'n':
#         print(f"{indice} - {letra}")


# 11) Crear un diccionario e imprimir sus claves utilizando un iterador
# mi_dicc = {
#     'nombre' : 'Willian',
#     'edad' : 50,
#     'profesión' : 'Ingeniero'
# }
# for clave in mi_dicc:
#     print(clave)


# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 
# lista_cadena = list(cadena)
# for i in lista_cadena:
#     print(i)

# lista3 = iter(lista_cadena)
# largo = len(lista3)
# for i in range(largo):
#     print(next(lista3))

# 13) Crear dos listas y unirlas en una tupla utilizando la función zip
# lista1 = [1, 2, 3, 4]
# lista2 = ['a', 'b', 'c', 'd']
# nueva_lista = zip(lista1, lista2)
# print(list(nueva_lista))


# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
# divisible_por7 = []
# for num in lis:
#     # print(num)
#     if num % 7 == 0:
#         divisible_por7.append(num)
    
# print(f"{divisible_por7} son divisibles por 7")


# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
# total = 0
# for elemento in lis:
#     if type(elemento) == list:
#         total = total + len(elemento)
#     else:
#         total += 1

# print(total)

# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es
# No funciona
# for elemento in lis:
#     if type(elemento) != list:
#         elemento = [elemento]
#         lis.insert(0,elemento)
# print(lis)

# for indice, elemento in enumerate(lis):
#     if (type(elemento) != list):
#         lis[indice]=[elemento]
# print(lis)