#4/2 +0! 16/4 +1! 36/6 +1! 64/10 -2! 100/16 -3!

n = int(input("Digete n: "))

signo = ""
termino = ""
contador = 0

f1 = 0
f2 = 1
s = 0

a = 0
b = 2
c = 0

v = 4
x = 4
y = 5
z = 4

for i in range(1,n+1):
  if i % 2 == 0:
    contador += 1
    if contador == 6:
      contador =1
    if contador < 4:
      signo = "+"
    if contador >= 4:
      signo = "-"
    f = 1
    for j in range(1,f1+1):
      f = f*j
    termino = signo+str(f1)+" "+str(f)
    s = f1 + f2
    f1 = f2
    f2 = s
    
  else:
    c = a + b
    a = b
    b = c
    termino = str(z)+"/"+str(c)
    z = x * v
    v = v + y
    y = y + 2

  print(termino)