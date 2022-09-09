print("convertir un numero de segundos a horas, minutos y segundos")
seconds = int(input("escribe la cantidad de segundos que desee: "))

horas = seconds // 3600
modul_seconds = seconds % 3600
minutos = modul_seconds//60
segundos = modul_seconds%minutos

print(f"El resultado es: H-{horas} M-{minutos} S-{segundos}")