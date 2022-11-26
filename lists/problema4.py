numeros = []
factoriales = []

n = int(input("cantidad de numeros: "))

for i in range(0,n):
  x = int(input("digitar numero: "))
  numeros.append(x)

for j in range(0,n):
  factorial = 1
  for f in range(1,numeros[j]+1):
    factorial *= f
  factoriales.append(factorial)

print(f"{numeros}\n{factoriales}")