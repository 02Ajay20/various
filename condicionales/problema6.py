print("Escribe las caractiristicas de una persona y te dira si es valida para el programa o no")

nombre = input("escribe tu nombre: ")
edad = int(input("escribe tu edad: "))
sexo = input("escribe el genero: ")
estado_civil = input("escribe tu estado civil: ")

if sexo == "hombre":
  if edad >= 40:
    if estado_civil == "casado":
      print(f"Aplica")
    else:
      print("No aplica")
  else:
    print("No aplica")
else:
  if sexo == "mujer":
    if edad <= 50:
      if estado_civil == "soltera":
        print("Aplica")
      else:
        print("No aplica")
    else:
      print("no aplica")
  else:
    print("No aplica")
