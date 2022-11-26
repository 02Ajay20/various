#Reserve chairs of cinema
chairs = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]

enter = True
while enter != False:
  print('''
1. Reserve
2. Show Reserves
3. Exit
''')
  option = input("Select option: ")
  number_chairs = len(chairs)
  number_chairs_row = len(chairs[0])
  if option == "1":
    chair = int(input("Select number chair: "))
    row = 0
    key = True
    if chair < 16:
      if chair > 10:
        row = 2
    elif chair < 11:
      if chair > 5:
        row = 1
    elif chair < 6:
      if chair > 0:
        row = 0
      else:
        print("only have 15 chairs, 1 - 15")
        key = False
    if key == True:
      for i in range(number_chairs_row):
        p = chairs[row][i]
        if chairs[row][i] == chair:
          chairs[row].pop(i)
          chairs[row].insert(i, 0)
          print("Revers succes")
          key = False
      if key == True:
        print("This chair has been reserved")

  elif option == "2":
    for i in range(number_chairs):
      for j in range(number_chairs_row):
        if chairs[i][j] < 10:
          print(chairs[i][j],end="  ")
        else:
          print(chairs[i][j],end=" ")
      print()
  elif option == "3":
    enter = False
  else:
    print("This option dont exist, try again\n")