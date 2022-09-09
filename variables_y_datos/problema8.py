print("convertir toneladas a otras medidas de peso")
toneladas = float(input("digite la cantidad de Toneladas a convertir: "))

kilogramos = toneladas * 1000
quintales = toneladas * 10
gramos = kilogramos * 1000
libras = toneladas * 2205

print(f'''{toneladas} Toneladas son {kilogramos} kilogramos
{toneladas} Toneladas son {quintales} quintales
{toneladas} Toneladas son {gramos} gramos
{toneladas} Toneladas son {libras} libras''')