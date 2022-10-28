n = int(input("Ingrese n: "))
if n % 2 == 0:
  n = n // 2
else:
  n = (n // 2)+1

signo = ""
con = 0
x1 = 4
x2 = 6
s1 = 0

f1 = 0
f2 = 1
s2 = 0

contador = 0

for i in range(1,n+1):
  for h in range(1):
    #signos - +
    con += 1
    if con == 7:
      con = 1
    if con < 5:
      signo = "-"
    if con >= 5:
      signo = "+"
    #sucesion = 4 6 10 16 26..
    print(signo,x1)
    s1 = x1 + x2
    x1 = x2
    x2 = s1

  for y in range(1):
    #Factorial de Fibonacci
    f = 1
    for j in range(1,f1+1):
      f = f*j
    print(f1,f)
    #Fibonacci
    s2 = f1 + f2
    f1 = f2
    f2 = s2

