#Suma las potencias de 2, de tres numeros distintos

print("Version sin utilizar funciones")
num1 = float(input("escribe el primer  numero: "))
num2 = float(input("escribe el sugundo numero: "))
num3 = float(input("escribe el tercero numero: "))

result = (num1**2) + (num2**2) + (num3**2)
print(f"El resultado es {result}")

print("\nVersion con una funcion")
def summation(num1, num2, num3):
  result = (num1**2) + (num2**2) + (num3**2)
  return result

num1 = float(input("escribe el primer  numero: "))
num2 = float(input("escribe el sugundo numero: "))
num3 = float(input("escribe el tercero numero: "))
print(summation(num1, num2, num3))