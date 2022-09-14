print("Promedio de las notas de 2 estudiantes, si nota la nota es mayor a 4.5 gana, menor pierde.\n")

ingles1 = float(input("Digita la nota de ingles del primer estudiante: "))
matematicas1 = float(input("Digita la nota de matematicas del primer estudiante: "))
programacion1 = float(input("Digita la nota de programacion del primer estudiante: "))
tecnologia1 = float(input("Digita la nota de tecnologia del primer estudiante: "))
ingles2 = float(input("Digita la nota de ingles del segundo estudiante: "))
matematicas2 = float(input("Digita la nota de matematicas del segundo estudiante: "))
programacion2 = float(input("Digita la nota de progamacion del segundo estudiante: "))
tecnologia2 = float(input("Digita la nota de tecnologia del segundo estudiante: "))
print()

estudiante1 = (ingles1 + matematicas1 + programacion1 + tecnologia1) / 4
estudiante2 = (ingles2 + matematicas2 + programacion2 + tecnologia2) / 4

if estudiante1 > 5 or estudiante2 > 5:
  print("mmm algo esta mal aqui, la nota maxima solo puede ser mayor a 5")
elif estudiante1 >= 4.5 and estudiante2 >= 4.5:
  print(f"Felicitaciones estudiante1 haz ganado la beca con: {estudiante1}")
  print(f"Felicitaciones estudiante2 haz ganado la beca con: {estudiante2}")
elif estudiante1 >= 4.5:
  print(f"Felicitaciones estudiante1 haz ganado la beca con: {estudiante1}")
elif estudiante2 >= 4.5:
  print(f"Felicitaciones estudiante2 haz ganado la beca con: {estudiante2}")
elif estudiante1 < 4.5 and estudiante2 < 4.5:
  print(f"haz perdido la beca estudiante1: {estudiante1}")
  print(f"haz perdido la beca estudiante2: {estudiante2}")
elif estudiante2 < 4.5:
  print(f"haz perdido la beca estudiante1: {estudiante1}")
elif estudiante2 < 4.5:
  print(f"haz perdido la beca estudiante2: {estudiante2}")