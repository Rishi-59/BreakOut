from brick import Brick
import turtle

from constants import (
    DIFFICULTY_STEPUP,
    BRICK_ROWS,
    BRICKS_PER_ROW,
    BRICK_GAP,
    BRICK_START_Y,
    BRICK_START_X,
    BRICK_WIDTH,
    BRICK_HEIGHT,
)


class Level:
    def __init__(self, level_number):
        self.level_number = level_number
        self.bricks = []
        self.create_bricks()

        self.next_level_button = turtle.Turtle()
        self.next_level_button.shape("square")
        self.next_level_button.shapesize(stretch_wid=1, stretch_len=5)
        self.next_level_button.color("white")
        self.next_level_button.penup()
        self.next_level_button.goto(0, 0)

        self.next_level_button.hideturtle()

    @staticmethod
    def get_offset(row):
        if row % 2 == 0:
            return 0

        return (BRICK_WIDTH + BRICK_GAP) / 2

    @staticmethod
    def get_brick_count(row):
        if row % 2 == 0:
            return BRICKS_PER_ROW
        return BRICKS_PER_ROW - 1

    def get_row_count(self):
        if self.level_number <= DIFFICULTY_STEPUP:
            return BRICK_ROWS + self.level_number - 1

        return (
                BRICK_ROWS
                + DIFFICULTY_STEPUP - 1
                + (self.level_number - DIFFICULTY_STEPUP) * 2
        )

    def create_bricks(self):
        self.bricks = []

        for row in range(self.get_row_count()):
            offset = self.get_offset(row)

            for column in range(self.get_brick_count(row)):
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
                self.bricks.append(brick)


    def remove_brick(self, brick):
        brick.destroy()
        self.bricks.remove(brick)

    def check_level_end(self):
        return not self.bricks

    def set_next_level_callback(self, callback):
        self.next_level_button.onclick(callback)

    def show_next_level_button(self):
        self.next_level_button.showturtle()

    def hide_next_level_button(self):
        self.next_level_button.hideturtle()
