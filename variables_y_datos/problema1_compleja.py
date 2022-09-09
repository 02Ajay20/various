#a diferencia de la version simple esta contiene excepeciones para evitar los posibles errores
#tambien tiene un bucle while True para que el programa no se cierra hasta que el usuario lo cierre

def problemA():
  try:
    print('''escribe un numero para siguiente ecuacion:

    100-200
    ───────
      A-5''')
    a = float(input("escriba el numero A: "))
    result = (100-200)/(a-5)
    print(f"el resultado es: {result}")
  except ValueError:
    print("ERROR - Escriba numeros, no letras")
    problemA()
  except ZeroDivisionError:
    print("ERROR - No se puede dividir por 0")
    problemA()

def problemB():
  try:
    print('''escribe un numero para siguiente ecuacion:

        A^2
    15- ───
         3''')
    a = float(input("escriba el numero A: "))
    result = 15 - a**2/3
    print(f"el resultado es: {result}")
  except ValueError:
    print("ERROR - Escriba numeros, no letras")
    problemB()

def problemC():
  try:
    print('''escribe los numeros para siguiente ecuacion:

    a^2 + b^2 - 35c''')
    a = float(input("escriba el numero a: "))
    b = float(input("escriba el numero b: "))
    c = float(input("esbriba el numero c: "))
    result = a**2 + b**2 - 35*c
    print(f"el resultado es: {result}")
  except ValueError:
    print("ERROR - Escriba numeros, no letras")
    problemC()

def problemD():
  try:
    print('''escribe un numero para la siguiente ecuacion:
    
    5x^2 - 3X + 5
    ''')
    x = float(input("escribe el numero x: "))
    result = 5*x**2 - 3*x + 5
    print(f"el resultado es: {result}")
  except ValueError:
    print("ERROR - Escriba numeros, no letras")
    problemD()

def problemE():
  try:
    print('''escribe los numeros para siguiente ecuacion:

    √a + √b^2''')
    a = float(input("escribe un numero a: "))
    b = float(input("escribe un numero b: "))
    result = (a**0.5) + ((b**0.5)**3)
    print(f"el resultado es: {result}")
  except ValueError:
    print("ERROR - Escriba numeros, no letras")
    problemE()

def problemF():
  try:
    print('''escribe un numero para siguiente ecuacion:

    a^10 - 5''')
    a = float(input("escribe un numero a: "))
    result = a**10 - 5
    print(f"el resultado es: {result}")
  except ValueError:
    print("ERROR - Escriba numeros, no letras")
    problemF()

print('''Elige una de las siguientes opciones:
Escribe A para la primera exprecion algebraica
Escribe B para la segunda exprecion algebraica
Escribe C para la tercera exprecion algebraica
Escribe D para la cuarta  exprecion algebraica
Escribe E para la quinta  exprecion algebraica
Escribe F para la sexta   exprecion algebraica
Escribe Salir cuando quieras cerrar el programa
''')
while True:
  execute = input("\nEscribe el problema que quieres ejecutar: ").lower()
  if execute == "a":
    problemA()
  elif execute == "b":
    problemB()
  elif execute == "c":
    problemC()
  elif execute == "d":
    problemD()
  elif execute == "e":
    problemE()
  elif execute == "f":
    problemF()
  elif execute == "salir":
    break
  else:
    print("Opcion inexistente, vuelve a intentarlo")
