#El uso de funciones es unicamete para no tener que hacer varios archivos o mostrar las series juntas
#El uso de while es unicamente para la comodidad a la hora de ejecutar el algoritmo
def serieA():
  user_num = int(input("cuantos numeros quieres ver: "))
  x = 1
  serie = 4
  print(x)

  for i in range(1,user_num):
    resultado = x * serie
    x += 1
    print(resultado)

def serieB():
  user_num = int(input("cuantos numeros quieres ver: "))
  x = 1
  serie = 3

  for i in range(1,user_num+1):
    print(x)
    x = x + serie
    serie = serie + 2

def serieC():
  user_num = int(input("cuantos numeros quieres ver: "))
  x = 2
  acumulator = 0

  for i in range(1,user_num+1):
    print(x)
    acumulator = acumulator + x
    x += 2

def serieD():
  user_num = int(input("cuantos numeros quieres ver: "))
  serie1 = 2
  serie2 = 4
  serie_suma = 0

  for i in range(1,user_num+1):
    if i % 2 != 0:
      negative_serie = serie1 * -1
      print(negative_serie)
    elif i % 2 == 0:
      print(f"+{serie1}")

    serie_suma = serie1 + serie2

    serie1 = serie2
    serie2 = serie_suma

print("Este algoritmo muestra diversas series numericas")

print('''
Elige la Serie que deseas digitar:
Escribe A para mostrar la serie A
Escribe B para mostrar la serie B
Escribe C para mostrar la serie C
Escribe D para mostrar la serie D
Escribe SALIR para cerrar el programa
''')
entrada = False

while entrada != True:
  option = input("Escribe la opcion que deseas realizar: ").lower()
  if option == "a":
    serieA()
  elif option == "b":
    serieB()
  elif option == "c":
    serieC()
  elif option == "d":
    serieD()
  elif option == "salir":
    print("\nPrograma cerrado con exito")
    entrada = True
  else:
    print("opcion incorrecta, vuelve a intentarlo")