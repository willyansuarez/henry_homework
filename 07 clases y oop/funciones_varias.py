
# # Pregunta 5
# class FuncionesVarias:
#     def __init__(self) -> None:
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




# Pregunta 6
class FuncionesVarias:
    def __init__(self, lista_num):
        self.lista_num = lista_num


    def verificar_primo(self):
        for i in self.lista_num:
            if self.__verificar_primo(i):
                print(f"El elemeto {i} si es un número primo")
            else:
                print(f"El elemeto {i} no es un número primo")

    def factorial(self):
        for i in self.lista_num:
            print(f"El factorial de {i} es {self.__factorial(i)}")
        
        
    def __factorial(self, num):
        factorial = 1
        if type(num) == int:
            if num > 0:
                num_original = num
                while num > 1:
                    factorial = factorial * num
                    num -= 1
                return factorial
            else:
                return f"La variable debe ser mayor a 0"
        else:
            return f"La variable debe ser un numero entero"

    def conversion_grados(self, valor, origen, destino):
        for i in self.lista_num:
            print(f"{i} grados {origen} son {self.__conversion_grados(i, origen, destino)} grados {destino}")
            
    def __conversion_grados(self, valor, origen, destino):
        cel_far = (valor * 1.8) + 32
        cel_kel = valor + 273.15
        far_cel = (valor - 32) * 5 / 9
        far_kel = 5 / 9 * (valor - 32) + 273.15
        kel_far = 1.8 * (valor - 273.15) + 32 
        kel_cel = valor - 273.15 

        if origen == 'Cel' and destino == 'Far':
            resultado = cel_far
        elif origen == 'Cel' and destino == 'Kel':
            resultado = cel_kel
        elif origen == 'Far' and destino == 'Cel':
            resultado = far_cel
        elif origen == 'Far' and destino == 'Kel':
            resultado = far_kel
        elif origen == 'Kel' and destino == 'Far':
            resultado = kel_far
        else:
            resultado = kel_cel

        return resultado

    def maximo_repetido(self, lista_num):
        maximo = 0
        num_maximo = 0
        for num in lista_num:
            num_repetido = lista_num.count(num)
            if num_repetido > maximo:
                maximo = num_repetido
                num_maximo = num
        
        return num_maximo, maximo
    
    def __verificar_primo(self, numero):
        if numero == 0:
            return f"El {numero} es 0"
        elif numero == 2 or numero == 3:
            return f"El {numero} es primo."
        else:
            for div in range(2, int(numero / 2) + 1):
                if numero % div == 0:
                    return False
        return True