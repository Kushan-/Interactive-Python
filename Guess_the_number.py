

import random
import math
import simplegui

secret_number = 0
low = 0
high = 100
remaining_guess = 0


# helper function to start and restart the game
def new_game(l,h):
    global low, high
    low = l
    high = h
    global remaining_guess,secret_number
    secret_number = random.randrange(low,high)
    remaining_guess = math.ceil(math.log(high-low+1,2))
    
   

# define event handlers for control panel
def range100():
    global low, high
    high = 100
    low =0
    new_game(low,high)
    
    # remove this when you add your code    
    pass

def range1000():
    global low, high
    high = 1000
    low =0
    new_game(low,high)
    
    
def input_guess(guess):
    guess = int(guess)
    print "Guess was ",guess
    global  remaining_guess 
    remaining_guess =  remaining_guess -1
    if  remaining_guess >=0 :
        print "The Number of remaining guesses", remaining_guess
        if guess <  remaining_guess :
            print "higher ! "
        elif guess >  remaining_guess :
            print "lower"
        elif guess ==  remaining_guess :
            print "correct"
            
    else :
          print "New Game"
          new_game(low,high)
        


frame = simplegui.create_frame("Guess the number",200,200)




frame.add_button("range is 0-100",range100,200)
frame.add_button("range is 0-1000",range1000,200)
frame.add_input("Enter a number",input_guess,200)


new_game(low,high)



