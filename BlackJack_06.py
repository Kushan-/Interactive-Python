# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.CARD = []

    def __str__(self):
        # return a string representation of a hand
        ans = " "
        for i in range(len(self.CARD)):

            ans += str(self.CARD[i])
        return ans
       

    def add_card(self, card):
        # add a card object to a hand
        self.card = card
        self.CARD.append(self.card)
    

    def get_value(self):
        Total = []
        aces = 0
        value = 0
        for k in self.CARD:
            val = k.get_rank()
            value += VALUES[val]

        if value <= 11:
            for k in self.CARD:    
                if k.get_rank() == "A":
                    if aces == 0:
                        value += 10
                        aces += 1    
        return value            

    def draw(self, canvas, pos):
        for d in self.CARD:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(d.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(d.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0] + 73 * self.CARD.index(d), pos[1] + CARD_CENTER[1]], CARD_SIZE)
 
        
# define deck class
class Deck:
    def __init__(self):
        # create a Deck object
        self.DECK = []
        for s in SUITS:
            for r in RANKS:
                test = Card(s,r)
                self.DECK.append(test)	

    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.DECK)

    def deal_card(self):
        # deal a card object from the deck
        a = self.DECK.pop()
        return a
            
    
    def __str__(self):
        # return a string representing the deck
        ams = ''
        for i in range(len(self.DECK)):
            ams += ' '
            ams += (str(self.DECK[i]))
        return "Deck contains: " + str(ams)
        
        

#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, my_deck, score
    if in_play:
        score -= 1
        outcome = "player loose"

    my_deck = Deck()
    my_deck.shuffle()
    dealer_hand = Hand()
    player_hand = Hand()
    for i in range(2):
        dealer_hand.add_card(my_deck.deal_card())
        player_hand.add_card(my_deck.deal_card())
        outcome = 'Hit or stand?'
        in_play = True
#    print player_hand
#    print dealer_hand


def hit():
    
    global outcome, in_play, player_hand, dealer_hand, my_deck, score
    if in_play == True:
        player_hand.add_card(my_deck.deal_card())
#        print player_hand.add_card(deck.deal_card())
        
        if player_hand.get_value() > 21:
            outcome = "busted, New Deal?"
            in_play = False
            score -= 1
            return outcome, in_play, score
        outcome = "Hit or stand?"
    
       
def stand():
    
    global outcome, in_play, player_hand, dealer_hand, score, deal_card, my_deck
#    if player_hand.get_value() > 21:
#        outcome = "busted"
#        score -= 1
#        return outcome,score
    if in_play == True:
            while (dealer_hand.get_value()) < 17:
                dealer_hand.add_card(my_deck.deal_card())
                
            in_play = False
            if dealer_hand.get_value() > 21:
                outcome = "Dealer busts, you win. New deal?"
                score += 1
                return score, outcome, in_play
            elif player_hand.get_value() >=  dealer_hand.get_value():
                outcome = "Player wins.New deal?"
                score += 1
                return score, outcome, in_play
            else:
                outcome = "Dealer wins. New deal?"
                score -= 1
                return score, outcome, in_play

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    dealer_hand.draw(canvas, [0, 100])    
    player_hand.draw(canvas, [0, 300])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [0 + CARD_BACK_CENTER[0], 100 + CARD_BACK_CENTER[1]], CARD_SIZE)    
    canvas.draw_text(outcome,[200,260],20,"Black","sans-serif")
    canvas.draw_text("Score: "+str(score),[200,450],30,"White","sans-serif")
    canvas.draw_text("BlackJack",[200,50],35,"orange")
    canvas.draw_text("Dealer",[50,80],25,"yellow")
    canvas.draw_text("Player",[50,290],25,"yellow")

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# deal an initial hand
deal()
# get things rolling
frame.start()


# remember to review the gradic rubric

