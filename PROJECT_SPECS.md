# BreakOut — Game Requirements & Development Plan

## 1. Project Overview

Build a classic **Breakout** game from scratch without following a tutorial.

LLM assistance is allowed for:
- Understanding concepts
- Debugging
- Reviewing code
- Suggesting implementation approaches

The game should be developed by understanding and implementing the logic rather than blindly copying a solution.

---

# 2. Core Game Features

The game must contain:

- Player paddle
- Ball
- Bricks
- Score system
- Lives / balls system
- Multiple levels
- Increasing difficulty
- High-score persistence
- Restart functionality
- Basic visual/UI refinement

---

# 3. Game Window

## Requirements

- Create a game window.
- Set a fixed window size.
- Set a meaningful title.
- Use a dark-blue background.
- Keep the play area visually distinct from the UI.

## Decisions

- Window size: **To be decided before implementation**
- Window title: `BreakOut`
- Background: Dark blue

---

# 4. Paddle

## Requirements

- Paddle must be visible at the bottom of the game area.
- Player must be able to move the paddle horizontally.
- Paddle must remain inside the game boundaries.
- Paddle should have a distinctive color that is easy to see against the background.
- Paddle should be visually distinct from the ball.

## Controls

- Left movement: `Left Arrow`
- Right movement: `Right Arrow`

---

# 5. Ball

## Requirements

- Ball should be white.
- Ball should move continuously once launched.
- Ball should bounce when it hits:
  - Left wall
  - Right wall
  - Top wall
  - Paddle
- Ball should destroy a brick when it collides with one.
- Ball should disappear / be considered lost when it passes below the paddle.

## Ball Speed

### Starting Speed

The game should have a defined default ball speed.

The default speed must be stored as a constant so that it can easily be reset.

### Level Speed Increase

When completing a level:

- Increase ball speed by **10%**.

### Time-Based Speed Increase

During gameplay:

- Increase ball speed by **1% every 10 seconds**.

The speed increase should apply to the current ball.

### Reset

Whenever a new ball is created after losing one:

- Reset the ball to the default speed.
- Do not carry the previous ball's increased speed into the new ball.

---

# 6. Ball Launch / Preparation

When a new ball is created:

1. Place the ball on/above the paddle.
2. Stop the ball from moving.
3. Allow the player to move the paddle freely.
4. Allow the player to position the paddle before launching.
5. Launch the ball using the defined launch action.

The exact launch control should be decided before implementation.

---

# 7. Lives / Balls

The player starts with:

**3 balls**

When the ball is lost:

### If balls remain:

1. Remove the lost ball.
2. Deduct the ball-loss score.
3. Check whether another ball is available.
4. Create a new ball.
5. Reset ball speed to the default.
6. Place the ball on the paddle.
7. Allow the player to reposition the paddle.
8. Wait for the player to launch the ball.

### If no balls remain:

1. Stop the game.
2. End the current run.
3. Compare current score with the stored high score.
4. Update the high score if the current score is higher.
5. Save the new high score.
6. Display the final score.
7. Provide a restart option.

---

# 8. Bricks

## Requirements

- Bricks should be arranged in rows and columns.
- Bricks should be destroyed when hit by the ball.
- Each destroyed brick should disappear from the board.
- The number of bricks should increase as the level increases.

## Brick Colors

Bricks should use randomly generated colors.

Possible approach:

- Generate random RGB values.
- Ensure the generated colors remain visible against the dark background.
- Each brick does not necessarily need to have a unique color.

---

# 9. Levels

## Level Progression

The game should contain approximately **10 levels**.

The exact maximum level should be stored as a constant.

Example:

```text
MAX_LEVEL = 10
```

## Completing a Level

A level is completed when:

> All bricks on the current board have been destroyed.

When this happens:

1. Stop normal gameplay.
2. Display a **Next Level** button.
3. Wait for the player to continue.
4. Increase the level number.
5. Generate the next brick layout.
6. Increase the ball speed by 10%.
7. Start the new level.

## Brick Progression

The number of bricks should increase with each level.

The exact progression formula should be decided during implementation.

Example possibilities:

```text
Level 1 → 20 bricks
Level 2 → 24 bricks
Level 3 → 28 bricks
...
```

The progression should be predictable rather than completely random.

## Maximum Level

After the final level is completed:

- Do not generate another level.
- Display a game-completion state.
- Compare/update the high score.
- Provide a restart option.

---

# 10. Score System

## Scoring Rules

| Event | Score Change |
|---|---:|
| Destroy brick | +10 |
| Lose ball | -5 |
| Complete level | `level × 100` |

### Example

Completing Level 3:

```text
3 × 100 = +300 points
```

---

# 11. Score State

The game should maintain:

- Current Score
- High Score
- Current Level
- Remaining Balls

The current score should be reset when the player presses **Restart**.

