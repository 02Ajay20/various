print("Escribe un numero de tres cifras y el algoritmo te dira si la centecima es par o impar\n")

numero_texto = input("escribe un numero de 3 cifras: ")
numero = int(numero_texto)
centecima = numero // 100

if len(numero_texto) > 3:
  print("escribe un numero de 3 cifras por favor")
elif len(numero_texto) < 3:
  print("escribe un numero de 3 cifras por favor")
elif centecima % 2 == 0:
  print(f"La centecima es par")
else:
  print(f"La centecima es impar")