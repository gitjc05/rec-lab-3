# Joaquin Cabra Romero

import turtle


def draw_bowtie(size):
    turtle.pendown()
    turtle.right(30)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size*2)
    turtle.right(120)
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.left(30)
    turtle.right(90)
    turtle.penup()
    turtle.forward(size/4)
    turtle.left(90)
    turtle.pendown()
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.circle(size/4)
    turtle.end_fill()
    turtle.penup()
    turtle.right(90)
    turtle.back(size/4)
    turtle.left(90)

def main():
    turtle.speed(10)
    turtle.pencolor("blue")
    draw_bowtie(80)
    turtle.done()


main()