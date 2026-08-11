from brick import Brick

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
