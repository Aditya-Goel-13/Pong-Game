from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, i):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.turtlesize(stretch_len=5, stretch_wid=1)
        self.speed("fastest")
        self.goto(i)

    def up(self):
        if self.ycor() < 240:
            self.forward(20)

    def down(self):
        if self.ycor() > -240:
            self.backward(20)

