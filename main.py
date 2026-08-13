import turtle
from game import Game

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

screen.tracer(0)

game = Game(screen)

screen.listen()


game.game_loop()
game.increase_ball_speed()

screen.mainloop()