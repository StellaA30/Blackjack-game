import random
import os
import time
from deck import init_cards
from deck import random_cards
from deck import calculate_score
from deck import compare_scores


def clear():
    os.system("clear")


def play():
    
    cards = init_cards()
    
    # define two empyty lists to store the player and dealer's cards
    user_cards = []
    computer_cards = []

    # a boolean which will be used to end the game if the dealer or player has a blackjack or if the user's score is over 21.
    end_game = False


    # this for loop is to deal the user and dealer's 2 cards using the random_cards() funnction.
    for i in range(2):
        user_cards.append(random_cards(cards))
        computer_cards.append(random_cards(cards))


    while not end_game:
    # calculate the player and dealer score from the first two cards
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f'Your cards are: {user_cards} and current score is: {user_score}')
        print(f"The dealer's first card is: {computer_cards[0]}")
        

        # the game ends if the dealer or the player has a blackjack (value 0) or if the player's score is over 21. 
        if user_score == 21 or computer_score == 21 or user_score > 21:
            end_game = True
        else:
            #if the game has not ended, the player can choose to 'hit' (draw a card) or 'stand' (stop drawing cards)
            user_deal = input("Type 'hit' to get another card or type 'stand' to pass: ").lower()
            if user_deal == 'hit':
                user_cards.append(random_cards(cards))
            else:
                end_game=True

    '''
    Dealer strategy
    the dealer has to hit until he/she busts or has at least 17
    
    '''
    while computer_score != 21 and computer_score < 17:
        computer_cards.append(random_cards(cards))
        # print(f"The dealers cards are: {computer_cards[:-1]}")
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final socre: {user_score}")
    print(f" The dealer's final hand: {computer_cards}, final score: {computer_score}")

    print(compare_scores(computer_score, user_score))
    # print(cards)
    # print(len(cards))

 




if __name__ == '__main__':
    clear()
    play()
