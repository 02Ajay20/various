#ejercicio1
def t1():
  n = int(input("digite n: "))
  x = 0
  y = 0
  signo = ""
  signo2 = ""

  f1 = 0
  f2 = 1
  s = 0

  for i in range(1,n+1):
    x +=1
    if x == 8:
      x = 1
    if x < 5:
      signo = "-"
    else:
      signo = "+"

    y += 1

    if y == 6:
      y = 1
    if y < 3:
      signo2 = "+"
    else:
      signo2 = "-"

    f = 1
    for h in range(1,i+1):
      f = f*h
      
    print(signo,f1, "/", signo2, i,"!", f)
    
    s = f1 + f2
    f1 = f2
    f2 = s
# t1()
#ejercicio2
def t2():
  n = int(input("escriba n: "))
  hombre = 0
  mujer = 0
  manana = 0
  tarde = 0
  noche = 0

  contH = 0
  contM = 0
  contMn = 0
  contT = 0
  contN = 0
  for i in range(1,n+1):
    geevvvvhehst = int(input("digite es numero: "))

    g = geevvvvhehst//100000000000
    ee = (geevvvvhehst//1000000000)%100
    vvvv = (geevvvvhehst//100000)%10000
    he = (geevvvvhehst//1000)%100
    hs = (geevvvvhehst//10)%100
    t = geevvvvhehst%10

  

    hora = hs - he
    pago = vvvv * hora
    
    if g == 1:
      contM += 1
      mujer = mujer + pago
    if g == 2:
      contH += 1
      hombre = hombre + pago
    if t == 1:
      contMn += 1
      manana = manana + pago
    if t == 2:
      contT += 1
      tarde = tarde + pago
    if t == 3:
      contN += 1
      noche = noche + pago

  if contM != 0:
      promedio = mujer/contM
      print("promedio mujeres",promedio)
  if contH != 0:
    promedio = hombre/contH
    print("promedio hombres",promedio)
  if contMn != 0:
    promedio = manana/contMn
    print("promedio manana",promedio)
  if contT != 0:
    promedio = tarde/contT
    print("promedio tarde",promedio)
  if contN != 0:
    promedio = noche/contN
    print("promedio noche",promedio)
# t2()
#ejercicio3
def t3():
  hora = int(input("Introduce las horas en formato HHMMSSNN: "))

  h = hora//1000000
  m = (hora//10000)%100
  s = (hora//100)%100
  n = hora%100

  sm = n
  s = s + n

  if s > 119:
    m += 2
    s = s % 120
  if s > 59:
    m += 1
    s = s % 60
  if m > 59:
    h += 1
    m = m % 60
  if h > 23:
    h = 0

  print("La hora",sm,"segundos despues es:",h,m,s)
# t3()