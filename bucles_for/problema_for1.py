print("Descubre cuales son los Multiplos de un numero")
user_number = int(input("Ingrese un numero: "))
iteraciones = int(input(f"cuantos multiplos de ({user_number}) quiere ver: "))
x = 1

for i in range(1,iteraciones+1):
  multiplo = user_number * x
  x += 1
  print(multiplo)