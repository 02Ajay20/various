print("Escribe un numero y te dara el dia de la semana que corresponda con este\n")

day = input("escribe el numero del 1 al 7: ")

if day > 7:
  print("dia de la semana inexistente, o al menos en este universo")
elif day == 1:
  print("elegiste el - LUNES")
elif day == 2:
  print("elegiste el - MARTES")
elif day == 3:
  print("elegiste el - MIERCOLES")
elif day == 4:
  print("elegiste el - JUEVES")
elif day == 5:
  print("elegiste el - VIERNES")
elif day == 6:
  print("elegiste el - SABADO")
elif day == 7:
  print("elegiste el - DOMINGO")