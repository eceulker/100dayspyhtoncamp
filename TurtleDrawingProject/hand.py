import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("purple")
drawing_board.title("Right Hand")
turtle_instance = turtle.Turtle()
turtle_instance.left(140)
turtle_instance.forward(100)
for i in range(2):
    turtle_instance.right(70)
    turtle_instance.forward(25)
turtle_instance.right(40)
turtle_instance.forward(40)
turtle_instance.right(225)
turtle_instance.forward(100)
for j in range(3):
    for i in range(2):
        turtle_instance.right(70)
        turtle_instance.forward(15)
    turtle_instance.right(40)
    turtle_instance.forward(80)
    turtle_instance.left(170)
    turtle_instance.forward(85)
for i in range(2):
 turtle_instance.right(70)
 turtle_instance.forward(10)
turtle_instance.right(40)
turtle_instance.forward(150)
turtle.done()
