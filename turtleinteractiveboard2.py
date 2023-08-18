import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("Light blue")
drawing_board.title("Phyton Turtle")

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="space")

turtle.mainloop()