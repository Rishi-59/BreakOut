import turtle

from ball import Ball
from paddle import Paddle
from brick import Brick
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BACKGROUND_COLOR,
    TITLE,
    LEFT_BTN,
    RIGHT_BTN,
    BALL_LAUNCH_BTN,
    BRICK_STRETCH_WIDTH,
    BRICK_STRETCH_HEIGHT
)

BRICK_ROWS = 3
BRICKS_PER_ROW = 9

BRICK_GAP = 10

BRICK_START_Y = SCREEN_HEIGHT // 2 - 40
BRICK_START_X = -(SCREEN_WIDTH // 2) + 40

BRICK_WIDTH = BRICK_STRETCH_WIDTH * 20
BRICK_HEIGHT = BRICK_STRETCH_HEIGHT * 20


def get_offset(row):
    if row % 2 == 0:
        return 0

    return (BRICK_WIDTH + BRICK_GAP) / 2

def get_brick_count(row):
    if row % 2 == 0:
        return BRICKS_PER_ROW
    return BRICKS_PER_ROW - 1


def create_bricks():
    bricks = []

    for row in range(BRICK_ROWS):
        offset = get_offset(row)

        for column in range(get_brick_count(row)):
            x = (
                BRICK_START_X
                + offset
                + column * (BRICK_WIDTH + BRICK_GAP)
            )

            y = (
                BRICK_START_Y
                - row * (BRICK_HEIGHT + BRICK_GAP)
            )

            brick = Brick(x, y)
            bricks.append(brick)

    return bricks

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
bricks = create_bricks()

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