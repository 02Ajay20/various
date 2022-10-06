print("Traductor de numeros (menores a 257) de Decimal a Binario")
user_number = int(input("escribe el numero que deseas convertir: "))
cosiente = 1

if user_number < 257:
  for i in range(1,user_number+1):
    if cosiente != 0:
      cosiente = user_number // 2
      modulo = user_number % 2
      print(modulo)

      user_number = cosiente
else:
  print("el numero tiene que ser menor a 257")

print("Para que tu numero se lea bien tienes que leerlo de abajo hacia arriba")