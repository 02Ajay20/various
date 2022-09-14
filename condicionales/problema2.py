print("Indentifica si un año es bisiesto o no\n")

year = int(input("digita un año de la sigiente manera - yyyymmdd: "))
yyyy = year //10000
yyyy_residuo = year % 10000
mm = yyyy_residuo // 100
dd = yyyy_residuo % 100

if yyyy % 4 == 0:
  print(f"{yyyy} es un año bisiesto")
else:
  print(f"{yyyy} no es un año bisiesto")