n = int(input("ingrese el numero de usuarios: "))

suma_h = 0
suma_h50 = 0
suma_j = 0
suma_j30 = 0
contador_h = 0
contador_h50 = 0
contador_j = 0
contador_j30 = 0

for i in range(1,n+1):
  vvvvgeehehs = int(input("ingresa los datos del usuario: "))

  valorhora = vvvvgeehehs // 10000000
  geehehs = vvvvgeehehs % 10000000
  genero = geehehs //1000000
  eehehs = geehehs % 1000000
  edad = eehehs // 10000
  hehs = eehehs % 10000
  he = hehs // 100
  hs = hehs % 100
  hora_f = hs - he
  print(valorhora,genero,edad,he,hs)

  if genero == 1:
    if edad < 30:
      pago = valorhora * hora_f
      suma_j30 += pago
      contador_j30 += 1
    else:
      pago = valorhora * hora_f
      suma_j += pago
      contador_j += 1
  if genero == 2:
    if edad > 50:
      pago = valorhora * hora_f
      suma_h50 += pago
      contador_h50 += 1
    else:
      pago = valorhora * hora_f
      suma_h += pago
      contador_h += 1

if contador_j != 0:
  promedio_j = suma_j/contador_j
  print("promedio mujeres", promedio_j)
if contador_j30 != 0:
  promedio_j30 = suma_j30/contador_j30
  print("promedio mujeres menores de 30", promedio_j30)
if contador_h != 0:
  promedio_h = suma_h/contador_h
  print("promedio hombres", promedio_h)
if contador_h50 != 0:
  promedio_h50 = suma_h50/contador_h50
  print("promedio hombres mayores de 50", promedio_h50)
else:
  print("no se puede dividir por 0")
