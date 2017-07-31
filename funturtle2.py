import turtle 
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3
direction = UP
UP_ARROW = "Up"
LEFT_ARROW = "Left"
DOWN_ARROW = "Down"
RIGHT_ARROW = "Right"
SPACE_BAR = "space"
def up():
    global dirction
    direction = UP
    print("you pressed up")
    turtle.pos()
    old_pos = turtle.pos()
    x= old_pos[0]
    y= old_pos[1]
    turtle.goto(x , y+10)
    print(turtle.pos)
def down():
    global  direction
    direction = DOWN
    print("you pressed down")
    turtle.pos()
    old_pos = turtle.pos()
    x= old_pos[0]
    y= old_pos[1]
    turtle.goto(x , y-10)
    print(turtle.pos)
    
def left ():
    global dirction
    direction = LEFT
    print("you pressed left")
    turtle.pos()
    old_pos = turtle.pos()
    x= old_pos[0]
    y= old_pos[1]
    turtle.goto(x -10,y)
    print(turtle.pos)
def right ():
    global direction
    direction = RIGHT
    print("you pressed right")
    turtle.pos()
    old_pos = turtle.pos()
    x= old_pos[0]
    y= old_pos[1]
    turtle.goto(x+10 , y)
    print(turtle.pos)
    
turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.onkeypress(turtle.stamp, SPACE_BAR)
turtle.listen()
