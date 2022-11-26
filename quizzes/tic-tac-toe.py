#Tic-Tac-Toe Game
ttt = [["■","■","■"],["■","■","■"],["■","■","■"]]
simbols = []
def players():
  enter = True
  while enter != False:
    player1 = input("Select a letter player 1: ").upper()
    player2 = input("Select a letter player 2: ").upper()
    if player1 == player2:
      print("Select diferent simbols")
    else:
      simbols.append(player1)
      simbols.append(player2)
      enter = False
def showttt(a,b):
  n = 1
  print()
  print("  a b c")
  for i in range(t):
    print(n,end=" ")
    for j in range(tt):
      print(ttt[i][j],end=" ")
    print()
    n += 1
  print()
def conditions(simbol):
  enter = True
  while enter != False:
    print("Select column and row, letters columns - numbers rows")
    column = input("Select column: ").lower()
    row = int(input("Select row: "))

    if row < 4:
      if row > 0:
        if column == "a":
          if ttt[row-1][0] != "■":
            print("This cell has already been selected")
          else:
            ttt[row-1].pop(0)
            ttt[row-1].insert(0, simbol)
            enter = False
        elif column == "b":
          if ttt[row-1][1] != "■":
            print("This cell has already been selected")
          else:
            ttt[row-1].pop(1)
            ttt[row-1].insert(1, simbol)
            enter = False
        elif column == "c":
          if ttt[row-1][2] != "■":
            print("This cell has already been selected") 
          else:
            ttt[row-1].pop(2)
            ttt[row-1].insert(2, simbol)
            enter = False
        else:
          print("this column dont exist, write a b or c")
      else:
        print("this row dont exist, write row 1 2 or 3")
    else:
      print("this row dont exist, write row 1 2 or 3")

def win():
  #Diagonals
  if ttt[1][1] == ttt[0][2]:
    if ttt[1][1]  == ttt[2][0]:
      if ttt[1][1] == player1:
        return player1
      elif ttt[1][1] == player2:
        return player2
  if ttt[1][1] == ttt[0][0]:
    if ttt[1][1]  == ttt[2][2]:
      if ttt[1][1] == player1:
        return player1
      elif ttt[1][1] == player2:
        return player2
  #Horizontals
  for h in range(t):
    for j in range(1):
      if ttt[h][0] == ttt[h][1]:
        if ttt[h][0] == ttt[h][2]:
          if ttt[h][0] == player1:
            return player1
          elif ttt[h][0] == player2:
            return player2
  #Verticals
  for v in range(t):
    for j in range(1):
      if ttt[0][v] == ttt[1][v]:
        if ttt[0][v] == ttt[2][v]:
          if ttt[0][v] == player1:
            return player1
          elif ttt[0][v] == player2:
            return player2

def reset():
  option = input("1. New Game or 2. Exit: ")
  if option == "1":
    ttt.clear()
    for add in range(t):
      ttt.append(["■","■","■"])
    simbols.clear()
    return True
  else:
    return False


tt = len(ttt[0])
t = len(ttt)
turn = 0

enter = True
while enter != False:
  if turn == 0:
    players()
  turn += 1
  player1 = simbols[0]
  player2 = simbols[1]
  showttt(t, tt)

  if turn % 2 != 0:
    print("Player 1 - Turn",turn)
    conditions(player1)
  if turn % 2 == 0:
    print("Player 2 - Turn",turn)
    conditions(player2)
    
  winner = win()
  if winner == player1:
    showttt(t, tt)
    print("Player 1 Winner!!!")
    enter = reset()
    turn = 0
  elif winner == player2:
    showttt(t, tt)
    print("Player 2 Winner!!!")
    enter = reset()
    turn = 0
  elif turn == 9:
    showttt(t, tt)
    print("Tie/Empate")
    enter = reset()
    turn = 0
