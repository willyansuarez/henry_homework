# Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero
# numero = 5
# if numero > 0:
#     print("El número es mayor que cero")
# elif numero < 0:
#     print("El número es menor que cero")
# else:
#     print("El número es igual a cero")


# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato
# var_1 = '10'
# var_2 = 'diez'
# if type(var_1) == type(var_2):
#     print("Las variables son del mismo tipo")
# else:
#     print("Las variables no son del mismo tipo")
    

# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
# num = int(input("Introduce un número del 1 al 20\n"))
# if num % 2 == 0:
#     print("El valor es par")
# else:
#     print("El valor es impar")

# for x in range(1, 21):
#     if x % 2 == 0:
#         print(f"El numero {x} es par")
#     else:
#         print(f"El numero {x} es impar")
    
    
# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3
# for i in range(0, 6):
#     potencia = i ** 3
#     print(f"El numero {i} elevado a la potencia 3 es: {potencia}")
    

# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos
# entero = 6
# for i in range(0, entero):
#     # print(f"Esta es la iteracion {i}")
#     pass
# print(i)

# 6) Utilizar un ciclo while para realizar el factorial de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0
# import time
# num_fact = 5
# factorial = 1
# contador = 1
# while contador <= num_fact:
#     if num_fact == 0:
#         res_factorial = 1
#         break
#     else:
#         print(f"El factorial en este paso vale {factorial}")
#         time.sleep(2)
#         print(f"El contador en este paso vale {contador}")
#         (time.sleep(2))
#         factorial = factorial * contador
#         print(f"Ahora el factorial vale {factorial}")
#         time.sleep(2)
#         contador += 1
#         print(f"Ahora el contador vale {contador}")
#         time.sleep(2)
# print(f"El factorial de {num_fact} es {factorial}")


# factorial = 1
# a = 8
# if type(a) == int:
#     if a > 0:
#         a_original = a
#         while a > 1:
#             factorial = factorial * a
#             a -= 1
#         print(f"El factorial de {a_original} es {factorial}")
#     else:
#         print("La variable debe ser mayor a 0")
# else:
#     print("La variable debe ser un numero entero")


# 7) Crear un ciclo for dentro de un ciclo while
# n = 0
# while n < 5:
#     n += 1
#     for i in range(1, n):
#         print(f"Ciclo while nro {n}")
#         print(f"Ciclo for nro {i}")


# 8) Crear un ciclo while dentro de un ciclo for
# n = 5
# for i in range(1, n):
#     while n < 5:
#         n -= 1
#         print(f"Ciclo while nro {n}")
#         print(f"Ciclo for nro {i}")
        
        
# 9) Imprimir los números primos existentes entre 0 y 30
# cont = 0
# numero = 30
# for n in range(1, numero + 1):
#     for d in range(1, n + 1):
#         if n % d == 0:
#             cont += 1
#     if cont == 2:
#         print(f"{n} es primo.")
#     cont = 0
# print("Fin")


# for nro in range(0, 31):
#     es_primo = True
#     for i in range(2, nro):
#         if nro % i == 0:
#             es_primo = False
#     if es_primo:
#         print(f"{nro} es primo")


# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin
# cant_ciclos = 0
# for nro in range(0, 31):
#     es_primo = True
#     for i in range(2, nro):
#         cant_ciclos += 1
#         if nro % i == 0:
#             es_primo = False
#             break
#     if es_primo:
#         print(f"{nro} es primo")
# print(f"{cant_ciclos} cantidad de ciclos")


# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?



# 12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?
# Si



# 13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300
# Para saber si es divisible entre 12 el resto de la division entre 3 y 4 debe ser 0
# rango = 100
# while rango <= 300:
#     # print(rango)
#     if rango % 3 == 0 and rango % 4 == 0:
#         print(f"El {rango} es divisible entre 12")
#     else:
#         rango += 1
#         continue
#     rango += 1

# n = 99
# while n <= 300:
#     n += 1
#     if n % 12 != 0:
#         continue
#     print(f"{n} es divisible por 12")


# 14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente
# jugar = True
# while jugar == True:
#     num_primo = int(input("Ingresa un numero para saber si es primo\n"))
#     if num_primo / num_primo == 1 and num_primo / 1 == num_primo:
#         print(f"El {num_primo} es primo")
#         resp = input(print(f"¿Desea introducir otro número? s / n\n"))
#         if resp == 's' or resp == 'S':
#             jugar = True
#     else:
#         print(f"Ejecución terminada")
#         break

n = int(input("Ingresa un número para saber si es primo\n"))
sigue = 1
primo = True
while sigue == 1:
    for div in range(2, n):
        if n % div == 0:
            primo = False
            break
    if primo:
        print(f"{n} es primo")
        print(f"¿Desea encontrar el siguiente número primo?\n")
        if input() != '1':
            print("Se finaliza el proceso")
            break
    else:
        primo = True
    n += 1



# 15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6
# rango = 100
# while rango <= 300:
#     if rango % 3 == 0 and rango % 6 == 0:
#         print(f"El {rango} es divisible entre 3 y múltiplo de 6")
#         break
#     rango += 1