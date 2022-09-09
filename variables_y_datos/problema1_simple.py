#El uso de funciones es basicamente para evitar tener que hacer 6 archivos distintos para cada problema

def problemA():
  print('''escribe un numero para siguiente ecuacion:

  100-200
  ───────
    A-5''')
  a = float(input("escriba el numero A: "))
  result = 100-200/a-5
  print(f"el resultado es: {result}")

def problemB():
  print('''escribe un numero para siguiente ecuacion:

      A^2
  15- ───
       3''')
  a = float(input("escriba el numero A: "))
  result = 15 - a**2/3
  print(result)

def problemC():
  print('''escribe los numeros para siguiente ecuacion:

  a^2 + b^2 - 35c''')
  a = float(input("escriba el numero a: "))
  b = float(input("escriba el numero b: "))
  c = float(input("esbriba el numero c: "))
  result = a**2 + b**2 - 35*c
  print(result)

def problemD():
  print('''escribe un numero para la siguiente ecuacion:
  
  5x^2 - 3X + 5
  ''')
  x = float(input("escribe el numero x: "))
  result = 5*x**2 - 3*x + 5
  print(result)

def problemE():
  print('''escribe los numeros para siguiente ecuacion:

  √a + √b^2''')
  a = float(input("escribe un numero a: "))
  b = float(input("escribe un numero b: "))
  result = (a**0.5) + ((b**0.5)**3)
  print(result)

def problemF():
  print('''escribe un numero para siguiente ecuacion:

  a^10 - 5''')
  a = float(input("escribe un numero a: "))
  result = a**10 - 5
  print(result)

# problemA()
# problemB()
# problemC()
# problemD()
# problemE()
# problemF()
