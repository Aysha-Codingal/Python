import turtle

screen = turtle.Screen()
screen.screensize(400,400)
screen.title("polygon")
screen.bgcolor('beige')

t = turtle.Turtle()
t.color("teal")
t.fillcolor('purple')
t.width(5)
n = 6
a = 360/n
t.begin_fill()
for i in range(n):
    t.forward(100)
    t.left(a)
t.end_fill()
turtle.done()    

