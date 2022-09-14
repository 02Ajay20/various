print('''Introduce el codigo de 8 digitos de un estudiante para verificar el que año y semestre empezo a estudiar
teniendo en cuenta que los primeros 4 digitos son el año y el siguiente digito es el semestre y los ultimos 3 la id
''')

code = int(input("escribe el codigo de estudiante: "))

year = code // 10000
modul_code = code % 10000
semester = modul_code // 1000

if semester == 1:
  print(f"el estudiante se iscribio en {year} en el {semester} semestre")
elif semester == 2:
  print(f"el estudiante se iscribio en {year} en el {semester} semestre")
else:
  print("un año solo puede tener 2 semestres ni mas ni menos\nvuelve a escribir el codigo")