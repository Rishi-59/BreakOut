import turtle
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PADDLE_COLOR, PADDLE_STRETCH_WIDTH, PADDLE_STRETCH_HEIGHT, \
    PADDLE_BOTTOM_MARGIN, PADDLE_MOVEMENT_DISTANCE, LEFT_BORDER, RIGHT_BORDER, PADDLE_WALL_MARGIN

PADDLE_Y = -SCREEN_HEIGHT / 2 + PADDLE_BOTTOM_MARGIN


class Paddle:
    def __init__(self):
        self.paddle = turtle.Turtle()

        self.paddle.shape("square")
        self.paddle.shapesize(
            PADDLE_STRETCH_HEIGHT,
            PADDLE_STRETCH_WIDTH
        )
        self.paddle.penup()
        self.paddle.color(PADDLE_COLOR)
        self.paddle.speed(100)
        self.paddle.goto(
            0,
            PADDLE_Y
        )

    def move_left(self):
        x = self.paddle.xcor()
        if x - PADDLE_MOVEMENT_DISTANCE > LEFT_BORDER + PADDLE_WALL_MARGIN:
            self.paddle.goto(x - PADDLE_MOVEMENT_DISTANCE, self.paddle.ycor())

    def move_right(self):
        x = self.paddle.xcor()
        if x + PADDLE_MOVEMENT_DISTANCE < RIGHT_BORDER - PADDLE_WALL_MARGIN:
            self.paddle.goto(x + PADDLE_MOVEMENT_DISTANCE, self.paddle.ycor())

    def reset(self):
        self.paddle.goto(
            0,
            PADDLE_Y
        )

    def xcor(self):
        return self.paddle.xcor()

    def ycor(self):
        return self.paddle.ycor()

    def width(self):
        return self.paddle.width()