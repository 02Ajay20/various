print("Calcular el area de la franja amarilla")
a = float(input("escribe un numero a: "))
b = float(input("escribe un numero b: "))
c = float(input("escribe un numero c: "))
r = a/2

trapeze = (a+c) / 2 * b
circle = 2 * 3.1416 * r

yellow_area = trapeze - circle
print(f"el area de la franja amarilla es: {yellow_area}")