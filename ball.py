import turtle
import math

from constants import (
    BALL_COLOR,
    SCREEN_HEIGHT,
    BALL_BOTTOM_MARGIN,
    BALL_MOVEMENT_DISTANCE,
    TOP_BORDER,
    LEFT_BORDER,
    RIGHT_BORDER,
    PADDLE_STRETCH_WIDTH,
    BOTTOM_BORDER,
)

BALL_Y = -SCREEN_HEIGHT / 2 + BALL_BOTTOM_MARGIN
PADDLE_HALF_WIDTH = (PADDLE_STRETCH_WIDTH / 2) * 20


class Ball:
    def __init__(self):
        # Movement state
        self.movement = BALL_MOVEMENT_DISTANCE
        self.speed_multiplier = 1.0

        self.dx = 0
        self.dy = self.movement
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

    def movement_steps(self):
        """Move the ball according to its current direction and speed.

        The ball may travel much farther than a brick is thick after its speed
        has increased. Return the number of small increments needed so callers
        can test collisions along the whole path rather than only at its end.
        """
        if not self.is_launched:
            return 0

        distance_x = self.dx * self.speed_multiplier
        distance_y = self.dy * self.speed_multiplier
        # A step smaller than half the ball diameter prevents it from jumping
        # across a paddle or a brick's collision area.
        steps = max(1, math.ceil(max(abs(distance_x), abs(distance_y)) / 4))
        return steps

    def move_step(self, steps):
        """Move one collision-safe increment using the current direction."""
        self.ball.goto(
            self.ball.xcor() + (self.dx * self.speed_multiplier / steps),
            self.ball.ycor() + (self.dy * self.speed_multiplier / steps),
        )

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
        """Move the ball with the paddle before launching."""
        self.ball.setx(paddle.xcor())

    def reset_position(self, reset_speed=False):
        """Return the ball to its starting position."""

        self.ball.goto(0, BALL_Y)
        self.is_launched = False

        # Reset to straight vertical movement
        self.dx = 0
        self.dy = self.movement

        if reset_speed:
            self.speed_multiplier = 1.0

    def bounce_from_paddle(self, ratio):
        """Change direction based on where the ball hits the paddle."""

        self.dx = -ratio * self.movement
        self.dy = -self.dy

    def bounce_horizontal(self):
        """Reverse horizontal direction."""
        self.dx = -self.dx

    def bounce_vertical(self):
        """Reverse vertical direction."""
        self.dy = -self.dy

    def is_lost(self):
        """Return True if the ball has fallen below the screen."""
        return self.ycor() < BOTTOM_BORDER

    def xcor(self):
        """Return the x coordinate of the ball."""
        return self.ball.xcor()

    def ycor(self):
        """Return the y coordinate of the ball."""
        return self.ball.ycor()

    def update_speed(self, reason):
        """Increase ball speed based on the reason."""

        if reason == "time":
            self.speed_multiplier *= 1.01  # +1%

        elif reason == "level":
            self.speed_multiplier *= 1.10  # +10%
