def initialize_game():
	players = [' ', ' ']
	player1_choice = False
	while player1_choice == False:
		player1_choice = input('Player 1: Would you like X or O? Enter here: ')
		if player1_choice.upper() == 'X' or player1_choice.upper() == "O":
			players[0] = player1_choice.upper()
		else:
			print("Invalid Input! Please try again.")
			player1_choice = False
	game_state = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
	if players[0] == 'X':
		players[1] = 'O'
	elif players[0] == 'O':
		players[1] = 'X'
	return game_state, players

def draw_board(game_state):
	board = f"   |   |   \n {game_state[0][0]} | {game_state[0][1]} | {game_state[0][2]}\n   |   |    \n-----------\n" \
	f"   |   |   \n {game_state[1][0]} | {game_state[1][1]} | {game_state[1][2]}\n   |   |    \n-----------\n" \
	f"   |   |   \n {game_state[2][0]} | {game_state[2][1]} | {game_state[2][2]}\n   |   |   \n"
	print(board)

def player_selection(game_state, players):
	selection = False
	while selection == False:
		selection = input('Enter the row and column in which you would like to play, separated by a space: ')
		selection = selection.split()
		location = [int(spot) for spot in selection]
		if len(location) != 2:
			print("Invalid input! Try again.")
			selection = False
		elif location[0] not in [0,1,2] or location[1] not in [0,1,2]:
			print("Invalid input! Try again.")
			selection = False
		elif game_state[location[0]][location[1]] != ' ':
			print("That spot has already been taken! Try again.")
			selection = False
	game_state[location[0]][location[1]] = players[0]
	return game_state

def is_board_full(game_state):
	for row in game_state:
		for entry in row:
			if entry == ' ':
				return False
	return True

def is_gameover(game_state):
	for i in range(3):
		if game_state[i][0] == game_state[i][1] and game_state[i][0] == game_state[i][2] and game_state[i][0] != ' ':
			return True
	for j in range(3):
		if game_state[0][j] == game_state[1][j] and game_state[0][j] == game_state[2][j] and game_state[0][j] != ' ':
			return True
	if game_state[0][0] == game_state[1][1] and game_state[0][0] == game_state[2][2] and game_state[0][0] != ' ':
		return True
	if game_state[0][2] == game_state[1][1] and game_state[0][2] == game_state[2][0] and game_state[0][2] != ' ':
		return True
	if is_board_full(game_state) == True:
		return True
	return False

def run_game(game_state, players):
	while True:
		game_state = player_selection(game_state, players)
		print("Current Board:")
		draw_board(game_state)
		players = players[::-1]
		if is_gameover(game_state) == True:
			print("Game over!")
			play_again = None
			while play_again == None:
				play_again = input("Would you like to play again? Y for yes or N for no: ")
				if play_again.upper() == 'Y':
					exit = False
					game_state, players = initialize_game()
					run_game(game_state, players)
				elif play_again.upper() == 'N':
					print("Exiting...")
					exit = True
					break
				else:
					exit = False
					print("Invalid selection! Please try again.")
					play_again = None
			if exit:
				break


if __name__ == "__main__":
	game_state, players = initialize_game()
	run_game(game_state, players)
