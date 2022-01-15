class text_colors: #class to allow text to be printed in different colors
    green = '\033[32m' #GREEN
    yellow = '\033[33m' #YELLOW
    red = '\033[31m' #RED
    white = '\033[0m' #RESET COLOR

def main(): #main function to control gameplay
  player="X" #X makes the first move
  game_grid=["1", "2", "3", "4", "5", "6", "7", "8", "9"] #set grid start state
  display_game_grid(game_grid) #print the grid
  while (game_status(game_grid)): #while the game is still going make a move, display the grid, and check for end game conditions
    player = make_move(game_grid, player)
    display_game_grid(game_grid)
  end_screen(game_grid, player) #call the end game function to end code execution

def end_screen(game_grid, player): #prints a message stating end game state 
  if (tie_game(game_grid) and not is_winner(game_grid)): #if there are no empty spots and no winner then state game was a draw
    print(text_colors.yellow + f"Looks like this round is a draw. Better luck next time!" + text_colors.white)
  else: #otherwise, declare the winner of the game
    if (player=="X"):
      player = "O"
    else:
      player = "X"
    print(text_colors.green + f"Congratulations, {player}! You won this round! Good game!" + text_colors.white)

def display_game_grid(game_grid): #prints the current game board
    print()
    print(f"{game_grid[0]}|{game_grid[1]}|{game_grid[2]}")
    print('-+-+-')
    print(f"{game_grid[3]}|{game_grid[4]}|{game_grid[5]}")
    print('-+-+-')
    print(f"{game_grid[6]}|{game_grid[7]}|{game_grid[8]}")
    print()

def game_status(game_grid): #returns true if game is still in progress
  if (is_winner(game_grid) or tie_game(game_grid)): #tie is false and 
    #if there is a winner or a tie game, return False
    return False
  else:
    return True

def is_winner(game_grid): #returns true if there is a winner
  if(game_grid[0] == game_grid[1] == game_grid[2] or
    game_grid[3] == game_grid[4] == game_grid[5] or
    game_grid[6] == game_grid[7] == game_grid[8] or
    game_grid[0] == game_grid[3] == game_grid[6] or
    game_grid[1] == game_grid[4] == game_grid[7] or
    game_grid[2] == game_grid[5] == game_grid[8] or
    game_grid[0] == game_grid[4] == game_grid[8] or
    game_grid[2] == game_grid[4] == game_grid[6]):
    return True
  else:
    return False

def tie_game(game_grid): #returns true if there is a tie game
  open_spot_count = 0
  for spot in game_grid:
    if (spot != "X" and spot != "O"):
      open_spot_count += 1
  if open_spot_count == 0:
    return True
  else:
    return False

def make_move(game_grid, player): #marks a square and switches players
  selection=int(input(f"{player}: choose a square from 1-9: "))
  if (game_grid[selection-1] == "X" or game_grid[selection-1] == "O"):
    print(text_colors.red + "Sorry, that spot is already taken, try another" + text_colors.white)
    return player
  else:
    game_grid[selection-1] = player
    print (text_colors.green + "Good move!" + text_colors.white)
    if(player=="X"):
      player = "O"
      return player
    else:
      player = "X"
      return player

if __name__ == "__main__": #calls the main function to initiate gameplay
    main()
