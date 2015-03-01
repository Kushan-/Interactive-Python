import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
score = 0
# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = [WIDTH/2,HEIGHT/2]
ball_vel = [0,0]
paddle1_pos =  (HEIGHT/2) #+ HALF_PAD_HEIGHT
paddle2_pos = (HEIGHT/2) #+ HALF_PAD_HEIGHT
paddle1_bottom = paddle1_pos + PAD_HEIGHT#(HEIGHT / 2) - HALF_PAD_HEIGHT
paddle2_bottom = paddle2_pos + PAD_HEIGHT #(HEIGHT / 2) - HALF_PAD_HEIGHT
paddle2_vel = 0
paddle1_vel = 0
score1 = 0
score2 = 0


def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, paddle1_bottom, paddle2_bottom  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos = (HEIGHT/2) - HALF_PAD_HEIGHT
    paddle2_pos = (HEIGHT/2) - HALF_PAD_HEIGHT
    paddle1_vel = 0
    paddle2_vel = 0
    paddle1_bottom = paddle1_pos + PAD_HEIGHT
    paddle2_bottom = paddle2_pos + PAD_HEIGHT 
    
    spawn_ball(random.choice([LEFT, RIGHT]))
#    spawn_ball(direction)

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == RIGHT:
        ball_vel[0] = random.randrange(120, 240)/60
        ball_vel[1] =  -random.randrange(60, 180)/60
    elif direction == LEFT:
        ball_vel[0] = -random.randrange(120, 240)/60
        ball_vel[1] = random.randrange(60, 180)/60
    else:
        print "This will never happen."

# define event handlers
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle2_vel, paddle1_vel, paddle1_bottom, paddle2_bottom, paddle2_top
    
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_circle([WIDTH / 2, HEIGHT/2], 50, 2, "White") 
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
 
    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS :
        if paddle1_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT:
            ball_vel[0] *= -1.1
        else:
            score2 += 1
            spawn_ball(RIGHT)
            
    elif ball_pos[0] >= (WIDTH - PAD_WIDTH) - BALL_RADIUS:
        if paddle2_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT:
            ball_vel[0] *= -1.1
        else:
            score1 += 1
            spawn_ball(LEFT)
            
    if ball_pos[1] <= BALL_RADIUS:
       ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1] 
   
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    canvas.draw_text(str(score1),[150, 50], 50, "White", "sans-serif")
    canvas.draw_text(str(score2),[450, 50], 50, "White", "sans-serif")
    
     # update paddle's vertical position, keep paddle on the screen
    if paddle2_pos + paddle2_vel >= HALF_PAD_HEIGHT and paddle2_pos + paddle2_vel < HEIGHT - HALF_PAD_HEIGHT + 10:
            paddle2_pos += paddle2_vel
            
           
    else:
            print "error"
            
    if paddle1_pos + paddle1_vel >= HALF_PAD_HEIGHT and paddle1_pos + paddle1_vel < HEIGHT - HALF_PAD_HEIGHT + 10 :
            paddle1_pos += paddle1_vel
    else:
            print "error"
        
    # draw paddles
    canvas.draw_line([0, paddle1_pos - HALF_PAD_HEIGHT], [0, paddle1_pos + HALF_PAD_HEIGHT], 17, "#00FFFF")

    
    canvas.draw_line([WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH, paddle2_pos + HALF_PAD_HEIGHT], 17, "yellow") 
    
    # draw scores
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos
    acc = 5

    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel += acc
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= acc
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += acc
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= acc        
    
   
def keyup(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos
    if key == simplegui.KEY_MAP["down"]:
            paddle2_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
            paddle2_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
            paddle1_vel = 0
    elif key == simplegui.KEY_MAP["w"]:
            paddle1_vel = 0      
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_canvas_background('green')
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', new_game)



# register event handlers
frame.set_draw_handler(draw)

# start frame
new_game()
frame.start()

