import random
import turtle
turtle.colormode(255)
color=[(211, 154, 98), (53, 107, 131), (177, 78, 33), (198, 142, 35), (116, 155, 171), (124, 79, 98), (123, 175, 157), (226, 197, 130), (190, 88, 109), (12, 50, 64), (56, 39, 19)]
timmy=turtle.Turtle()
timmy.speed("fastest")
timmy.up()
timmy.ht()
timmy.setheading(135)
timmy.fd(225)
timmy.setheading(0)
def painting():
    timmy.down()
    timmy.dot(20,color[random.randint(0,len(color)-1)])
    timmy.up()
    timmy.fd(50)
def origin():
    timmy.setheading(270)
    timmy.fd(50)
    timmy.setheading(180)
    timmy.fd(500)
    timmy.setheading(0)
    timmy.down()
for i in range(10):
    for j in range(10):
        painting()
    origin()
screen=turtle.Screen()
screen.exitonclick()