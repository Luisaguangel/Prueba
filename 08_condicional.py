# Condicional If; Else se traduce como sino en español. Se corta con espacio normal para indicar que la instrución termino.
# Elif hace referencia a una función SI anidada
adivinar = 50
numero = int(input('Sr usuario, digite un número: '))
if (numero > adivinar):
  print('Bajar')
elif (numero < adivinar):
  print('Subir')
else:
  print('Verdadero')

print('La instrucción IF terminó')

#If anidado 2
if (numero >= adivinar):
  if(numero > adivinar):
    print('coloque un número menor')
  else:
    print('Acertado')
else:
  print('coloque un número mayor')
print('La instrucción IF terminó')