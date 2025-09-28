import turtle

screen = turtle.Screen()
screen.screensize(400,400)
screen.title("square spiral")
screen.bgcolor('black')

t = turtle.Turtle()
t.color("purple")

t.width(3)
s = 5

while True:
    t.forward(s)
    t.left(90)
    s += 5
