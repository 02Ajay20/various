user_num = int(input("cuantos numeros quieres ver: "))
serie1 = 0
serie2 = 2
serie_suma = 0
contador = 0

for i in range(0,user_num+1):
  serie_suma = serie1 + serie2
  factorial = 1
  for j in range(1,serie_suma+1):
    factorial = factorial * j
  if contador == 4:
    contador = 0
  elif contador < 2:
    negative_serie = serie_suma* -1
    negative_factorial = factorial * -1
    print(f"{negative_serie}, {negative_factorial}")
    contador += 1
  elif contador >= 2:
    print(f"+{serie_suma}, {factorial}")
    contador += 1

  serie1 = serie2
  serie2 = serie_suma