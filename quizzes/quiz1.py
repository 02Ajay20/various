numero = int(input("Ingrese un numero en hehsvvvvg: "))

hehs = numero // 100000
modulohehs = numero % 100000
valorhora = modulohehs // 10
genero = modulohehs % 10

horasentrada = hehs // 100
horassalida = hehs % 100

horastotal = horassalida - horasentrada
# print(horastotal)
totalpago = (horastotal * valorhora)

if horastotal < 8:
  if genero == 1:
    porcentaje = 0.1
    bonificacion = totalpago * porcentaje
    print("su bonificacion es de ", bonificacion)
    print("Horas trabajadas: ", horastotal)
    print("pagototal: ", totalpago + horastotal)
  if genero == 2:
    porcentaje = 0.05
    bonificacion = totalpago * porcentaje
    print("su bonificacion es de ", bonificacion)
    print("Horas trabajadas: ", horastotal)
    print("pagototal: ", totalpago + bonificacion)
  if genero >2:
    print("operacion incorrecta vuelva a intentarlo")

elif horastotal > 8 and horastotal < 12:
    if genero == 1:
      porcentaje = 0.2
      bonificacion = totalpago * porcentaje
      print("su bonificacion es de ", bonificacion)
      print("Horas trabajadas: ", horastotal)
      print("pagototal: ", totalpago + bonificacion)
    if genero == 2:
      porcentaje = 0.3
      bonificacion = totalpago * porcentaje
      print("su bonificacion es de ", bonificacion)
      print("Horas trabajadas: ", horastotal)
      print("pagototal: ", totalpago + bonificacion)
    if genero >2:
      print("operacion incorrecta vuelva a intentarlo")

elif horastotal >= 12:
  print("entra o entra hijueputa")
  if genero == 1:
    porcentaje = 0.4
    bonificacion = totalpago * porcentaje
    print("su bonificacion es de ", bonificacion)
    print("Horas trabajadas: ", horastotal)
    print("pagototal: ", totalpago + bonificacion)
  if genero == 2:
    porcentaje = 0.4
    bonificacion = totalpago * porcentaje
    print("su bonificacion es de ", bonificacion)
    print("Horas trabajadas: ", horastotal)
    print("pagototal: ", totalpago + bonificacion)
  if genero >2:
    print("operacion incorrecta vuelva a intentarlo")

else:
  print("valor de horas incorrecto")
