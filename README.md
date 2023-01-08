# Blackjack-game

This project models a single iteration of a game of Blackjack between the dealer and a single player.

## Assumptions made for the game solution
1) The soultion model a single deck of 52 cards
2) The Jack/Queen/King all count as 10 in the deck of cards created (see deck.py)
3) The ace is initially set to 11 and if the score is already over 21, then the ace value changes to 1
4) Cards are removed from the deck as they are drawn
5) The dealer will continue to draw a card as long as the dealer's score is less than 17
6) If both scores for the dealer and player exceeds 21, then the player loses


## How to run code
1) Run the blackjack.py file to play a single round of the game. Ensure that the deck.py is saved in the same directory as the blackjack.py file 
2) deck.py consists of the different functions to deal the cards, compare and calculate scores, etc..

