import turtle

from ball import Ball
from paddle import Paddle
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BACKGROUND_COLOR,
    TITLE,
    LEFT_BTN,
    RIGHT_BTN,
    BALL_LAUNCH_BTN,
)

screen = turtle.Screen()

screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor(BACKGROUND_COLOR)
screen.title(TITLE)

paddle = Paddle()
ball = Ball()

screen.listen()
screen.onkey(paddle.move_left, LEFT_BTN)
screen.onkey(paddle.move_right, RIGHT_BTN)
screen.onkey(ball.launch, BALL_LAUNCH_BTN)


def game_loop():
    if ball.is_launched:
        ball.move()
        ball.check_collision()
        ball.paddle_collision(paddle)
    else:
        ball.follow(paddle)

    screen.ontimer(game_loop, 10)


game_loop()
screen.mainloop()