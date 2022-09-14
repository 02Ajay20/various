#No se como resolver esto sin operadores logicos.
print("Escribe las caractiristicas de una persona y te dira si es valida para el programa o no")

nombre = input("escribe tu nombre: ")
edad = int(input("escribe tu edad: "))
sexo = input("escribe el genero: ")
estado_civil = input("escribe tu estado civil: ")

if edad >= 40:
  print(f"aplica {nombre}\nedad {edad}")
if sexo == "hombre":
  print(f"aplica {sexo}")
if estado_civil == "casado":
  print(f"aplica {estado_civil}")


if edad <= 50:
  print(f"aplica {nombre}\nedad {edad}")
if sexo == "mujer":
  print(f"aplica {sexo}")
if estado_civil == "soltera":
  print(f"aplica {estado_civil}")
else:
  print("no aplica")