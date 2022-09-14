print("Escribe las caractiristicas de una persona y te dira si es valida para el programa o no")

nombre = input("escribe tu nombre: ")
edad = int(input("escribe tu edad: "))
sexo = input("escribe el genero: ")
estado_civil = input("escribe tu estado civil: ")

if edad >= 40 and sexo == "hombre" and estado_civil == "casado":
  print(f"es un {sexo} de {edad} años llamado {nombre} que esta {estado_civil}")
elif edad <= 50 and sexo == "mujer" and estado_civil == "soltera":
  print(f"es una {sexo} de {edad} años llamada {nombre} que esta {estado_civil}")
else:
  print("no aplica")