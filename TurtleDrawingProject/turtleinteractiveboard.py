import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("yellow")
drawing_board.title("Phyton Turtle")

potato = turtle.Turtle()

def k1():
    potato.forward(50)

def k2():
    potato.left(50)

def k3():
    potato.right(50)

def k4():
    potato.back(50)

drawing_board.onkey(k1, "A")
drawing_board.onkey(k2, "Left")
drawing_board.onkey(k3, "Right")
drawing_board.onkey(k4, "Down")

drawing_board.listen()



turtle.done()

