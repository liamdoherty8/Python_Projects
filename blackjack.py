import random

class Deck():
	def __init__(self, cardlist):
		self.deck = []
		for card in cardlist:
			self.deck.append(card)

	def shuffle(self):
		random.shuffle(self.deck)

	def deal_card(self):
		return self.deck.pop(0)


class Card():
	def __init__(self, suit, rank, values):
		self.suit = suit
		self.rank = rank
		self.value = values[rank]

	def __str__(card):
		return f"{card.rank} of {card.suit}"


class Player():
	def __init__(self, name, money, hand = []):
		self.name = name
		self.money = money
		self.hand = hand

	def make_choice(self):
		choice = False
		while choice == False:
			choice = input("Would you like to hit or stay? Press H for hit or S for stay: ").upper()
			if choice == 'H' or choice == 'S':
				return choice
			else:
				print("I did not understand your choice! Please choose H or S.")
				choice = False

	def place_bet(self):
		bet = False
		while bet == False:
			try:
				bet = float(input(f"{self.name}, you have {self.money} dollars. Place your bet: "))
				if bet > self.money:
					print("You do not have that much money! Please make a different bet.")
					bet = False
				elif bet <= 50:
					print("You must bet a higher amount (at least $50)! Please make a different bet.")
					bet = False
				elif bet%10 != 0:
					print("You must bet in multiples of 10 dollars! Please make a different bet.")
					bet = False
			except ValueError:
				print("Whoops! You didn't enter a number. Please try again:")
				bet = False
		return bet

	def add_to_hand(self, card):
		self.hand.append(card)
		if card.rank == "Ace":
			if sum_hand(self.hand) < 11:
				card.value = 11
			else:
				card.value = 1

	def display_hand(self):
		for card in self.hand:
			print(card, end = '  ')
		print('\n')

	def clear_hand(self):
		self.hand = []


class Dealer():
	def __init__(self, hand = []):
		self.hand = hand

	def add_to_hand(self, card):
		self.hand.append(card)
		if card.rank == "Ace":
			if sum_hand(self.hand) < 11:
				card.value = 11
			else:
				card.value = 1

	def clear_hand(self):
		self.hand = []

	def display_hand(self):
		for card in self.hand:
			print(card, end = '  ')
		print('\n')


def initialize_game():
	dealer = Dealer()
	name = input("Player, what is your name? Enter here: ")
	print(f"{name}, we are giving you $500 to start the game.")
	player = Player(name, 500)
	suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
	ranks = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", \
				 "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
	values = {"Ace": 1, "Two": 2, "Three": 3, "Four": 4, \
	 			"Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, \
	 			"Ten": 10, "Jack": 10, "Queen": 10, "King": 10}
	card_list = []
	for suit in suits:
		for rank in ranks:
			card_list.append(Card(suit, rank, values))
	return dealer, player, card_list


def sum_hand(hand):
	total = 0
	for card in hand:
		total += card.value
	return total
	

def initialize_game_state(dealer, player, card_list):
	dealer.clear_hand()
	player.clear_hand()
	deck = Deck(card_list)
	deck.shuffle()
	for card in range(2):
		player.add_to_hand(deck.deal_card())
		dealer.add_to_hand(deck.deal_card())
	bet = player.place_bet()
	print("Your first hand is:", end = ' ')
	player.display_hand()
	print("The dealer has: ", dealer.hand[0])
	return deck, bet


def run_game():
	print("Welcome to the Game of BlackJack!")
	new_game = True
	dealer, player, card_list = initialize_game()
	while new_game == True:
		game_on = True
		deck, bet = initialize_game_state(dealer, player, card_list)
		while game_on == True:
			player_choice = player.make_choice()
			if player_choice == 'H':
				player.add_to_hand(deck.deal_card())
				print("Your current hand is:")
				player.display_hand()
				if sum_hand(player.hand) > 21:
					print("Bust! You lose.")
					player.money -= bet
					break
			elif player_choice == 'S':
				player_hand_total = sum_hand(player.hand)
				print("Your total is:  ", player_hand_total)
				while sum_hand(dealer.hand) <= player_hand_total:
					dealer.add_to_hand(deck.deal_card())
					print("The dealer's current hand is:")
					dealer.display_hand()
					if sum_hand(dealer.hand) > 21:
						print("Congratulations! The dealer busted and you won!")
						player.money += bet
						game_on = False
						break
					elif sum_hand(dealer.hand) > player_hand_total:
						print("The dealer beat you! Better luck next time!")
						player.money -= bet
						game_on = False
						break

		if player.money < 50:
			print("You no longer have enough money to play with! Ending game...")
			break
		play_again = False
		while play_again == False:
			play_again = input("Would you like to play again? Y for yes or N for no: ")
			if play_again.upper() == 'Y':
				new_game = True
			elif play_again.upper() == 'N':
				new_game = False
			else:
				print("I did not understand your decision, please try again!")
				play_again = False


if __name__ == "__main__":
	run_game()

