#calcular el area de una forma especifica

a = float(input("Escriba el valor de a: "))
b = float(input("Escriba el valor de b: "))
c = float(input("Escriba el valor de c: "))
d = float(input("Escriba el valor de d: "))
e = float(input("Escriba el valor de e: "))

rectangle = e+d
triangle = e*b/2
trapeze = ((c-e)+a)/2*b
result = rectangle + triangle + trapeze

print(f"El area total es: {result}")