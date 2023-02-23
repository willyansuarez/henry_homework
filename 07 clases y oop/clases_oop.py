# ## Clases y Programación Orientada a Objetos

# 1) Crear la clase vehículo que contenga los atributos:
# Color
# Si es moto, auto, camioneta ó camión
# Cilindrada del motor
# class Vehiculo:
#     def __init__(self, color, tipo, cilindrada):
#         self.color = color
#         self.tipo = tipo
#         self.cilindrada = cilindrada


# 2) A la clase Vehiculo creada en el punto 1, agregar los siguientes métodos:
# Acelerar
# Frenar
# Doblar
class Vehiculo:
    def __init__(self, tipo, color, cilindrada):
        self.color = color
        self.tipo = tipo
        self.cilindrada = cilindrada
        self.__velocidad = 0
        self.direccion = 0


    # Métodos
    # def acelerar(self):
    #     return f"El vehículo {self.tipo} está acelerando"

    # def frenar(self):
    #     return f"El vehículo {self.tipo} está frenando"

    # def doblar(self):
    #     return f"El vehículo {self.tipo} está doblando"

    # def estado(self, velocidad, direccion):
    #     return f"El vehículo {self.tipo} va a {velocidad} kilómetros y va en direccion {direccion}"

    # def info_vehiculo(self):
    #     return f"El vehículo {self.tipo} es de color {self.color} y de {self.cilindrada} cilindros"
        
    def acelerar(self, vel):
        self.__velocidad += vel

    def frenar(self, vel):
        self.__velocidad -= vel

    def doblar(self, grados):
        self.direccion += grados

    def estado(self, velocidad, direccion):
        return f"Velocidad {self.__velocidad} direccion {self.direccion}"
    
    def detalle(self):
        return f"Soy {self.tipo} de color {self.color} y mi cilindrada es {self.cilindrada}"
    
    def devolver_velocidad(self):
        return self.__velocidad
    

v1 = Vehiculo('auto', 'rojo', 8)
v2 = Vehiculo('camión', 'gris', 16)
v3 = Vehiculo('camioneta', 'verde', 8)
print(v1.detalle())
print(v2.detalle())
print(v3.detalle())


v1.acelerar(30)
print(v1.devolver_velocidad())

# Esto no daba error, pero sel le agregó dos guión bajo a la variable para que no se pudiera acceder desde la instancia sino dentro de la clase
# print(v1.velocidad)

# print(f"{v1.tipo} de color {v1.color} y {v1.cilindrada} de cilindrada")
# print(f"{v2.tipo} de color {v2.color} y {v2.cilindrada} de cilindrada")
# print(f"{v3.tipo} de color {v3.color} y {v3.cilindrada} de cilindrada")


# 3) Instanciar 3 objetos de la clase vehículo y ejecutar sus métodos, probar luego el resultado
# print(v1.acelerar())
# print(v1.frenar())
# print(v1.doblar())

# print(v2.acelerar())
# print(v2.frenar())
# print(v2.doblar())

# print(v3.acelerar())
# print(v3.frenar())
# print(v3.doblar())


# 4) Agregar a la clase Vehiculo, un método que muestre su estado, es decir, a que velocidad se encuentra y su dirección. Y otro método que muestre color, tipo y cilindrada
# print(v1.info_vehiculo())
# print(v1.estado(45, 'oeste'))
# print(v2.info_vehiculo())
# print(v2.estado(60, 'norte'))
# print(v3.info_vehiculo())
# print(v3.estado(63, 'este'))


# 5) Crear una clase que permita utilizar las funciones creadas en la práctica del módulo 6
# Verificar Primo
# Valor modal
# Conversión grados
# Factorial
# class FuncionesVarias:
#     def __init__(self):
#         pass


#     def verificar_primo(self, numero):
#         if numero == 0:
#             return f"El {numero} es 0"
#         elif numero == 2 or numero == 3:
#             return f"El {numero} es primo."
#         else:
#             for div in range(2, int(numero / 2) + 1):
#                 if numero % div == 0:
#                     return False
#         return True

#     def factorial(self, num):
#         factorial = 1
#         if type(num) == int:
#             if num > 0:
#                 num_original = num
#                 while num > 1:
#                     factorial = factorial * num
#                     num -= 1
#                 return f"El factorial de {num_original} es {factorial}"
#             else:
#                 return f"La variable debe ser mayor a 0"
#         else:
#             return f"La variable debe ser un numero entero"


#     def conversion_grados(self, valor, origen, destino):
#         cel_far = (valor * 1.8) + 32
#         cel_kel = valor + 273.15
#         far_cel = (valor - 32) * 5 / 9
#         far_kel = 5 / 9 * (valor - 32) + 273.15
#         kel_far = 1.8 * (valor - 273.15) + 32 
#         kel_cel = valor - 273.15 

#         if origen == 'Cel' and destino == 'Far':
#             resultado = cel_far
#         elif origen == 'Cel' and destino == 'Kel':
#             resultado = cel_kel
#         elif origen == 'Far' and destino == 'Cel':
#             resultado = far_cel
#         elif origen == 'Far' and destino == 'Kel':
#             resultado = far_kel
#         elif origen == 'Kel' and destino == 'Far':
#             resultado = kel_far
#         else:
#             resultado = kel_cel

#         return resultado

#     def maximo_repetido(self, lista_num):
#         maximo = 0
#         num_maximo = 0
#         for num in lista_num:
#             num_repetido = lista_num.count(num)
#             if num_repetido > maximo:
#                 maximo = num_repetido
#                 num_maximo = num
        
#         return num_maximo, maximo

# 6) Probar las funciones incorporadas en la clase del punto 5

# 7) Es necesario que la clase creada en el punto 5 contenga una lista, sobre la cual se aplquen las funciones incorporadas

# 8) Crear un archivo .py aparte y ubicar allí la clase generada en el punto anterior. Luego realizar la importación del módulo y probar alguna de sus funciones
