import turtle
turtle.shape('turtle')
square = turtle.clone()
square.shape('square')
square.goto(100,100)
turtle.penup
turtle.goto(0,0)
turtle.pendown
turtle.goto(100,0)
turtle.goto(100,100)
turtle.goto(0,100)
turtle.goto(0,0)
triangle = turtle.clone()
triangle.shape("triangle")
triangle.goto(-200,0)
square.goto(150,150)
square.stamp()
square.goto(-220,4)
triangle.stamp()
triangle.goto(-240,10)
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
def down():
    global  direction
    direction = DOWN
    print("you pressed down")
def left ():
    global dirction
    direction = LEFT
    print("you pressed left")
def right ():
    global direction
    direction = RIGHTS
    print("you pressed right")
##turtle.mainloop()
