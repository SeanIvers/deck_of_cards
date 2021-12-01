from classes import deck

bicycle = deck.Deck()
black_jack_deck = deck.BlackJackDeck()

# bicycle.show_cards()

# print(bicycle.cards)

black_jack_deck.show_cards()

def play_game():
    choice = input("Would you like to play a hand of Black Jack? y or n ")
    while choice == "y":

        print("Your hand is:")
        card_1 = black_jack_deck.pick_random_card()
        card_2 = black_jack_deck.pick_random_card()
        

        choice = input("Would you like to play a hand of Black Jack? y or n ")
    
    if choice == "n":
        print("Thanks for playing!")
        return
    
    else:
        print("Please enter a valid choice: ")
        play_game()

play_game()