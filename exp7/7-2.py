import turtle


def draw_pentagon_star(screen, pen):
    pen.speed(3)
    for _ in range(5):
        pen.forward(100)
        pen.right(144)
    pen.penup()


def draw_petal_arcs(screen, pen):
    pen.speed(3)
    pen.penup()
    pen.goto(0, 100)
    pen.pendown()
    for _ in range(5):

        pen.circle(40, 180)
        pen.right(108)


def main():
    screen = turtle.Screen()
    screen.setup(width=1000, height=1000)
    screen.bgcolor('white')

    pen = turtle.Turtle()

    draw_pentagon_star(screen, pen)
    pen.clear()
    draw_petal_arcs(screen, pen)

    turtle.done()



main()
