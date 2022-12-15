motorbikes = []
cars = []
carfee = 0
motorbikefee = 0

def identification(vehicle,place):
  index = 0
  code = ""
  number_cars = len(cars)
  number_motorbikes = len(motorbikes)
  
  if vehicle == "c":
    number_vehicles = len(cars)
    type_vehicle = cars
    y ="Car"
  elif vehicle == "m":
    number_vehicles = len(motorbikes)
    type_vehicle = motorbikes
    y = "Moto"
    
  if place == "entry":
    plate = input("Enter the license plate number of the vehicle you want entry: ").upper()
  else:
    plate = input("Enter the license plate of the car you are looking for: ").upper()
  for i in range(number_vehicles):
    code = type_vehicle[i][0]
    if code == plate:
      if place == "entry":
        return "ready_vehicle"
      else:
        index = i
        return index
  if place == "search":
    index = "nf"
    return index

  if code != plate:
    if place == "entry":
      return plate
    else:
      if place == "exit":
        print("Vehicle not found")
        index = "nf"
        return index

def hours(ind, vehicle, heme):
  minutes = 0
  total = 0
  index = ind
  while minutes == 0:
    hsms = input("Write the exit hour HSMS: ")
    digito = len(hsms)
    if digito == 4:
      hsms = int(hsms)
      he = heme // 100
      me = heme % 100
      hs = hsms // 100
      ms = hsms % 100
    
    if digito != 4:
      print("The digits of the HSMS must be 4")
    elif heme > hsms:
      print("Entry hours may not be longer than exit hours")
    elif hs > 23:
      print("The hours cannot be longer than 23")
    elif ms > 60:
      print("The hours are only 60 minutes, try again")
    else:
      hour_entry = he * 60
      hour_exit = hs * 60
      hour_entry += me
      hour_exit += ms
      minutes = hour_exit - hour_entry

      if  minutes == 0:
          print("Hours cannot sum 0, try again")
  
  if vehicle == "c":
    total = minutes * carfee
    cars[index].append(hsms)
    cars[index].append(minutes)
    cars[index].append(total)
  elif vehicle == "m":
    total = minutes * motorbikefee
    motorbikes[index].append(hsms)
    motorbikes[index].append(minutes)
    motorbikes[index].append(total)

def fees():
  def entryFees(mod):
    global carfee
    global motorbikefee
    enter = True
    while enter != False:
      if mod == "modify":
        print("\nModify Fees Menu:\n1. Modify Cars fee\n2. Modify Motorbikes fee\n3. Back to Fees Menu")
      else:
        print("\nEnter Fees Menu:\n1. Entry Cars fee\n2. Entry Motorbikes fee\n3. Back to Fees Menu")
      options = input("\nSelect an option: ")

      if options == "1":
        if mod == "modify":
          carfee = int(input("New cars fee: "))
        else:
          if carfee > 0:
            print("The Fee has already been writted")
          else:
            carfee = int(input("Fee for Cars: "))
            if carfee < 0:
              carfee *= -1

      elif options == "2":
        if mod == "modify":
          motorbikefee = int(input("New motorbikes fee: "))
        else:
          if motorbikefee > 0:
            print("The Fee has already been writted")
          else:
            motorbikefee = int(input("Fee for motorbikes: "))
            if motorbikefee < 0:
              motorbikefee *= -1
      elif options == "3":
        enter = False
      else:
        print("This option don't exist")
      
  def showFees():
    print("\nCar fee:",carfee,"\nMotorbike fee:",motorbikefee)
    press_continue = input("\tPress enter to Continue")


  enter = True
  while enter != False:
    print("\nFees Menu:\n1. Entry vehicles fees\n2. Show fees\n3. Modify fees\n4. Back to Main Menu")
    options = input("\nSelect an option: ")

    if options == "1":
      entryFees("entry")
    elif options == "2":
      showFees()
    elif options == "3":
      entryFees("modify")
    elif options == "4":
      enter = False
    else:
      print("This option don't exist")

