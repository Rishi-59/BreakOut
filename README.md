# BreakOut

A retro-style recreation of the classic Breakout arcade game, built with Python's standard-library `turtle` module. Clear the coloured brick field, protect the ball with the paddle, and build the highest score you can.

## Features

- Paddle, ball, wall, brick, and paddle collision handling
- Collision-safe ball movement that continues to work as ball speed increases
- Three lives per run and a clickable retry button after game over
- Progressive levels with additional brick rows
- Speed increases by 10% after each completed level and by 1% every 10 seconds
- Score, high score, lives, and level display
- Persistent high score stored in `highscore.txt`
- Cyan retro UI buttons and `Press Start 2P` display font

## Requirements

- Python 3.12 or newer
- A Python installation with Tk/Turtle support
- The **Press Start 2P** font installed locally for the intended pixel-font styling (Turtle falls back to an available system font if it is not installed)

No third-party Python packages are required.

## Run the game

From the repository root:

```bash
python3 main.py
```

If you use `uv`:

```bash
uv run main.py
```

## Controls

| Input | Action |
| --- | --- |
| Left Arrow | Move paddle left |
| Right Arrow | Move paddle right |
| Space | Launch the ball |
| Mouse click | Choose **NEXT LEVEL** or **RETRY** when shown |
| `C` | Clear the current level (development shortcut) |

## Scoring

| Event | Score change |
| --- | ---: |
| Destroy a brick | +10 |
| Lose a ball | -5 |
| Complete a level | `level × 100` |

## How it works

You start each run with three lives. Before launch, the ball follows the paddle so you can choose its starting position. Hitting different areas of the paddle changes the ball's horizontal direction.

After every cleared board, click **NEXT LEVEL** to generate a denser brick layout. Speed increases during a run, while losing a ball resets it to the default speed. When all lives are gone, click **RETRY** to start a fresh run; your high score remains saved.

## Project structure

| File | Responsibility |
| --- | --- |
| `main.py` | Configures the Turtle window and starts the game loop |
| `game.py` | Coordinates game state, input, collisions, levels, and retry flow |
| `ball.py` | Ball movement, speed scaling, and wall bouncing |
| `paddle.py` | Paddle rendering and horizontal movement |
| `level.py` / `brick.py` | Brick layout, level progression, and next-level button |
| `scoreboard.py` | Score display and high-score persistence |
| `constants.py` | Centralised gameplay, layout, input, and UI settings |
| `PROJECT_SPECS.md` | Original project requirements and development plan |

## Customisation

Most gameplay and visual values live in `constants.py`, including window dimensions, default ball movement, lives, brick layout, colours, UI fonts, and button sizing.

## License

This project currently has no license specified.
