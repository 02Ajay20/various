#este algoritmo es como un Fizz-Buzz pero los digitos los introduce el usuario
print("Escribe un numero de 4 digitos y el algoritmo te dira si es multiplo de 3, 6 o ambos")

numero_texto = input("escribe un numero de cuatro cifras: ")
numero = int(numero_texto)

if numero < 0:
  print("escribe un numero positivo")
elif len(numero_texto) > 4 or len(numero_texto) < 4:
  print("escribe un numero de 4 cifras por favor")
  
elif numero % 6 == 0 and numero % 3 == 0:
  print(f"{numero} es multiplo de 3 y de 6")
elif numero % 3 == 0:
  print(f"{numero} es multiplo de 3")
elif numero % 6 == 0:
  print(f"{numero} es multiplo de 6")
else:
  print(f"{numero} no es multiplo ni de 3 ni de 6")