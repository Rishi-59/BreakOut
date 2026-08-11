import turtle

from constants import (
    BRICK_SCORE,
    BALL_LOST_PENALTY,
    LEVEL_SCORE_MULTIPLIER,
    HIGH_SCORE_FILE,
    SCOREBOARD_COLOR,
    SCOREBOARD_Y,
    SCOREBOARD_FONT
)


class ScoreBoard:
    def __init__(self):
        self.score = 0
        self.high_score = self._load_high_score()

        self.display = turtle.Turtle()
        self.display.hideturtle()
        self.display.penup()
        self.display.color(SCOREBOARD_COLOR)
        self.display.goto(0, SCOREBOARD_Y)
        self.update_display(1,3)

    @staticmethod
    def _load_high_score():
        with open(HIGH_SCORE_FILE, "r") as file:
            return int(file.read().strip())

    def _save_high_score(self):
        with open(HIGH_SCORE_FILE, "w") as file:
            file.write(str(self.high_score))

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self._save_high_score()

    def brick_destroyed(self):
        self.score += BRICK_SCORE

    def ball_lost(self):
        self.score -= BALL_LOST_PENALTY

    def level_completed(self, level):
        self.score += level * LEVEL_SCORE_MULTIPLIER

    def reset_score(self):
        self.score = 0

    def update_display(self, level, lives):
        self.display.clear()

        self.display.write(
            f"Score: {self.score}    "
            f"High Score: {self.high_score}    "
            f"Lives: {lives}    "
            f"Level: {level}",
            align="center",
            font=SCOREBOARD_FONT
        )
