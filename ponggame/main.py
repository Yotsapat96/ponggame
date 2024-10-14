from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# game screen
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)

# scoreboard
scoreboard = ScoreBoard()
screen.title("pong")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


# make ball move
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    # detect collision with wall
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()
    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >= 330 or ball.distance(l_paddle) < 50 and ball.xcor() <= -330:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_scored()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_scored()

    screen.update()
    ball.move()
screen.exitonclick()
