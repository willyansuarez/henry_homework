# ## Funciones

# 1) Crear una función que reciba un número como parámetro y devuelva si True si es primo y False si no lo es
# def es_primo(numero):
#     if numero == 0:
#         # print(f"El {numero} es 0")
#         return False
#     elif numero == 2 or numero == 3:
#         # print(f"El {numero} es primo.")
#         return True
#     else:
#         for div in range(2, int(numero / 2) + 1):
#             if numero % div == 0:
#                 return False
#     return True

# print(es_primo(91))

# Sin la funcion
# Solución video
# nro = 100
# es_primo = True
# for i in range(2, int(nro / 2) + 1):
#     if nro % i == 0:
#         es_primo = False
#         break
# return es_primo

# Esto es sin la funcion
# if es_primo:
#     print(f"El {nro} es primo")
# else:
#     print(f"El {nro} no es primo")


# def verifica_primo(nro):
#     es_primo = True
#     for i in range(2, int(nro / 2) + 1):
#         if nro % i == 0:
#             es_primo = False
#             break
#     return es_primo
    
# print(verifica_primo(85))

# 2) Utilizando la función del punto 1, realizar otra función que reciba de parámetro una lista de números y devuelva sólo aquellos que son primos en otra lista
# lista_primos = []
# def son_primos(lis):
#     for elemento in lis:
#         if elemento == 0:
#             continue
#         if elemento == 2 or elemento == 3:
#             lista_primos.append(elemento)
#         if elemento % 2 == 0:
#             continue
#         if elemento % 3 ==  0:
#             continue
#         if elemento % 5 ==  0:
#             continue
#         if elemento % 7 ==  0:
#             continue
#         if elemento % 11 ==  0:
#             continue
#         else:
#             lista_primos.append(elemento)
#     return lista_primos

# lista_numeros = [2, 59, 97, 85, 54, 23, 31, 89]
# print(son_primos(lista_numeros))

# Solución video
# def crea_lista_primos(lista_valores):
#     lista_2 = []
#     for elemento in lista_1:
#         if verifica_primo(elemento):
#             lista_2.append(elemento)
        
#     return lista_2
    
# lista_1 = list(range(2, 100))
# lista_p = (crea_lista_primos(lista_1))
# print(lista_p)


# 3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. Si hay más de un "más repetido", que devuelva cualquiera
# def repetido(lis):
#     dicc_repetidos = {}
#     for i, e in enumerate(lis):
#         rep = lis.count(e)
#         if rep not in dicc_repetidos.keys():
#             dicc_repetidos[e] = rep
#         else:
#             continue
    
#     return dicc_repetidos

# lista_numeros = [2, 59, 59, 85, 31, 59, 31, 2, 59, 31, 54]
# print(repetido(lista_numeros))

# Solucion 1 video (participante)
# def maximo_repetido(lista_num):
#     maximo = 0
#     num_maximo = 0
#     for num in lista_num:
#         num_repetido = lista_num.count(num)
#         if num_repetido > maximo:
#             maximo = num_repetido
#             num_maximo = num
    
#     return num_maximo, maximo
# lista_numeros = [2, 59, 59, 85, 31, 59, 31, 2, 59, 31, 54]
# result = maximo_repetido(lista_numeros)
# print(f"El número {result[0]} es el que se repite mas veces: {result[1]}")

# Solucion 2 video (profesor)
# def valor_modal(lista):
#     lista_unicos = []
#     lista_repeticiones = []
#     if len(lista) == 0:
#         return None
#     for elemento in lista:
#         if elemento in lista_unicos:
#             i = lista_unicos.index(elemento)
#             lista_repeticiones[i] += 1
#         else:
#             lista_unicos.append(elemento)
#             lista_repeticiones.append(1)
#     moda = lista_unicos[0]
#     maximo = lista_repeticiones[0]
#     for i, elemento in enumerate(lista_unicos):
#         if lista_repeticiones[i] > maximo:
#             moda = lista_unicos[i]
#             maximo = lista_repeticiones[i]
#     return moda, maximo

# lista_numeros = [2, 59, 59, 85, 31, 59, 31, 2, 59, 31, 54]
# moda, maximo = (valor_modal(lista_numeros))
# print(f"El valor {moda} es el que se repite mas veces: {maximo}")


# 4) A la función del punto 3, agregar un parámetro más, que permita elegir si se requiere el menor o el mayor de los mas repetidos.
# def valor_modal(lista, menor):
#     '''
#     Esta función calcula las veces que se repite un elemento
#     en una lista y recibe dos parámetros
#     1- Una lista de valores
#     2- Un booleano verdadero(por defecto) por si se requiere el mínimo de los mas repetidos o falso
#     '''
#     lista_unicos = []
#     lista_repeticiones = []
#     if len(lista) == 0:
#         return None
#     if menor:
#         lista.sort()
#     else:
#         lista.sort(reverse=True)
#     for elemento in lista:
#         if elemento in lista_unicos:
#             i = lista_unicos.index(elemento)
#             lista_repeticiones[i] += 1
#         else:
#             lista_unicos.append(elemento)
#             lista_repeticiones.append(1)
#     moda = lista_unicos[0]
#     maximo = lista_repeticiones[0]
#     for i, elemento in enumerate(lista_unicos):
#         if lista_repeticiones[i] > maximo:
#             moda = lista_unicos[i]
#             maximo = lista_repeticiones[i]
    