def entryVehicles():
  create_vehicle = []
  print("What type of vehicle do you want to entry:\nc. Car - m. Motorbike")
  vehicle = input("Select the vehicle: ").lower()

  key = True
  if vehicle == "c":
    while key != False:
      plate = identification(vehicle, "entry")
      count_letters = 0
      count_numbers = 0
      if len(plate) == 6:
        for i in range(6):
          digit = plate[i]
          if i <= 2:
            if digit == "1":
              count_letters += 1
            if digit == "2":
              count_letters += 1
            if digit == "3":
              count_letters += 1
            if digit == "4":
              count_letters += 1
            if digit == "5":
              count_letters += 1
            if digit == "6":
              count_letters += 1
            if digit == "7":
              count_letters += 1
            if digit == "8":
              count_letters += 1
            if digit == "9":
              count_letters += 1
            if digit == "0":
              count_letters += 1
          if i > 2:
            if digit == "1":
              count_numbers += 1
            if digit == "2":
              count_numbers += 1
            if digit == "3":
              count_numbers += 1
            if digit == "4":
              count_numbers += 1
            if digit == "5":
              count_numbers += 1
            if digit == "6":
              count_numbers += 1
            if digit == "7":
              count_numbers += 1
            if digit == "8":
              count_numbers += 1
            if digit == "9":
              count_numbers += 1
            if digit == "0":
              count_numbers += 1
      if count_numbers == 3 and count_letters == 0:
        key = False
      else:
        if plate == "ready_vehicle":
          print("This vehicle already exists")
        else:
          print("The plate must have 6 digits, three letters and three numbers")
        
  elif vehicle == "m":
    while key != False:
      plate = identification(vehicle, "entry")
      count_letters = 0
      count_numbers = 0
      if len(plate) == 6:
        for i in range(6):
          digit = plate[i]
          if i <= 2 or i > 4:
            if digit == "1":
              count_letters += 1
            if digit == "2":
              count_letters += 1
            if digit == "3":
              count_letters += 1
            if digit == "4":
              count_letters += 1
            if digit == "5":
              count_letters += 1
            if digit == "6":
              count_letters += 1
            if digit == "7":
              count_letters += 1
            if digit == "8":
              count_letters += 1
            if digit == "9":
              count_letters += 1
            if digit == "0":
              count_letters += 1
          if i > 2 and i <= 4:
            if digit == "1":
              count_numbers += 1
            if digit == "2":
              count_numbers += 1
            if digit == "3":
              count_numbers += 1
            if digit == "4":
              count_numbers += 1
            if digit == "5":
              count_numbers += 1
            if digit == "6":
              count_numbers += 1
            if digit == "7":
              count_numbers += 1
            if digit == "8":
              count_numbers += 1
            if digit == "9":
              count_numbers += 1
            if digit == "0":
              count_numbers += 1
      if count_numbers == 2 and count_letters == 0:
        key = False
      else:
        print("The plate has to have 6 digits, three letters, two numbers and one letter at the end")
  else:
    print("This type vehicle don't exist")

  client_name = input("Write the client name: ").capitalize()
  key = True
  while key != False:
    heme = input("Write the entry hour HEME: ")
    digito = len(heme)
    if digito == 4:
      heme = int(heme)
      he = heme // 100
      me = heme % 100
    if digito != 4:
      print("The digits of the HEME must be 4")
    elif he > 23:
      print("The hours cannot be longer than 23")
    elif me > 60:
      print("The hours are only 60 minutes, try again")
    else:
      key = False

  create_vehicle.append(plate)
  create_vehicle.append(client_name)
  create_vehicle.append(heme)
  if vehicle == "c":
    cars.append(create_vehicle)
  elif vehicle == "m":
    motorbikes.append(create_vehicle)

def searchVehicles():
  enter = True
  while enter != False:
    print("\nSearch Menu:\n1. Search Cars\n2. Search Motosbikes\n3. Back to Main Menu")
    options = input("\nSelect an option: ")
    number_cars = len(cars)
    number_motorbikes = len(motorbikes)

    if options == "1" or options == "2":
      if options == "1":
        number_vehicles = number_cars
        vehicle = "c"
        type_vehicle = cars
        y = "Car"
      if options == "2":
        number_vehicles = number_motorbikes
        vehicle = "m"
        type_vehicle = motorbikes
        y = "Moto"

      if number_vehicles == 0:
        if options == "1":
          extras("no_cars")
        if options == "2":
          extras("no_motos")
      else:
        index = identification(vehicle,"search")
        if index != "nf":
          number_vehicle = len(type_vehicle[index])
          for a in range(1):
            print("\nType of vehicle:",y)
            print("Plate:",type_vehicle[index][0])
            print("Propietary:",type_vehicle[index][1])
            print("Entry hour:",type_vehicle[index][2])
            if number_vehicle > 3:
              print("Exit hour:",type_vehicle[index][3])
              print("Minutes:",type_vehicle[index][4])
              print("Total:",type_vehicle[index][5])
          press_continue = input("\tPress enter to Continue")
        else:
          print("Vehicle not found")

    elif options == "3":
      enter = False
    else:
      print("This option don't exist")

