from ball import Ball
from paddle import Paddle
from level import Level

from constants import (
    BALL_MOVEMENT_DISTANCE,
    BALL_PADDLE_COLLISION_MARGIN,
    PADDLE_STRETCH_WIDTH,
    BRICK_WIDTH,
    BRICK_HEIGHT,
    BALL_RADIUS
)

PADDLE_HALF_WIDTH = (PADDLE_STRETCH_WIDTH / 2) * 20


class Game:
    def __init__(self):
        self.ball = Ball()
        self.paddle = Paddle()
        self.level = Level(1)
        pass

    def paddle_ball_collision(self):
        """Check and handle collisions with the paddle."""
        # Check y level with acceptable margin
        if self.paddle.ycor() >= self.ball.ycor() >= self.paddle.ycor() - BALL_PADDLE_COLLISION_MARGIN:
            ratio = (self.ball.xcor() - self.paddle.xcor()) / PADDLE_HALF_WIDTH

            if -1 <= ratio <= 1:
                # collision
                self.ball.bounce_from_paddle(ratio)

    def ball_brick_collision(self):
        for brick in self.level.bricks:

            ball_left = self.ball.xcor() - BALL_RADIUS
            ball_right = self.ball.xcor() + BALL_RADIUS
            ball_top = self.ball.ycor() + BALL_RADIUS
            ball_bottom = self.ball.ycor() - BALL_RADIUS

            brick_left = brick.xcor() - BRICK_WIDTH / 2
            brick_right = brick.xcor() + BRICK_WIDTH / 2
            brick_top = brick.ycor() + BRICK_HEIGHT / 2
            brick_bottom = brick.ycor() - BRICK_HEIGHT / 2

            horizontal_collision = (
                    ball_right >= brick_left
                    and ball_left <= brick_right
            )

            vertical_collision = (
                    ball_top >= brick_bottom
                    and ball_bottom <= brick_top
            )

            if horizontal_collision and vertical_collision:
                self.level.remove_brick(brick)
                self.ball.bounce_from_brick()
                break

    def game_loop(self, screen):

        if self.ball.is_launched:
            self.ball.move()
            self.ball.check_collision()
            self.paddle_ball_collision()
            self.ball_brick_collision()
        else:
            self.ball.follow(self.paddle)

        screen.ontimer(lambda: self.game_loop(screen), 10)
