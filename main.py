import turtle
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR, TITLE

screen = turtle.Screen()

screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor(BACKGROUND_COLOR)
screen.title(TITLE)

screen.mainloop()