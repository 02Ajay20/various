print("Cual es la tabla de multiplicar de un numero? con este algoritmo lo sabras")
user_number = int(input("Ingrese un numero: "))
multiplicador = 1

print(f"\nLa tabla del {user_number} es:")
for i in range(0,9):
  resultado = user_number * multiplicador
  print(f"{user_number} x {multiplicador} = {resultado}")
  multiplicador += 1