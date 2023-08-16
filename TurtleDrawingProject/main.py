import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Pyhton Turtle")
turtle_instance = turtle.Turtle()
# square
''' 
turtle_instance.forward(100)
for i in range(3) :
 turtle_instance.right(90)
 turtle_instance.forward(100)
'''
# star
'''
turtle_instance.forward(100)
for i in range(5):
    turtle_instance.right(120)
    turtle_instance.forward(100)
    turtle_instance.left(48)
    turtle_instance.forward(100)
'''
# polygon
num_sides = 7
angle = 360.0 / num_sides
side_lenght = 100
for i in range(num_sides):
    turtle_instance.right(angle)
    turtle_instance.forward(side_lenght)

''' 
turtle_instance.forward(100)
turtle_instance2 = turtle.Turtle()
turtle_instance2.left(45)
turtle_instance2.forward(100)
'''

turtle.done()