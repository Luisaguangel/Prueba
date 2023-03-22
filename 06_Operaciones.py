#Operaciones Aritméticas
#Suma + , Resta - , Mutiplicación * , División /, División entera //, Residuo o Módulo % (lo que queda de la división), Potenciación **
# JERARQUIA = Primero se realizan operacione en (), después **, * /, + y -
number = int(input('Digite un número: '))
'''
print(f'la suma con 2 es: {number + 2}')
print(f'la resta con 2 es: {number - 2}')
print(f'la multiplicaión con 2 es: {number * 2}')
print(f'la división con 2 es: {number / 2}')
print(f'la división entera con 2 es: {number // 2}')
print(f'El residuo con 2 es: {number % 2}')
print(f'la potenciación con 2 es: {number ** 2}')
'''
#Operaciones de asignación
contador = 1
print(f'antes de += {contador}')
contador += 1  #Operador de asignación incremental
print(f'despues de += {contador}')
contador -= 1  #Operador de asignación decremental

number += 1
print(f'Al usar el operador incremental +=, el resultado es {number}')
number -= 1
print(f'Al usar el operador decremental -=, el resultado es {number}')
number *= 2
print(f'Al usar el operador *=, el resultado es {number}')
number /= 2
print(f'Al usar el operador /=, el resultado es {number}')
number //= 2
print(f'Al usar el operador //=, el resultado es {number}')
number %= 3
print(f'Al usar el operador %=, el resultado es {number}')
number **= 2
print(f'Al usar el operador **=, el resultado es {number}')
