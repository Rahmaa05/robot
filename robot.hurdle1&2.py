def kanan():
    turn_left()
    turn_left()
    turn_left()

def lompat():
    move()
    turn_left()
    move()
    kanan()
    move()
    kanan()
    move()
    turn_left()
    
def berkalikali():
    while not at_goal():
        lompat()
        if at_goal():
            done()
berkalikali()