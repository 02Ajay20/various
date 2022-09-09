print("convertir kilometros a otras medidas de distancia/longitud")
kilometros = float(input("digite la cantidad de kilometros a convertir: "))

metros = kilometros * 1000
centimetros = metros * 100
milimetros = centimetros * 10
pulgadas = kilometros * 39370
yardas = kilometros * 1094
millas = kilometros // 1.609
pies = kilometros * 3281

print(f'''{kilometros} kilometros son {metros} metros
{kilometros} kilometros son {centimetros} centimetros
{kilometros} kilometros son {milimetros} milimetros
{kilometros} kilometros son {pulgadas} pulgadas
{kilometros} kilometros son {yardas} yardas
{kilometros} kilometros son {millas} millas
{kilometros} kilometros son {pies} pies''')