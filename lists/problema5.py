numeros = []
ordenados = []
n = int(input("cuantos numeros quiere ingresar: "))

for i in range(1,n+1):
  x = int(input("escriba un numero: "))
  numeros.append(x)

# for dentro del for para que el numero se ponga en el lugar si es menor que el siguiente y mayor que el anterior
for i in range(0, n):
  if i == 0:
    ordenados.append(numeros[i])
  if i == 1:
    if numeros[i] >= ordenados[0]:
      ordenados.append(numeros[i])
    if numeros[i] < ordenados[0]:
      ordenados.insert(0, numeros[i])
      
  if i > 1:
    if numeros[i] > ordenados[i-1]:
      ordenados.append(numeros[i])
    elif numeros[i] < ordenados[0]:
      ordenados.insert(0, numeros[i])
    else:
      cont = 0
      for j in range(0,i-1):
        if cont == 0:
          if numeros[i] == ordenados[j]:
            ordenados.insert(j, numeros[i])
            cont += 1
        if numeros[i] < ordenados[j+1]:
          if numeros[i] > ordenados[j]:
            ordenados.insert(j+1, numeros[i])

print("el numero menor es",ordenados[0],"\nel numero mayor es",ordenados[n-1])