The high score should **not** be reset when restarting.

---

# 12. High Score Persistence

The high score must persist after closing the game.

## Storage

Store the high score in a text file.

Example:

```text
highscore.txt
```

## Requirements

When the game starts:

1. Check whether the high-score file exists.
2. If it exists, read the stored high score.
3. If it does not exist, use `0` as the high score.
4. Display the high score.

When the game ends:

1. Compare current score with high score.
2. If current score is greater:
   - Update high score.
   - Save it to the text file.
3. Otherwise, keep the existing high score.

---

# 13. Game States

The game should have clearly defined states rather than relying on scattered boolean conditions.

Minimum required states:

```text
READY
PLAYING
LEVEL_COMPLETE
GAME_OVER
GAME_COMPLETE
```

## READY

- Ball is positioned on the paddle.
- Ball is not moving.
- Paddle can move.
- Player can launch the ball.

## PLAYING

- Ball is moving.
- Paddle can move.
- Collision detection is active.
- Score can change.
- Timer-based ball speed increase is active.

## LEVEL_COMPLETE

- All bricks are destroyed.
- Ball movement stops.
- Next Level button is displayed.
- Player cannot continue until the next level is selected.

## GAME_OVER

- No balls remain.
- Gameplay stops.
- Final score is displayed.
- High score is checked.
- Restart is available.

## GAME_COMPLETE

- Maximum level has been completed.
- Gameplay stops.
- Final score is displayed.
- High score is checked.
- Restart is available.

---

# 14. Collision Rules

The game must detect collisions between the ball and:

### Walls

- Left wall → reverse horizontal direction.
- Right wall → reverse horizontal direction.
- Top wall → reverse vertical direction.

### Paddle

- Ball hits paddle → reverse vertical direction.
- Ball should not pass through the paddle.

Optional refinement:

- Paddle position can influence the horizontal direction of the ball.

This should only be implemented if it does not unnecessarily complicate the core project.

### Bricks

When the ball hits a brick:

1. Remove the brick.
2. Add `+10` to the score.
3. Reverse the appropriate ball direction.
4. Check whether any bricks remain.
5. If no bricks remain → complete the level.

---

# 15. Timer-Based Difficulty

The game should gradually become harder while a ball is active.

Every **10 seconds**:

```text
Current Speed × 1.01
```

Example:

```text
Initial speed = 5

After 10 sec  → 5.05
After 20 sec  → 5.1005
After 30 sec  → 5.1515
```

The timer should only operate while the game is actively being played.

It should not continue during:

- READY
- LEVEL_COMPLETE
- GAME_OVER
- GAME_COMPLETE

---

# 16. UI Requirements

The game should display:

- Current Score
- High Score
- Current Level
- Remaining Balls / Lives

## Buttons

Required buttons:

- `Next Level`
- `Restart`

Buttons should use an accent color that contrasts with the game background.

The **Next Level** button should only appear when the current level is complete.

The **Restart** button should be available when appropriate.

---

# 17. Visual Design

## Background

- Dark blue tone.

## Ball

- White.

## Paddle

- Bright / distinctive color.
- Must be easy to see.

## Bricks

- Random RGB-based colors.
- Colors should remain visible against the background.

## Score Labels

- Use a contrasting text color.
- Labels should remain readable throughout gameplay.

## Buttons

- Use a separate accent color.
- Button text should be clearly readable.

The visual design should remain simple. Do not spend excessive development time on aesthetics before the game logic works.

---

# 18. Restart Behaviour

When the player presses **Restart**:

Reset:

- Current score → `0`
- Level → `1`
- Remaining balls → `3`
- Ball speed → default speed
- Bricks → Level 1 configuration
- Game state → `READY`

Do **not** reset:

- High score

The game should then be ready for the player to launch the first ball.

---

# 19. Constants

Game values should be centralized instead of scattered throughout the code.

Likely constants:

```text
WINDOW_WIDTH
WINDOW_HEIGHT

MAX_LEVEL
STARTING_BALLS

DEFAULT_BALL_SPEED
LEVEL_SPEED_INCREASE
TIME_SPEED_INCREASE
SPEED_INCREASE_INTERVAL

BRICK_SCORE
BALL_LOST_SCORE
LEVEL_COMPLETION_SCORE_MULTIPLIER
```

This will make balancing the game much easier later.

---

# 20. Development Order

Implement the game in small, testable stages.

## Phase 1 — Window

- Create window.
- Set title.
- Set dimensions.
- Set background.

### Test

Confirm that the window opens and closes correctly.

---

## Phase 2 — Paddle

- Create paddle.
- Add horizontal movement.
- Restrict movement to the window.

### Test

Verify:
- Left movement works.
- Right movement works.
- Paddle cannot leave the screen.

---

## Phase 3 — Ball

- Create ball.
- Add movement.
- Add wall collisions.
- Add paddle collision.

