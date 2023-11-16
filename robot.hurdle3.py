def lurus():
    while front_is_clear():
        move()
        if at_goal():
            done()
    lompat()
def kanan():
    turn_left()
    turn_left()
    turn_left()
def lompat():
    turn_left()
    move()
    kanan()
    move()
    kanan()
    move()
    turn_left()
    lurus()
lurus()
lompat()
