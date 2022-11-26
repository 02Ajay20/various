n = int(input("numero: "))
counter = 0
numeros = []
multiplos = []
primes = []

for i in range(1,n+1):
  x = int(input("escribe numeros: "))
  numeros.append(x)
  if i % 3 == 0:
    multiplos.append(x)
  c = x
  counter = 0
  for j in range(1,x+1):
    if x % c == 0:
      counter += 1
    c -= 1
  if counter == 2:
    primes.append(x)

print(f"numeros: {numeros}\nmultiplos de 3: {multiplos}\nprimos {primes}")