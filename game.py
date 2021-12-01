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
        score = card_1.point_val + card_2.point_val
        print("Your score is: ", score)
        print("--------------------------")
        print("The dealer's hand is:")
        dealer_card_1 = black_jack_deck.pick_random_card()
        dealer_card_2 = black_jack_deck.pick_random_card()
        dealer_score = dealer_card_1.point_val + dealer_card_2.point_val
        print("The dealer's score is: ", dealer_score)

        if dealer_score == 21:
            print("Sorry, you lose.")
            break

        elif score == 21:
            print("You win!")
            break
        
        hit = input("Would you like to hit? y or n ")
        while hit == "y":
            card = black_jack_deck.pick_random_card()
            score += card.point_val
            print(card.point_val)
            print(score)

            if score == 21:
                print("You win!")

            elif score > 21:
                print("Sorry, you lose.")
                break

            hit = input("Would you like to hit? y or n ")

        choice = input("Would you like to play another hand of Black Jack? y or n ")
    
    if choice == "n":
        print("Thanks for playing!")
        return
    
    else:
        print("Please enter a valid choice: ")
        play_game()

play_game()