print("El programa sumara los numeros que escribas, excepto si son negativos")

num_1 = float(input("Escribe el primer numero: "))
num_2 = float(input("Escribe el segundo numero: "))
num_3 = float(input("Escribe el tercer numero: "))
num_4 = float(input("Escribe el cuarto numero: "))

if num_1 < 0:
  num_1 = 0
if num_2 < 0:
  num_2 = 0
if num_3 < 0:
  num_3 = 0
if num_4 < 0:
  num_4 = 0

suma = num_1 + num_2 + num_3 + num_4
if suma == 0:
  print("Este programa no realiza sumas de numeros negativos, vuelve a intentarlo")
else:
  print(f"\nLa suma descartando los negativos es: {suma}")