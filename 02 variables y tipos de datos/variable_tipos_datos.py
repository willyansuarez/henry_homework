
## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
numero = 8
print(numero)


# 2) Imprimir el tipo de dato de la constante 8.5
# numero_float = 8.5
# print(type(numero_float))
print(type(8.5))


# 3) Imprimir el tipo de dato de la variable creada en el punto 1
print(type(numero))


# 4) Crear una variable que contenga tu nombre
nombre = 'Willian'


# 5) Crear una variable que contenga un número complejo
numero_complejo = 5 + 4j


# 6) Mostrar el tipo de dato de la variable crada en el punto 5
print(type(numero_complejo))



# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
numero_pi = 3.1415926535897932384626433832795
print(round(numero_pi, 4))


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
verdadero = True
verdadero_palabra = 'True'
# No son lo mismo


# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8
print(type(verdadero))
print(type(verdadero_palabra))


# 10) Asignar a una variable, la suma de un número entero y otro decimal
total = 5 + 10.84
print(total)

# 11) Realizar una operación de suma de números complejos
suma_compleja1 = 4 + 2j
suma_compleja2 = 5 + 9j
print(suma_compleja1 + suma_compleja2)


# 12) Realizar una operación de suma de un número real y otro complejo
suma_real_compl = 12.54 + 4j
print(suma_real_compl)


# 13) Realizar una operación de multiplicación
producto = 4 * 5


# 14) Mostrar el resultado de elevar 2 a la octava potencia
potencia = 2 ** 8
print(potencia)


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
cociente = 27 / 4
print(cociente)


# 16) De la división anterior solamente mostrar la parte entera
entero = 27 // 4
print(entero)


# 17) De la división de 27 entre 4 mostrar solamente el resto
resto = 27 % 4
print(resto)


# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
resultado = entero * 4 + resto
print(resultado)


# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
saludo = 'Hola '
nombre = 'Willian'
print(saludo + nombre)


# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
print("2" == 2)
# Esto ocurre porque los tipos de datos son diferentes, uno es string o cadena y el otro entero


# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
print(int("2") == 2)


# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
# a = float('3,8')
# print(a)
# El error es la coma, enprogramación se usa el punto como separador decimal


# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
numero3 = 3
print(numero3)
numero3 -= 1
print(numero3)


# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
print(1 << 2)


# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
# print(2 + '2')
# El error es que no se puede sumar enteros con string, aunque fueran del mismo tipo da resultados
# diferentes, si fueran enteros el resultado es 4, en cambio si fueran string las
# concatenaria y el resultado sería '22'


# 26) Realizar una operación válida entre valores de tipo entero y string
numero_cadena = '5'
numero_entero = 15
suma_tipos_diferentes = int(numero_cadena) + numero_entero
print(suma_tipos_diferentes)

print('hola' * 3)