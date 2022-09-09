#Saca el valor del 16% IVA de un valor especifico

print("escribe un valor y obten el iva (16%) de ese valor")
value = float(input("Escribe un valor en pesos colombianos: "))
iva = value * .16
total = value + iva

print(f"\nEl 16% de iva de {value} es {iva}\nEl valor mas el 16% de iva el {total}")