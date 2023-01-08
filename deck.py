import random
import itertools

print("let's play a game of Blackjack!!")



'''
init_card() function for the 52 deck of cards
initially assigned ace to 11 and it's going to count as 11 unil the user goes over 21
all cards with J Q, K counts as 10, hence why the additional 3 10s
'''

def init_cards():
    deck = []
    card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    #initials of Spades, Hearts, Clubs and Diamonds
    suits = ['S', 'H', 'C', 'D']
    for suit in suits:
        for num in card:
            deck.append(suit+str(num))
    return deck



''' A function that takes cards and randomly selects one card'''
def random_cards(deck):
    random_card = random.choice(deck)
    random_card_num = int(random_card[1:]) #take the integer part of the randmoly chosen card
    deck.remove(random_card) #remove the card from the deck after dealing 
    return random_card_num 



'''A function that calculates the scores of randomly selected cards '''
def calculate_score(card_list):
    # if 10 in card_list and 11 in card_list and len(card_list) == 2:
    #checking for a blackjack (ace +10)
    if len(card_list)==2 and sum(card_list)==21:
        return 21 
    #check for an ace (11) and replace with 1 if score is over 21
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)

    return sum(card_list)



'''Function to compare the dealings'''
def compare_scores(computer_score, user_score):

    if user_score > 21 and computer_score > 21:
        return "You went over, you lose"

    if user_score == computer_score:
        return "Draw, Push!"
    elif computer_score == 21:
        return "You lose, Dealer wins!"
    elif user_score == 21:
        return "Blackjack , you win!"
    elif user_score > 21:
        return "You bust, Dealer wins!"
    elif computer_score > 21:
        return " Dealer went over, you win!"
    elif user_score > computer_score:  #in the case when both less than 21 but user score is higher than computer score
        return "You win"
    else:
        return "You lose!!!"

