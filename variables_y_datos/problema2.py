print("calcular el area de un triangulo")
a = float(input("escribe un numero a: "))
b = float(input("escribe un numero b: "))
c = float(input("escribe un numero c: "))
p = (a+b+c)/2

area = (p * (p-a) * (p-b) * (p-c))**0.5
print(f"el area es {area:.2f}")