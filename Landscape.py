import turtle
turtle.bgcolor("Sky Blue")
Milly = turtle.Turtle()
Milly.shape("turtle")
Milly.penup()
Milly.color("brown")
Milly.goto(-200,-200)
Milly.left(90)
Milly.pensize(25)
Milly.pendown()
Andy = turtle.Turtle()
Andy.shape("turtle")
Andy.color("Lime Green")
Andy.penup()
Andy.goto(-360,-300)
Andy.pendown()
Andy.pensize(200)
Billy = turtle.Turtle()
Billy.shape("turtle")
Billy.color("Red")
Billy.penup()
Billy.goto(225,250)
Billy.pendown()
Billy.pensize(7)
Roger = turtle.Turtle()
Roger.shape("turtle")
Roger.color("Red")
Roger.penup()
Roger.goto(-225,250)
Roger.pendown()
Roger.pensize(10)
Andy.shape("turtle")
Milly.shape("turtle")
Billy.shape("turtle")
Roger.shape("turtle")
Andy.speed(900)
Milly.speed(5)
Billy.speed(900)
Roger.speed(900)

def Leaf():
    for i in range(18):
        Milly.color("Green")
        Milly.begin_fill()
        Milly.circle(i * 2)
        Milly.right(70)
        Milly.forward(10)
        Milly.end_fill()

def Cloud():
    for i in range(20):
        Milly.color("white")
        Milly.begin_fill()
        Milly.circle(i*2)
        Milly.right(70)
        Milly.forward(10)
        Milly.end_fill()

Milly.forward(160)
Andy.forward(720)
Leaf()
Cloud()
Milly.penup()
Milly.goto(-225,150)
Milly.pendown()
Cloud()


turtle.exitonclick()