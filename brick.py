import random
import turtle

from constants import (
    BRICK_STRETCH_WIDTH,
    BRICK_STRETCH_HEIGHT,
    BRICK_COLORS
)


class Brick:

    def __init__(self, x, y):
        self.brick = turtle.Turtle()
        self.brick.speed(0)
        self.brick.shape("square")
        self.brick.color(random.choice(BRICK_COLORS))
        self.brick.shapesize(
            BRICK_STRETCH_HEIGHT,
            BRICK_STRETCH_WIDTH
        )
        self.brick.penup()
        self.brick.goto(x, y)

    def destroy(self):
        self.brick.hideturtle()

    def xcor(self):
        return self.brick.xcor()

    def ycor(self):
        return self.brick.ycor()