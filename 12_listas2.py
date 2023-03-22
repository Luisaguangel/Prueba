num = [99, 34, 25, 56, 72]
print(num)
num[1] = 88
print(num)
#num=[99, 88, 25, 56, 72]
# Función Insert. Insertar un nuevo valor en la ubicación que solicite
num.insert(1, 77)
print(num)
# Función append. Adicionar valores a una lista
num.append(100)
print(num)
# Función extend. Adicionar una lista
num2 = [9, 8, 7]
num.extend(num2)
print(num)
# REMOVE. Eliminar elementos de una lista
#num = [99, 77, 88, 25, 56, 72,100, 9, 8, 7]
num.remove(100)
print(num)
#Funciónn POP: Para eliminar npumero se debe indicar indice. Si no se indica automaticamente elimina el ultimo número
num.pop()
print(num)
#Función Delete
del num[0]
print(num)
#Función clear
num2.clear()
print(num2)
