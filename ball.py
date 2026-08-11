import turtle

from constants import (
    BALL_COLOR,
    SCREEN_HEIGHT,
    BALL_BOTTOM_MARGIN,
    BALL_MOVEMENT_DISTANCE,
    TOP_BORDER,
    LEFT_BORDER,
    RIGHT_BORDER,
    BALL_PADDLE_COLLISION_MARGIN, PADDLE_STRETCH_WIDTH
)


BALL_Y = -SCREEN_HEIGHT / 2 + BALL_BOTTOM_MARGIN
PADDLE_HALF_WIDTH = (PADDLE_STRETCH_WIDTH / 2 ) * 20

class Ball:
    def __init__(self):
        # Movement state
        self.dx = 0
        self.dy = BALL_MOVEMENT_DISTANCE
        self.is_launched = False

        # Create ball
        self.ball = turtle.Turtle()
        self.ball.shape("circle")
        self.ball.penup()
        self.ball.color(BALL_COLOR)
        self.ball.goto(0, BALL_Y)

    def launch(self):
        """Launch the ball."""
        self.is_launched = True

    def move(self):
        """Move the ball according to its current direction and speed."""
        if not self.is_launched:
            return

        new_x = self.ball.xcor() + self.dx
        new_y = self.ball.ycor() + self.dy

        self.ball.goto(new_x, new_y)

    def check_collision(self):
        """Check and handle collisions with the walls."""

        # Top wall
        if self.ball.ycor() >= TOP_BORDER:
            self.dy = -self.dy

        # Left and right walls
        if (
            self.ball.xcor() >= RIGHT_BORDER
            or self.ball.xcor() <= LEFT_BORDER
        ):
            self.dx = -self.dx


    def follow(self, paddle):
        """Move the ball with paddle before launching."""
        self.ball.setx(paddle.xcor())

    def reset(self):
        """Return the ball to its starting position."""
        self.ball.goto(0, BALL_Y)
        self.dx = 0
        self.dy = BALL_MOVEMENT_DISTANCE
        self.is_launched = False

    def bounce_from_paddle(self, ratio):
        self.dx = -ratio * BALL_MOVEMENT_DISTANCE
        self.dy = -self.dy

    def bounce_from_brick(self):
        pass

    def xcor(self):
        """Return the x coordinate of the ball."""
        return self.ball.xcor()

    def ycor(self):
        """Return the y coordinate of the ball."""
        return self.ball.ycor()