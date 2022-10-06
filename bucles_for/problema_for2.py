print("Este algoritmo te muestra los divisores de un numero")
user_number = int(input("Escriba un numero: "))
divisor = 1

for i in range(1,user_number+1):
  if user_number % divisor == 0:
    print(divisor)

  divisor += 1