def showVehicles():
  def show(vehicle):
    number_cars = len(cars)
    number_motorbikes = len(motorbikes)
    if vehicle == "c":
      number_vehicles = number_cars
      type_vehicle = cars
      y = "Car"
    if vehicle == "m":
      number_vehicles = number_motorbikes
      type_vehicle = motorbikes
      y = "Moto"

    if number_vehicles == 0:
      if vehicle == "c":
        extras("no_cars")
      if vehicle == "m":
        extras("no_motos")
    else:
      x = 0
      name_digits = 0
      for i in range(number_vehicles):
        name_digits = len(type_vehicle[i][1])
        if name_digits > x:
          x = name_digits
      if x <= 8:
        x = 10
      print("Type Search:",y)
      print("Plate   Propiety"," "*(x-9),"Entry Exit Minutes Total")
      for v in range(number_vehicles):
        number_vehicle = len(type_vehicle[v])
        name_digits = x - len(type_vehicle[v][1])
        print(type_vehicle[v][0],end="  ")
        if type_vehicle[v][2] < 1000:
          print(type_vehicle[v][1],end=" "*(name_digits+2))
        else:
          print(type_vehicle[v][1],end=" "*(name_digits+1))
        if number_vehicle == 3:
          print(type_vehicle[v][2])
        if number_vehicle > 3:
          if type_vehicle[v][3] < 1000:
            print(type_vehicle[v][2],end=" "*3)
          else:
            print(type_vehicle[v][2],end="  ")
          print(type_vehicle[v][3],end=" ")
          if type_vehicle[v][4] > 999:
            print(type_vehicle[v][4],end=" "*4)
          elif type_vehicle[v][4] > 99:
            print(type_vehicle[v][4],end=" "*5)
          elif type_vehicle[v][4] > 9:
            print(type_vehicle[v][4],end=" "*6)
          print(type_vehicle[v][5])
      press_continue = input("\tPress enter to Continue")

  enter = True
  while enter != False:
    print("\nShow Vehicles Menu:\n1. Show All Cars\n2. Show All Motorbikes\n3. Back to Main Menu")
    options = input("\nSelect an option: ")

    if options == "1":
      show("c")
    elif options == "2":
      show("m")
    elif options == "3":
      enter = False
    else:
      print("This option don't exist")

def exitVehicles():
  key = True
  enter = True
  while enter != False:
    number_cars = len(cars)
    number_motorbikes = len(motorbikes)
    vehicle = input("What type of vehicle exit. Write c. Car - m. Moto: ")
    if vehicle == "c":
      if number_cars == 0:
        extras("no_cars")
      else:
        index = identification("c","exit")
        if index != "nf":
          if len(cars[index]) > 3:
            key = False
          else:
            heme = cars[index][2]
            hours(index, "c", heme)
        else:
          key = False
        enter = False
    elif vehicle == "m":
      if number_motorbikes == 0:
        extras("no_motos")
      else:
        index = identification("m","exit")
        if index != "nf":        
          if len(motorbikes[index]) > 3:
            key = False
          else:
            heme = motorbikes[index][2]
            hours(index, "m", heme)
        else:
          key = False
        enter = False
    else:
      print("type vehicle wrong, write c or m")

  if key == True:
    if vehicle == "c":
      type_vehicle = cars
      y = "Car"
    if vehicle == "m":
      type_vehicle = motorbikes
      y = "Moto"

    for a in range(1):
      print("\nType of vehicle:",y)
      print("Plate:",type_vehicle[index][0])
      print("propietary:",type_vehicle[index][1])
      print("Entry Hour:",type_vehicle[index][2])
      print("Exit Hour:",type_vehicle[index][3])
      print("Minutes:",type_vehicle[index][4])
      print("Total pay:",type_vehicle[index][5])
    press_continue = input("\tPress enter to Continue")
  else:
    if index != "nf":
      print("This vehicle has left")

def cashFlow():
  print("\tCashFlow")
  number_cars = len(cars)
  number_motos = len(motorbikes)
  total_cars = 0
  total_motos = 0
  total = 0

  if number_cars > 0:
    for a in range(number_cars):
      number_vehicle = len(cars[a])
      if number_vehicle > 3:
        total_cars += cars[a][5]
  if number_motos > 0:
    for m in range(number_motos):
      number_vehicle = len(motorbikes[m])
      if number_vehicle > 3:
        total_motos += motorbikes[m][5]
  total = total_cars + total_motos

  x = 0
  print("TotalCars  TotalMotos  Total")
  if total > 0:
    if total_cars > 0:
      n = str(total_cars)
      x = 11 - len(n)
      print(total_cars,end=" "*x)
    else:
      print("          ",end=" ")
    if total_motos > 0:
      n = str(total_motos)
      x = 12 - len(n)
      print(total_motos,end=" "*x)
    else:
      print("           ",end=" ")
    print(total)
    press_continue = input("\tPress enter to Continue")
  else:
    print("No vehicles has left")

