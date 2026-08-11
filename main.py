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

game = Game()

screen.listen()
screen.onkey(game.paddle.move_left, LEFT_BTN)
screen.onkey(game.paddle.move_right, RIGHT_BTN)
screen.onkey(game.ball.launch, BALL_LAUNCH_BTN)
# screen.onkey(game.clear_level, "c")

game.game_loop(screen)
screen.mainloop()