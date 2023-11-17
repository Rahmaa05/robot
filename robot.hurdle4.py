def kanan():
    turn_left()
    turn_left()
    turn_left()
def lompat():
    while front_is_clear():
        move()
        if at_goal():
            done()
    turn_left()
    while wall_on_right():
        move()
    kanan()
    move()
    kanan()
    while front_is_clear():
        move()
    turn_left()
while not at_goal():
    lompat()
