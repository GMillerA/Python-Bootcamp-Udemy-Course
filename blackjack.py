# -*- coding: utf-8 -*-
"""
Milestone Project 2
Blackjack Game
"""
from __future__ import print_function
from IPython.display import clear_output
import itertools
import random

clear_output
def blackjack():

    while True:
        print("Welcome to Blackjack!")
        #Set up Game
        set_up()
        #Take turns
        play()
        #win check
        check_win()
        #replay?
        if replay() == False:
            break
    
def set_up():

    class Player(object):
        '''
        Class for Player in Blackjack Game
        '''
        def __init__(self,name,hand=list(), val = 0):
            self.name = name
            self.hand = hand
            self.val = val

            
    global player
    s = raw_input("Enter Player Name: ")
    player = Player(name=s)
    
    
    global dealer
    dealer = Player(name="dealer")
   
    #Set Up Deck
    vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    suits = ['spades', 'clubs', 'hearts', 'diamonds']

    class Card(object):
        def __init__(self, rank, suit):
            self.rank = rank
            self.suit = suit
        def __repr__(self):
            letters = {1:'A', 11:'J', 12:'Q', 13:'K'}
            letter = letters.get(self.rank, str(self.rank))
            return "<Card %s %s>" % (letter, self.suit)
    
    global deck
    deck = list()
    global d
    d = list(itertools.product(vals, suits))
        
    for i in range(52):
        newcard = Card(rank = d[i][0], suit = d[i][1])
        deck.append(newcard)
    
    random.shuffle(deck)
    
    
def play():
    #player goes first
    print ("Dealing Cards")
    player.hand = list()
    player.hand.append(deck.pop())
    player.hand.append(deck.pop())
    print ("You have these cards: ")
    print (player.hand)
    #Dealer is dealt cards
    dealer.hand = list()
    dealer.hand.append(deck.pop())
    dealer.hand.append(deck.pop())
    
    
    #Take turns
    player_turn()
    dealer_turn()
    
    
def handvalue(Player):
    s = 0
    for i in Player.hand:
        v = {'ace':1, '2': 2, '3':3, '4':4, '5':5,'6':6, '7':7, '8':8,'9':9, '10':10, 'jack':11, 'queen':12,'king':13}
        
        s += v[i.rank]
    Player.val = s 
    
def check_win():
    pval = player.val
    dval = dealer.val 
    p_diff = 21 - pval
    d_diff = 21 - dval
    if pval == 21 or dval >= 21 or p_diff < d_diff:
        print ("You are the winner!")
        
    else:
        print ("Dealer is the wnner!")
        

def replay():
    s = raw_input("Want to Play Again? ")
    if s == "Yes" or s == "yes":
        blackjack()
    if s == "No" or s == "no":
        return False
        

        
def player_turn():
    print ("It's your turn!")
    while True: 
        t = raw_input("Hit or Stay: ")
        while t == "hit" or t == "Hit":
            player.hand.append(deck.pop())
            print ("You have these cards: ")
            print (player.hand)
            t = raw_input("Hit or Stay: ")
        if t == "stay" or t == "Stay":
            break 

def dealer_turn():
    dval = dealer.val
    while dval < 15: 
        dealer.hand.append(deck.pop())
        handvalue(dealer)
        dval = dealer.val
