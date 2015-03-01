# implementation of card game - Memory

import simplegui
import random
CARDS = range (0,8) + range (0,8)
Turns = 0


# helper function to initialize globals
def new_game():
    global state,exposed,card_opened,Turns
    state = 0
    random.shuffle(CARDS)
    exposed = [False] * 16
    card_opened = []
    state = 0
    Turns = 0
    

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state,card_opened,Turns


    indx = pos[0]/50   
   
    if state == 0:
        card_opened.append(indx)
        exposed[indx] = True
        state = 1
        
    elif state == 1:
        if (indx in card_opened) == False:
            card_opened.append(indx)
            exposed[indx] = True
            Turns += 1
            label.set_text("Turns = " + str(Turns))
            state = 2
    else:      
        if (indx in card_opened) == False:
            if CARDS[card_opened[-1]] != CARDS[card_opened[-2]]:
                exposed[card_opened[-1]] = False
                exposed[card_opened[-2]] = False
                card_opened.pop()
                card_opened.pop()
            exposed[indx]=True
            card_opened.append(indx)
            state = 1
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global card_pos, CARDS, exposed
    
    for c in range(16):
        canvas.draw_polygon([[c*50, 0],[c*50+50,0],[c*50+50,100],[c*50,100]], 1, "Black", "Green")
        if exposed[c] is True:
            canvas.draw_text(str(CARDS[c]), [50*c,80], 90, "White", "sans-serif")



# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(Turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_canvas_background('Red')
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
