import random
import itertools

print("let's play a game of Blackjack!!")



'''
init_cards() function creates the deck of cards containing 52 card objects.
The ace is initially assigned to 11 and it's going to count as 11 unil the user goes over 21.
The Jack, Queen, King cards counts as 10, hence why the additional 3 10s in the card list
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



''' random_cards() is a function that takes the deck of cards and randomly selects (draws) one card, 
which is then removed from the deck.'''

def random_cards(deck):
    random_card = random.choice(deck)
    random_card_num = int(random_card[1:]) #take the integer part of the randmoly chosen card
    deck.remove(random_card) #remove the card from the deck after dealing 
    return random_card_num 



'''calculate_score() takes a list (of cards) as input and returns the score. 
In this function, we also check for a blackjack and an ace. 
If an ace (11) exists in the list of cards and the total score is over 21, then replace its value of 11 with 1.'''

def calculate_score(card_list):
    # if 10 in card_list and 11 in card_list and len(card_list) == 2 , then blackjack with ace+10
    #checking for a blackjack 
    if len(card_list)==2 and sum(card_list)==21:
        return 21 
    #check for an ace (11) and replace with 1 if score is over 21
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)

    return sum(card_list)



'''Function to compare the scores of the player and computer to see who wins.'''
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
        return "You win, dealer loses"
    else:
        return "You lose!!!"

