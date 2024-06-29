from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.y = random.choice([-10, 10])
        self.x = random.choice([-10, 10])

    def move(self):
        x_cor = self.xcor() + self.x
        if (self.ycor() >= 280 and self.y > 0) or (self.ycor() <= -280 and self.y < 0):
            self.y *= -1
        y_cor = self.ycor() + self.y
        self.goto(x_cor, y_cor)

    def hit(self, mode):
        if mode == "mad":
            self.y = random.randint(-10, 10)
        self.x *= -1

