# semester project: ride the bus 

import random 

# the rank of the cards 

Ranks = [ '2' , '3', '4', '5', '6', '7', '8' ,'9', 'Queen', 'King', 'Ace' ]
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] 
suit_colors = {'Hearts': 'red', 'Diamonds': 'red', 'Clubs': 'black', 'Spades': 'black'} 

def create_deck(): 
 "make a 52 card deck and shuffle it random" 

 deck = [(rank, suit) for rank in Ranks for suit in suits]  
 random.shuffle(deck) 
 return deck 

def draw_card():
    "draw a card that is from the deck"

def ride_the_bus(): 
    deck = create_deck(deck)
stage = 1 
cards_drawn = ()

print("Welcome to ride the bus! Do you dare to play??? once you start you cannot stop until game over complete all 4 stages to win.\n") 