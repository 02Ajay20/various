print("Este algoritmo saca los promedios de los numeros pares e impares por aparte")
iteraciones_par = int(input("cuantos pares desea digitar: "))
suma_par = 0
suma_impar = 0
contador_par = 0
contador_impar = 0

for i in range(1,iteraciones_par+1):
  user_number = int(input("Escribe un numero: "))
  if user_number % 2 == 0:
    suma_par = user_number + suma_par
    contador_par += 1
  
  if user_number % 2 != 0:
    suma_impar = user_number + suma_impar
    contador_impar += 1

if suma_par != 0:
  promedio_par = suma_par/contador_par
  print(f"\nEl promedio de la suma de los pares ({suma_par}) es: {promedio_par}")
else:
  print("No escribiste numeros pares")
if suma_impar != 0:
  promedio_impar = suma_impar/contador_impar
  print(f"El promedio de la suma de los impares ({suma_impar}) es: {promedio_impar}")
else:
  print("No escribiste numeros impares")