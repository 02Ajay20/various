print("De tres numeros cual es el menor, cual es el mayor y/o cuales son iguales")

num_1 = float(input("Escribe el primer  numero: "))
num_2 = float(input("Escribe el segundo numero: "))
num_3 = float(input("Escribe el tercero numero: "))

if num_1 == num_2:
  if num_1 == num_3:
    print(f"{num_1} {num_2} {num_3} son iguales")
  else:
    print(f"{num_1} {num_2} son iguales")
    if num_1 > num_3:
      print(f"{num_1} {num_2} mayores\n{num_3} menor")
    else:
      print(f"{num_3} mayor\n{num_1} {num_2} menores")
else:
  if num_1 == num_3:
    print(f"{num_1} {num_3} son iguales")
    if num_1 > num_2:
      print(f"{num_1} {num_3} mayores\n{num_2} menor")
    else:
      print(f"{num_2} mayor\n{num_1} {num_3} menores")
  else:
    if num_2 == num_3:
      print(f"{num_2} {num_3} son iguales")
      if num_1 > num_2:
        print(f"{num_1} mayor\n{num_2} {num_3} menores")
      else:
        print(f"{num_2} {num_3} mayor\n{num_1} menor")
    else:
      if num_1 > num_2:
        if num_1 > num_3:
          print(f"{num_1} mayor")
          if num_2 > num_3:
            print(f"{num_3} menor")
          else:
            print(f"{num_2} menor")
        else:
          print(f"{num_3} mayor\n{num_2} menor")
      else:
        if num_2 > num_3:
          print(f"{num_2} mayor")
          if num_1 > num_3:
            print(f"{num_3} menor")
          else:
            print(f"{num_1} menor")
        else:
          print(f"{num_3} mayor\n{num_1} menor")

print("\n\tprgrama finalizado")