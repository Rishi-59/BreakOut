SCREEN_WIDTH = 650
SCREEN_HEIGHT = 900

BACKGROUND_COLOR = "DarkBlue"
TITLE = "BreakOut"

# main.py
LEFT_BTN = "Left"
RIGHT_BTN = "Right"
BALL_LAUNCH_BTN = "space"

# constants.py
PADDLE_COLOR = "White"
PADDLE_STRETCH_WIDTH = 6
PADDLE_STRETCH_HEIGHT = 1
PADDLE_BOTTOM_MARGIN = 30
PADDLE_MOVEMENT_DISTANCE = 20
PADDLE_WALL_MARGIN = 30

# ball.py
BALL_COLOR = "Red"
BALL_BOTTOM_MARGIN = 45
BALL_MOVEMENT_DISTANCE = 10
BALL_PADDLE_COLLISION_MARGIN = -(BALL_BOTTOM_MARGIN - PADDLE_BOTTOM_MARGIN - 20)

# borders
RIGHT_BORDER = SCREEN_WIDTH / 2 - 10
LEFT_BORDER = -SCREEN_WIDTH / 2 + 10
TOP_BORDER = SCREEN_HEIGHT / 2 - 10
BOTTOM_BORDER = -SCREEN_HEIGHT / 2 + 10

# brick.py
BRICK_STRETCH_WIDTH = 3
BRICK_STRETCH_HEIGHT = 1
BRICK_COLORS = [
    "red",
    "orangered",
    "orange",
    "gold",
    "yellow",
    "chartreuse",
    "lime",
    "springgreen",
    "cyan",
    "deepskyblue",
    "dodgerblue",
    "magenta",
    "hotpink",
    "violet",
]