def extras(x):
  if x == "no_vehicles":
    enter = True
    while enter != False:
      print("No hay Vehiculos, queres ingresar uno?")
      yes_or_not = input("Yes - No: ").lower()
      if yes_or_not == "yes":
        entryVehicles()
        enter = False
      elif yes_or_not == "no":
        enter = False
  if x == "no_motos":
    enter = True
    while enter != False:
      print("No hay Motos, queres ingresar una?")
      yes_or_not = input("Yes - No: ").lower()
      if yes_or_not == "yes":
        entryVehicles()
        enter = False
      elif yes_or_not == "no":
        enter = False
  if x == "no_cars":
    enter = True
    while enter != False:
      print("No hay Carros, queres ingresar uno?")
      yes_or_not = input("Yes - No: ").lower()
      if yes_or_not == "yes":
        entryVehicles()
        enter = False
      elif yes_or_not == "no":
        enter = False
  if x == "no_fees":
    enter = True
    while enter != False:
      print("No se han ingresado los fees de los car o de las motos, quieres ingresarlo?")
      yes_or_not = input("Yes - No: ").lower()
      if yes_or_not == "yes":
        fees()
        enter = False
      elif yes_or_not == "no":
        enter = False
        
def sortVehicle():
  sort_vehicle = []
  indexs = []
  position = 0
  counter = 0

  enter = True
  while enter != False:
    vehicle = input("write c.Car - m. Moto: ").lower()
    if vehicle == "c":
      enter = False
    elif vehicle == "m":
      enter = False
    else:
      print("This type vehicle dont exist")

  number_cars = len(cars)
  number_motorbikes = len(motorbikes)
  if vehicle == "c":
    number_vehicles = number_cars
    type_vehicle = cars
    y = "Car"
  elif vehicle == "m":
    number_vehicles = number_motorbikes
    type_vehicle = motorbikes
    y = "Moto"
  
  for i in range(number_vehicles):
    if len(type_vehicle[i]) > 3:
      counter += 1
      if i == 0:
        sort_vehicle.append(type_vehicle[i])
        indexs.append(i)
      if i == 1:
        if type_vehicle[i] >= sort_vehicle[0]:
          sort_vehicle.append(type_vehicle[i])
          indexs.append(i)
        if type_vehicle[i] < sort_vehicle[0]:
          sort_vehicle.insert(0, type_vehicle[i])
          indexs.insert(0, i)
      if i == number_vehicles-1:
        if type_vehicle[i] == sort_vehicle[i-1]:
          sort_vehicle.append(type_vehicle[i])
          indexs.append(i)
      if i > 1:
        if type_vehicle[i] > sort_vehicle[i-1]:
          sort_vehicle.append(type_vehicle[i])
          indexs.append(i)
        elif type_vehicle[i] < sort_vehicle[0]:
          sort_vehicle.insert(0, type_vehicle[i])
          indexs.insert(0, i)
        else:
          cont = 0
          for j in range(0,i-1):
            if cont == 1:
              break
            if cont == 0:
              if type_vehicle[i] == sort_vehicle[j]:
                sort_vehicle.insert(j, type_vehicle[i])
                indexs.append(i)
                cont += 1
              if type_vehicle[i] < sort_vehicle[j+1]:
                if type_vehicle[i] > sort_vehicle[j]:
                  sort_vehicle.insert(j+1, type_vehicle[i])
                  indexs.insert(j+1, i)
                  cont += 1
  if counter == 0:
    print("No vehicles has left")
  else:
    print("Type Search:",y)
    print("Plate  Minutes")
    for v in range(number_vehicles):
      print(type_vehicle[indexs[v]][0],end="  ")
      print(type_vehicle[indexs[v]][4])
    press_continue = input("\tPress enter to Continue")      

def menu():
  enter = True
  while enter != False:
    print("""\n\tMain Menu:
1. Fees
2. Entry Vehicles
3. Search Vehicles
4. Show Vehicles
5. Exit Vehicles
6. CashFlow
7. Sort Vehicles for minutes
8. Close Program""")
    number_cars = len(cars)
    number_motorbikes = len(motorbikes)
    options = input("\nOption to realize: ")
    
    if options == "1":
      fees()
    elif options == "2":
      entryVehicles()
    elif options == "3":
      if number_cars > 0 or number_motorbikes > 0:
        searchVehicles()
      else:
        extras("no_vehicles")
    elif options == "4":
      if number_cars > 0 or number_motorbikes > 0:
        showVehicles()
      else:
        extras("no_vehicles")
    elif options == "5":
      if number_cars > 0 or number_motorbikes > 0:
        exitVehicles()
      else:
        extras("no_vehicles")
    elif options == "6":
      if carfee == 0 or motorbikefee == 0:
        extras("no_fees")
      elif number_cars == 0 or number_motorbikes == 0:
        extras("no_vehicles")
      else:
        cashFlow()
    elif options == "7":
      if number_cars > 0 or number_motorbikes > 0:
        sortVehicle()
      else:
        extras("no_vehicles")
    elif options == "8":
      enter = False
    else:
      print("This option don't exist\n")

menu()
print("Program Successfully Closed")
