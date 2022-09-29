juan = int(input("Digite los votos de Juan: "))
pedro = int(input("Digite los votos de Pedro: "))
maria = int(input("Digite los votos de Maria: "))

suma = juan + pedro + maria
fifty_percent = suma / 2
ganador = 0
empate = 0
nombre = ""

if juan > fifty_percent:
  ganador = 1
else:
  if pedro > fifty_percent:
    ganador = 2
  else:
    if maria > fifty_percent:
      ganador = 3
    else:
      #aqui empieza la tralla, si no gana ninguno a la primera pasa lo siguiente
      #primera parte: si alguno o todos los resultados de votos son iguales
      if juan == pedro:
        if juan == maria:
          empate = 1
        else:
          if juan > maria:
            print("\nsegunda vuelta")
            juan = int(input("Digite los votos de Juan: "))
            pedro = int(input("Digite los votos de Pedro: "))
            while juan == pedro:
              print("\nHubo un empate - intentenlo otra vez")
              juan = int(input("Digite los votos de Juan: "))
              pedro = int(input("Digite los votos de Pedro: "))
            if juan > pedro:
              ganador = 1
            else:
              ganador = 2
          else:
            empate = 2
      else:
        if pedro == maria:
          if juan > maria:
            empate = 2
          else:
            print("\nsegunda vuelta")
            pedro = int(input("Digite los votos de Pedro: "))
            maria = int(input("Digite los votos de Maria: "))
            while pedro == maria:
              print("\nHubo un empate - intentenlo otra vez")
              pedro = int(input("Digite los votos de Pedro: "))
              maria = int(input("Digite los votos de Maria: "))
            if pedro > maria:
              ganador = 2
            else:
              ganador = 3
        else:
          if juan == maria:
            if juan > pedro:
              print("\nsegunda vuelta")
              juan = int(input("Digite los votos de Juan: "))
              maria = int(input("Digite los votos de Maria: "))
              while juan == maria:
                print("\nHubo un empate - intentenlo otra vez")
                juan = int(input("Digite los votos de Juan: "))
                maria = int(input("Digite los votos de Maria: "))
              if juan > maria:
                ganador = 1
              else:
                ganador = 3
            else:
              print("Eleccion anulada por empate en la sugunda posicion")
          else:
            #segunda parte: si todos los resultados de votos son distinto
            if pedro < juan:
              if pedro < maria:
                print("\nsegunda vuelta")
                juan = int(input("Digite los votos de Juan: "))
                maria = int(input("Digite los votos de Maria: "))
                while juan == maria:
                  print("\nHubo un empate - intentenlo otra vez")
                  juan = int(input("Digite los votos de Juan: "))
                  maria = int(input("Digite los votos de Maria: "))           
                if juan > maria:
                  ganador = 1
                else:
                  ganador = 3
              else:
                print("\nsegunda vuelta")
                juan = int(input("Digite los votos de Juan: "))
                pedro = int(input("Digite los votos de Pedro: "))
                while juan == pedro:
                  print("\nHubo un empate - intentenlo otra vez")
                  juan = int(input("Digite los votos de Juan: "))
                  pedro = int(input("Digite los votos de Pedro: "))
                if juan > pedro:
                  ganador = 1
                else:
                  ganador = 2
            else:
              if maria < pedro:
                if maria < juan:
                  print("\nsegunda vuelta")
                  juan = int(input("Digite los votos de Juan: "))
                  pedro = int(input("Digite los votos de Pedro: "))
                  while juan == pedro:
                    print("\nHubo un empate - intentenlo otra vez")
                    juan = int(input("Digite los votos de Juan: "))
                    pedro = int(input("Digite los votos de Pedro: "))
                  if juan > pedro:
                    ganador = 1
                  else:
                    ganador = 2
                else:
                  print("\nsegunda vuelta")
                  pedro = int(input("Digite los votos de Pedro: "))
                  maria = int(input("Digite los votos de Maria: "))
                  while pedro == maria:
                    print("\nHubo un empate - intentenlo otra vez")
                    pedro = int(input("Digite los votos de Pedro: "))
                    maria = int(input("Digite los votos de Maria: "))
                  if pedro > maria:
                    ganador = 2
                  else:
                    ganador = 3
              else:
                print("\nsegunda vuelta")
                pedro = int(input("Digite los votos de Pedro: "))
                maria = int(input("Digite los votos de Maria: "))
                while pedro == maria:
                  print("\nHubo un empate - intentenlo otra vez")
                  pedro = int(input("Digite los votos de Pedro: "))
                  maria = int(input("Digite los votos de Maria: "))
                if pedro > maria:
                  ganador = 2
                else:
                  ganador = 3

if empate == 1:
  print("Eleccion anulada por empate triple")
elif empate == 2:
  print("Eleccion anulada por empate en la sugunda posicion")

if ganador == 1:
  nombre = "Juan"
  print(f"Gana {nombre}")
elif ganador == 2:
  nombre = "Pedro"
  print(f"Gana {nombre}")
elif ganador == 3:
  nombre = "Maria"
  print(f"Gana {nombre}")

print("\n\tPrograma Finalizado")