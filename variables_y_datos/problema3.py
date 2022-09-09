def conversorDolarPeso():
  print("Conversor de dolares a pesos y de pesos a dolares")
  cop = int(input("Digite a cantidad de pesos que quieres convertir: "))
  dolares = float(input("Digite a cantidad de dolares que quieres convertir: "))
  
  conversion_cop = cop / 4397
  conversion_dolares = dolares * 4397
  print(f"{cop} Pesos son {conversion_dolares} Dolares\n{dolares} Dolares son {conversion_cop:.1f} Pesos")

def temperatureConversion():
  print("Conversor de centigrados a farenheit y de farenheit a centigrados")
  celcius = float(input("escriba el numero de grados centigrados que quiera convertir: "))
  farenheit = float(input("escriba el numero de grados farenheit que quiera convertir: "))

  conversion_farenheit = (celcius * 9/5) + 32
  conversion_celcius = (farenheit - 32) * 5/9
  print(f"{celcius} grados centigrados son {conversion_farenheit} Dolares\n{farenheit} Dolares son {conversion_celcius} Pesos")

def average():
  print("calcula el promedio entre tres numeros")
  num1 = int(input("Escribe el primer  numero: "))
  num2 = int(input("Escribe el segundo numero: "))
  num3 = int(input("Escribe el tercero numero: "))

  suma = num1 + num2 + num3
  average = suma/3
  print(f"el promedio de {num1}, {num2}, {num3} es: {average}")

# average()
# temperatureConversion()
# conversorDolarPeso()