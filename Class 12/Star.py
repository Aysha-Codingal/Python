import turtle

screen = turtle.Screen()
screen.screensize(400,400)
screen.title("Star")
screen.bgcolor('beige')

t = turtle.Turtle()
t.color("teal")
t.fillcolor('lightpink')
t.width(5)
n = 3
a = 360/n
t.begin_fill()
for i in range(n):
    t.forward(100)
    t.left(a)

t.left(90)
t.penup()
t.forward(65)
t.right(90)
t.pendown()

for i in range(n):
        t.forward(100)
        t.right(a)
t.end_fill()
turtle.done()    

