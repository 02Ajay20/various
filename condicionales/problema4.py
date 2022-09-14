print('''Digita 2 numeros y si la suma de estos es negativa obtendras el promedio de esta
si es positiva te dira si la suma es par o impar
''')

num_1 = int(input("escribe un numero: "))
num_2 = int(input("escribe otro numero: "))

suma = num_1 + num_2
average = (num_1 + num_2) / 2

if suma < 0:
  print(f"El promedio de {num_1} y {num_2} es: {average}")
elif suma % 2 == 0:
  print(f"La suma es: {suma}")
  print(f"La suma de {num_1} + {num_2} es par")
elif suma % 2 != 0:
  print(f"La suma es: {suma}")
  print(f"La suma de {num_1} + {num_2} es impar")