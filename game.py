from ball import Ball
from paddle import Paddle
from level import Level
from scoreboard import ScoreBoard

from constants import (
    BALL_MOVEMENT_DISTANCE,
    BALL_PADDLE_COLLISION_MARGIN,
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
                self.ball.reset_position()
                self.paddle.reset()
            else:
                self.game_over()

    def update_ui(self):
        self.scoreboard.update_display(
            self.level_count,
            self.lives
        )


    def game_loop(self, screen):
        if not self.is_game_over:
            if self.ball.is_launched:
                self.ball.move()
                self.ball.check_collision()
                self.paddle_ball_collision()
                self.ball_brick_collision()
                self.handle_ball_loss()

                if self.level.check_level_end():
                    self.next_level()

            else:
                self.ball.follow(self.paddle)

        screen.ontimer(lambda: self.game_loop(screen), 10)

# def clear_level(self):
#     for brick in self.level.bricks[:]:
#         self.level.remove_brick(brick)
