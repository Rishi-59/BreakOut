import turtle
from paddle import Paddle
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR, TITLE

screen = turtle.Screen()

screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor(BACKGROUND_COLOR)
screen.title(TITLE)

paddle = Paddle()

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

screen.mainloop()