# template for "Stopwatch: The Game"
import simplegui
# define global variables
val = 0
scounter = 0
flag = True
x = 0
sucess = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(val):
    d = val%10
    c = val / 10 % 10
    b = (((val / 10) % 60) / 10)
    a = val / 600
    return str(a)+":"+str(b)+str(c)+"."+str(d)
 
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button():
    flag = True
    timer.start()
    
def restart_button():
    global val,x,sucess
    x = 0
    val = 0
    sucess = 0   
def stop_button():
    
    flag = False
    timer.stop()
    #stop_counter(flag)
    global sucess
    global x
    if (val % 10) == 0:
        x += 1
        sucess = sucess+1
        return str(sucess)+"/"+str(x)
    else:
        x = x+1
        return str(sucess)+"/"+str(x)
    flag = False

# define event handler for timer with 0.1 sec interval
def tick():
    global val
    val += 1
    
#def stop_counter(flag):
#    global y
#    global x
#    ifd
#    if (val % 10) == 0:
#        x += 1
#        return str(x)+"/"+str(y)
#    else:
#        y = y+1
#        return str(x)+"/"+str(y)
            
    
#define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(val),[75,100], 30, "White")
    canvas.draw_text(str(sucess) + "/" + str(x),[100,50], 20, "red")
    


    
# create frame
frame = simplegui.create_frame("stopwatch", 200, 200)
timer = simplegui.create_timer(100, tick)

# register event handlers
frame.set_draw_handler(draw_handler)
frame.add_button("Start", start_button)
frame.add_button("Stop", stop_button)
frame.add_button("Restart", restart_button)

# start frame
frame.start()


