n = int(input("numero: "))
counter = 0
primes = []

for i in range(1,n+1):
  c = i
  counter = 0
  for j in range(1,i+1):
    if i % c == 0:
      counter += 1
    c -= 1
  if counter == 2:
    primes.append(i)

print(primes)