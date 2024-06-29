from turtle import Screen, Turtle
from paddle import Paddle
import time
from ball import Ball
from score import Score


def initialise():
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)
    ini = Turtle()
    ini.speed("fast")
    ini.color("white")
    ini.penup()
    ini.goto(0, 300)
    ini.setheading(270)
    for i in range(0, 610, 10):
        if i % 20 == 0:
            ini.pendown()
        else:
            ini.penup()
        ini.forward(10)


def reset():
    global t
    l_paddle.goto(-390, 10)
    r_paddle.goto(380, 10)
    ball.goto(0, 0)
    ball.x *= -1
    t = 0.06


# initialization
screen = Screen()
initialise()
l_paddle = Paddle((-390, 10))
r_paddle = Paddle((380, 10))
ball = Ball()
t = 0.06
l_point = Score((-55, 225))
r_point = Score((20, 225))
player_1 = screen.textinput(title="Name", prompt="Enter name of Player 1")
player_2 = screen.textinput(title="Name", prompt="Enter name of Player 2")
mode = screen.textinput(title="Mode", prompt="Select Mode(Mad/Normal)").lower()
s = int(screen.textinput(title="Score", prompt="Set Score Limit"))
screen.update()
time.sleep(2)

# for movement
screen.listen()
screen.onkey(fun=r_paddle.up, key="8")
screen.onkey(fun=r_paddle.down, key="2")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")

# game begin
game = True
while game:
    time.sleep(t)
    ball.move()

    # collision with paddle
    if ((abs(ball.ycor() - l_paddle.ycor()) <= 50 and ball.xcor() <= -370 and ball.x < 0) or
            (abs(ball.ycor() - r_paddle.ycor()) <= 50 and ball.xcor() >= 360 and ball.x > 0)):
        ball.hit(mode)
        if t > 0:
            t *= 0.9

    # Left miss
    if ball.xcor() == -400:
        r_point.scores()
        screen.update()
        time.sleep(2)
        reset()

    # right miss
    if ball.xcor() == 390:
        l_point.scores()
        screen.update()
        time.sleep(2)
        reset()

    if l_point.i == s:
        l_point.win(f"{player_1} Wins!")
        game = False

    if r_point.i == s:
        l_point.win(f"{player_2} Wins!")
        game = False
    screen.update()

screen.exitonclick()
