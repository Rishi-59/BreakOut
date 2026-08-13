from ball import Ball
from paddle import Paddle
from level import Level
from scoreboard import ScoreBoard

from constants import (
    PADDLE_STRETCH_WIDTH,
    BRICK_WIDTH,
    BRICK_HEIGHT,
    BALL_RADIUS,
    STARTING_LIVES
)

PADDLE_HALF_WIDTH = (PADDLE_STRETCH_WIDTH / 2) * 20


class Game:
    def __init__(self):
        self.level_count = 1
        self.ball = Ball()
        self.paddle = Paddle()
        self.level = Level(self.level_count)
        self.scoreboard = ScoreBoard()
        self.lives = STARTING_LIVES
        self.is_game_over = False

    def paddle_ball_collision(self):
        """Check and handle collisions with the paddle."""
        # Only a downward-moving ball can strike the top of the paddle.
        # Using the ball's bounds also makes this work at increased speed.
        paddle_top = self.paddle.ycor() + BALL_RADIUS
        ball_bottom = self.ball.ycor() - BALL_RADIUS
        horizontal_distance = abs(self.ball.xcor() - self.paddle.xcor())

        if (
            self.ball.dy < 0
            and ball_bottom <= paddle_top
            and self.ball.ycor() >= self.paddle.ycor()
            and horizontal_distance <= PADDLE_HALF_WIDTH + BALL_RADIUS
        ):
            ratio = max(-1, min(1, (self.ball.xcor() - self.paddle.xcor()) / PADDLE_HALF_WIDTH))
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
                self.scoreboard.brick_destroyed()
                self.update_ui()
                x_overlap = (
                        BRICK_WIDTH / 2 + BALL_RADIUS
                        - abs(self.ball.xcor() - brick.xcor())
                )

                y_overlap = (
                        BRICK_HEIGHT / 2 + BALL_RADIUS
                        - abs(self.ball.ycor() - brick.ycor())
                )

                if x_overlap < y_overlap:
                    self.ball.bounce_horizontal()
                else:
                    self.ball.bounce_vertical()

                self.level.remove_brick(brick)
                break

    def next_level(self):
        self.ball.update_speed('level')
        self.ball.reset_position()
        self.paddle.reset()

        self.scoreboard.level_completed(self.level_count)
        self.update_ui()

        self.level_count += 1
        self.level = Level(self.level_count)

    def game_over(self):
        self.scoreboard.update_high_score()
        self.update_ui()
        self.is_game_over = True

    def handle_ball_loss(self):
        if self.ball.is_lost():
            self.lives -= 1
            self.scoreboard.ball_lost()
            self.update_ui()

            if self.lives > 0:
                self.ball.reset_position(reset_speed=True)
                self.paddle.reset()
            else:
                self.game_over()

    def update_ui(self):
        self.scoreboard.update_display(
            self.level_count,
            self.lives
        )

    def increase_ball_speed(self, screen):
        if not self.is_game_over:
            self.ball.update_speed("time")

        screen.ontimer(
            lambda: self.increase_ball_speed(screen),
            10_000
        )

    def game_loop(self, screen):
        if not self.is_game_over:
            if self.ball.is_launched:
                # Test collisions after every small increment.  This prevents
                # a faster ball from tunnelling through bricks or the paddle.
                steps = self.ball.movement_steps()
                for _ in range(steps):
                    self.ball.move_step(steps)
                    self.ball.check_collision()
                    self.paddle_ball_collision()
                    self.ball_brick_collision()

                    if self.ball.is_lost():
                        self.handle_ball_loss()
                        break

                    if self.level.check_level_end():
                        self.next_level()
                        break

            else:
                self.ball.follow(self.paddle)

        screen.ontimer(lambda: self.game_loop(screen), 10)

# def clear_level(self):
#     for brick in self.level.bricks[:]:
#         self.level.remove_brick(brick)