#     return moda, maximo

# lista_numeros = [2, 59, 59, 85, 31, 59, 31, 2, 59, 31, 54]
# # moda, maximo = (valor_modal(lista_numeros, True))
# moda, maximo = (valor_modal(lista_numeros, False))
# print(f"El valor {moda} es el que se repite mas veces: {maximo}")


# 5) Crear una función que convierta entre grados Celsius, Farenheit y Kelvin<br>
# Fórmula 1	: (°C × 9/5) + 32 = °F<br>
# Fórmula 2	: °C + 273.15 = °K<br>
# Debe recibir 3 parámetros: el valor, la medida de orígen y la medida de destino
# def conversion_temperatura(valor, origen, destino):
#     cel_far = (valor * 1.8) + 32
#     cel_kel = valor + 273.15
#     far_cel = (valor - 32) * 5 / 9
#     far_kel = 5 / 9 * (valor - 32) + 273.15
#     kel_far = 1.8 * (valor - 273.15) + 32 
#     kel_cel = valor - 273.15 

#     if origen == 'Cel' and destino == 'Far':
#         resultado = cel_far
#     elif origen == 'Cel' and destino == 'Kel':
#         resultado = cel_kel
#     elif origen == 'Far' and destino == 'Cel':
#         resultado = far_cel
#     elif origen == 'Far' and destino == 'Kel':
#         resultado = far_kel
#     elif origen == 'Kel' and destino == 'Far':
#         resultado = kel_far
#     else:
#         resultado = kel_cel

#     return resultado

# print(conversion_temperatura(32, 'Cel', 'Kel'))

# Solución video
def conversion_grados(valor, origen, destino):
    if origen == 'celsius':
        if destino == 'celsius':
            valor_destino = valor
        elif destino == 'farenheit':
            valor_destino = (valor * 9 / 5) + 32
        elif destino == 'kelvin':
            valor_destino = valor + 273.15
        else:
            'Parámetro de destno incorrecto'
    elif origen == 'farenheit':
        if destino == 'celsius':
            valor_destino = (valor - 32) * 5 / 9
        elif destino == 'farenheit':
            valor_destino = valor
        elif destino == 'kelvin':
            valor_destino = ((valor - 32) * 5 / 9) + 273.15
        else:
            'Parámetro de destno incorrecto'
    elif origen == 'kelvin':
        if destino == 'celsius':
            valor_destino = valor - 273.15
        elif destino == 'farenheit':
            valor_destino = (valor - 273.15) * 9 / 5 + 32 
        elif destino == 'kelvin':
            valor_destino = valor
        else:
            'Parámetro de destno incorrecto'
    
    return valor_destino

# print('1 grado celsius a celsius ', conversion_grados(1, 'celsius', 'celsius'))
# print('1 grado celsius a kelvin ', conversion_grados(1, 'celsius', 'kelvin'))
# print('1 grado celsius a farenheit ', conversion_grados(1, 'celsius', 'farenheit'))

# print('1 grado kelvin a kelvin ', conversion_grados(1, 'kelvin', 'kelvin'))
# print('1 grado kelvin a celsius ', conversion_grados(1, 'kelvin', 'celsius'))
# print('1 grado kelvin a farenheit ', conversion_grados(1, 'kelvin', 'farenheit'))

# print('1 grado farenheit a farenheit ', conversion_grados(1, 'farenheit', 'farenheit'))
# print('1 grado farenheit a kelvin ', conversion_grados(1, 'farenheit', 'kelvin'))
# print('1 grado farenheit a celsius ', conversion_grados(1, 'farenheit', 'celsius'))


# 6) Iterando una lista con los tres valores posibles de temperatura que recibe la función del punto 5, hacer un print para cada combinación de los mismos:
# def imprimir_temperatura():
#     print(conversion_temperatura(32, 'Cel', 'Far'))
#     print(conversion_temperatura(32, 'Cel', 'Kel'))
#     print(conversion_temperatura(32, 'Far', 'Cel'))
#     print(conversion_temperatura(32, 'Far', 'Kel'))
#     print(conversion_temperatura(32, 'Kel', 'Far'))
#     print(conversion_temperatura(32, 'Far', 'Kel'))

# imprimir_temperatura()

metricas = ['celsius', 'kelvin', 'farenheit']
for i in range(0, 3):
    for j in range(0, 3):
        print('1 grado', metricas[i], 'a', metricas[j], ':', conversion_grados(1, metricas[i], metricas[j]))


# 7) Armar una función que devuelva el factorial de un número. Tener en cuenta que el usuario puede equivocarse y enviar de parámetro un número no entero o negativo
# def factorial(num):
#     factorial = 1
#     if type(num) == int:
#         if num > 0:
#             num_original = num
#             while num > 1:
#                 factorial = factorial * num
#                 num -= 1
#             print(f"El factorial de {num_original} es {factorial}")
#         else:
#             print("La variable debe ser mayor a 0")
#     else:
#         print("La variable debe ser un numero entero")

# factorial(5)