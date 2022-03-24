# import time
from turtle import Screen
from paddle import Paddle
from ball import PongBall
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = PongBall()
the_scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "a")
screen.onkey(l_paddle.go_down, "q")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()
    # collision with l_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        the_scoreboard.l_add_point()

    # detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        the_scoreboard.r_add_point()


screen.exitonclick()