### Test

Verify the ball can continuously bounce around the play area.

---

## Phase 4 — Bricks

- Generate bricks.
- Detect brick collision.
- Remove destroyed bricks.
- Add score.

### Test

Verify:
- Ball destroys bricks.
- Destroyed bricks disappear.
- Score increases correctly.

---

## Phase 5 — Lives

- Add 3-ball system.
- Detect ball loss.
- Deduct score.
- Create replacement ball.
- Reset ball speed.

### Test

Verify:
- Ball loss works.
- Replacement ball works.
- Game ends after the final ball.

---

## Phase 6 — Levels

- Detect when all bricks are destroyed.
- Create Next Level button.
- Increase brick count.
- Increase ball speed by 10%.
- Implement maximum level.

### Test

Complete a level and verify the entire transition.

---

## Phase 7 — Difficulty

- Add 1% speed increase every 10 seconds.
- Ensure timer only runs during active gameplay.
- Reset timer appropriately for new balls / levels.

### Test

Verify speed changes correctly over time.

---

## Phase 8 — Score & High Score

- Implement scoring rules.
- Create high-score file.
- Read high score at startup.
- Save high score when appropriate.
- Display high score.

### Test

Close and reopen the game to verify persistence.

---

## Phase 9 — Game States

Refactor gameplay around explicit states:

```text
READY
PLAYING
LEVEL_COMPLETE
GAME_OVER
GAME_COMPLETE
```

Ensure each state allows only the appropriate actions.

---

## Phase 10 — UI Refinement

Only after the game is fully functional:

- Improve colors.
- Improve labels.
- Improve buttons.
- Improve brick appearance.
- Improve spacing/alignment.
- Add small visual refinements.

---

# 21. Definition of Done

The project is considered complete when:

- [ ] Game window works
- [ ] Paddle moves correctly
- [ ] Ball moves correctly
- [ ] Ball bounces from walls
- [ ] Ball bounces from paddle
- [ ] Bricks are generated
- [ ] Bricks are destroyed by the ball
- [ ] Brick count increases between levels
- [ ] Score system works
- [ ] Ball-loss penalty works
- [ ] Level-completion bonus works
- [ ] Three-ball system works
- [ ] Replacement ball works
- [ ] Ball speed resets correctly
- [ ] Level speed increase works
- [ ] 10-second speed increase works
- [ ] Next Level functionality works
- [ ] Maximum level works
- [ ] Game Over works
- [ ] Game Complete works
- [ ] Restart works
- [ ] High score is saved
- [ ] High score is loaded
- [ ] High score is displayed
- [ ] UI is readable
- [ ] Game colors are visually consistent

---

# 22. Requirements Freeze

The following decisions are finalized before implementation.

- [x] Window dimensions
  - Vertical rectangle.
  - Height: Use the maximum practical vertical size available on the laptop.
  - Width: Approximately half of the screen width.
  - Exact dimensions will be determined during initial setup.

- [x] Ball launch control
  - `Up Arrow` launches the ball.
  - Ball remains stationary on the paddle until launched.

- [x] Brick progression
  - Maximum: 10 levels.
  - Levels 1–5:
    - Add 1 additional row of bricks per level.
  - Levels 6–10:
    - Add 2 additional rows of bricks per level.
  - Brick layout must remain within the available game area.

- [x] Maximum level
  - 10 levels.

- [x] Paddle dimensions
  - Paddle width: approximately 1/5–1/6 of the game window width.
  - Paddle height will be determined during implementation.

- [x] Default ball speed
  - Use a starting speed that feels appropriate for Turtle's update/movement system.
  - The exact numeric value will be tuned during implementation.
  - Treat the default speed as a constant so it can be reset whenever a new ball is created.

- [x] Paddle influence on ball direction
  - Yes.
  - The paddle's position relative to the ball's impact point should influence the ball's horizontal direction.
  - This is required for meaningful player control.

Once implementation begins, **do not introduce new gameplay features casually**.

If a new idea appears during development:

1. Finish the current requirement first.
2. Record the idea under `Future Improvements`.
3. Only implement it if it is necessary to fix a requirement or bug.

---

# 23. Future Improvements

Ideas that are intentionally outside the current scope:

- Power-ups
- Multiple balls
- Different brick types
- Unbreakable bricks
- Special paddle abilities
- Sound effects
- Music
- Particle effects
- Animated backgrounds
- Difficulty selection
- Pause menu
- Settings menu

These should **not** be implemented unless the core game is already complete.

---

# 24. Development Principle

The primary objective of this project is not to build the most sophisticated Breakout game.

The objective is to practice:

- Requirement gathering
- Breaking a problem into components
- State management
- Collision detection
- Event handling
- Timers
- File handling
- Debugging
- Refactoring
- Incremental development

**Build the simplest implementation that satisfies the defined requirements.**

