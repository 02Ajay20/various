n = int(input("digite n: "))

TOTAL = 0
TBONI = 0
TH = 0
TM = 0

subtotal = 0
bonificacion = 0
total = 0
category = 0

turno = 0  #if turno == 1 dia  if turno == 2 noche

for i in range(1,n+1):
  dato = int(input("digite en formato hehseegvvvv: "))
  he = dato//1000000000
  hs = (dato%1000000000)//10000000
  ee = (dato%10000000)//100000
  g = (dato%100000)//10000
  v = dato%10000

  hora = hs-he
  subtotal = hora * v

  if hora < 5:
    category = 1
  if hora >= 5:
    if hora <= 8:
      category = 2
  if hora > 8:
    category = 3
  
  if he >= 6:
    if he <= 17:
      turno = 1
    if he > 17:
      turno = 2
  else:
    turno = 2

  if g == 1:
    if category > 1:
      if turno == 2:
        bonificacion = subtotal * 0.4
        TM += bonificacion
  if g == 2:
    if category != 2:
      if turno == 2:
        bonificacion = subtotal * 0.2
        TH += bonificacion

  total = bonificacion + subtotal
  print(f"Subtotal persona: {subtotal}\nBonificacion persona: {bonificacion}\nTotal persona: {total}")

  TOTAL += total
  TBONI += bonificacion

print()
print(f"Total Todos: {TOTAL}")
print(f"Bonificacion Todos: {TBONI}")
print(f"Bonificacion Hombres: {TH}")
print(f"Bonificacion Mujeres: {TM}")