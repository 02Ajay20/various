n = int(input("Cantidad de usuarios a ingresar: "))
acumpago = 0
acumboni = 0
acumh = 0
acumm = 0

for i in range(1,n+1):
  x = int(input("ingrese el valor en formato hehsgteevvvv: "))
  he = x // 10000000000
  hs = (x // 100000000)%100
  g = (x // 10000000)%10
  t = (x // 1000000)%10
  e = (x // 10000)%100
  v = x % 10000
  print(he,hs,g,t,e,v)

  if g == 1:
    if e > 50:
      if t == 3:
        porcentaje = 0.3
      else:
        porcentaje = 0
    else:
      if e > 30:
        if t == 1:
          porcentaje = 0.2
        else:
          if t == 2:
            porcentaje = 0.2
          else:
            porcentaje = 0
      else:
        porcentaje = 0
      
  if g == 2:
    if e > 55:
      if t == 3:
        porcentaje = 0.2
      else:
        porcentaje = 0
    else:
      porcentaje = 0
  #else

      
  subtotal = (hs-he)*v
  boni = subtotal * porcentaje
  tpago = subtotal + boni

  acumpago = acumpago + tpago
  acumboni = acumboni + boni
  if g == 1:
    acumm = acumm + boni
  if g == 2:
    acumh = acumh + boni

  print("pago persona:","subtotal",subtotal,"bonificacion",boni,"pagototal",tpago)
  
print("Pago Total Todos:",acumpago)
print("Bonificacion Todos:",acumboni)
print("Bonificacion Hombres:",acumh)
print("Bonificacion mujeres:",acumm)
