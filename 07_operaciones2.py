#OPERACIONES RELACIONALES O DE COMPARACIÓN
# TRUE(1) / FALSE (0)
number = int(input('Digite un número: '))
print(number > 3)  # Pregunta si number es mayor que 3
print(number >= 3)  # Pregunta si number es mayor o igual que 3
print(number <= 3)  # Pregunta si number es menor o igual que 3
print(number < 3)  # Pregunta si number es menor que 3
print(number == 3)  # Pregunta si number es igual que 3
print(number != 3)  # Pregunta si number NO es igual que 3

# operaciones lógicas
print("Operaciones lógicas")
# CONJUNCIÓN (AND) (&); SI ALGÚN DATO ES FALSE TODO SERA False
print('Conjunción:')
print(False & False)
print(number > 3 and number < 10)

#DISYUNCIÓN (OR) (|); SI ALGÚN DATO ES TRUE TODO SERA True. Cuando todo los valores son falsos todo sera falso
print('Disyunción:')
print(False or False)
print(True or False)
print(number <= 3 or number >= 10)

#NEGACIÓN (NOT);
print('Negación:')
print(not (True))
print(not (number <= 3 or number >= 10))

#OR EXCLUSIVA (^); Va a ser falso cuando los valores ingresados sean los mismos
print('OR Exclusiva:')
print(True ^ True)
print(False ^ True)
print(False ^ False)
# Operaciones de contenido o de pertenencia (in); Pregunta si un valor se encuentra dentro de una variable
print('Operador in:')
Nombre = 'Luisa Guavita'
print('G' in Nombre)
