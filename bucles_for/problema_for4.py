print("Este algoritmo te dice el pormedio de los numeros que digites")
iteracion = int(input("Cuantos numeros desea digitar: "))
suma = 0
contador = 0

for i in range(1,iteracion+1):
  user_num = int(input("Escriba un numero: "))
  suma = user_num + suma
  contador += 1

promedio = suma/contador
print(f"El promedio de {suma} es: {promedio}")