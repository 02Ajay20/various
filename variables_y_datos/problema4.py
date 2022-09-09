def triangleArea():
  print("Calcula el area de un triangulo")
  base = float(input("escriba la base del triangulo: "))
  height = float(input("escribe la altura del triangulo: "))

  triangle_area = base * height / 2
  print(f"El area del triangulo es: {triangle_area}")

def rhombusArea():
  dheight = float(input("escriba el diametro vertical del rombo: "))
  dwidth = float(input("escriba el diametro horizontal del rombo: "))

  rhombus_area = dheight * dwidth / 2
  print(f"El area del rombo es: {rhombus_area}")

def trapezeArea():
  print("Calcula el area de un triangulo")
  menorbase = float(input("escriba la base del trapecio: "))
  majorbase = float(input("escriba la base del trapecio: "))
  height = float(input("escribe la altura del trapecio: "))

  trapeze_area = (majorbase+menorbase) / 2 * height 
  print(f"El area del trapecio es: {trapeze_area}")

# trapezeArea()
# rhombusArea()
# triangleArea()