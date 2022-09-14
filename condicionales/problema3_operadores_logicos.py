print("Digita un numero y este se escribira en letras\n")

numero_texto = input("escribe un numero de tres cifras: ")
numero = int(numero_texto)

if len(numero_texto) > 3 or len(numero_texto) < 3:
  print("escribe un numero de 3 cifras por favor")

num_a = numero // 100
num_a_resuduo = numero % 100
num_b = num_a_resuduo // 10
num_c = num_a_resuduo % 10

if num_a == 1 or num_b == 1 or num_c == 1:
  print("uno")
if num_a == 2 or num_b == 2 or num_c == 2:
  print("dos")
if num_a == 3 or num_b == 3 or num_c == 3:
  print("tres")
if num_a == 4 or num_b == 4 or num_c == 4:
  print("cuatro")
if num_a == 5 or num_b == 5 or num_c == 5:
  print("cinco")
if num_a == 6 or num_b == 6 or num_c == 6:
  print("seis")
if num_a == 7 or num_b == 7 or num_c == 7:
  print("siete")
if num_a == 8 or num_b == 8 or num_c == 8:
  print("ocho")
if num_a == 9 or num_b == 9 or num_c == 9:
  print("nueve")
if num_a == 0 or num_b == 0 or num_c == 0:
  print("cero")