import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("pink")
drawing_board.title("Squares")
turtle_instance = turtle.Turtle()
turtle_instance.color("green")

for j in range(5, 125, 10):
    for i in range(3):
        turtle_instance.forward(j)
        turtle_instance.right(90)
        turtle_instance.forward(j+2)


turtle.done()