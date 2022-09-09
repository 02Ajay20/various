print("determine el area de un diamante: ")
a = float(input("escribe un numero a: "))
b = float(input("escribe un numero b: "))
c = float(input("escribe un numero c: "))
d = float(input("escribe un numero d: "))

triangle = c * b / 2
trapeze = (c+a) / 2 * (d-b)

diamond_area = triangle + trapeze
print(f"esta es el area del diamante: {diamond_area}")