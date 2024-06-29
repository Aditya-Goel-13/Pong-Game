from turtle import Turtle


class Score(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(pos)
        self.i = 0
        self.write(arg=self.i, font=("Courier", 55, "normal"))

    def scores(self):
        self.i += 1
        self.clear()
        self.write(arg=self.i, font=("Courier", 55, "normal"))

    def win(self, win):
        self.goto(-350, 0)
        self.color("Blue")
        self.write(arg=win, font=("Courier", 70, "normal"))

