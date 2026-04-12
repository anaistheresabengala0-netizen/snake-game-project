# A classic 2D Snake Game

## Overview

This project is a classic **Snake** game implemented in **Python** using **Pygame**.

The player controls a snake moving on a grid, trying to eat food to grow longer while
avoiding walls, poison, and colliding with its own body.

The game includes:

- A main menu with difficulty selection (**EASY**, **MEDIUM**, **HARD**)
- In‑game score and timer display
- Pause / resume
- A game‑over screen

The project is aimed at beginners learning Python, Pygame, and basic game‑loop / OOP concepts.

---
## Contributors

-   Anais Theresa Bengala Nyangono
-   Romaric Lonfonyuy

------------------------------------------------------------------------

## Features

**Menu with difficulty selection**
  - Three buttons: EASY, MEDIUM, HARD.
  - Each difficulty sets a different snake speed.
- **Grid-based playfield**
  - Checkerboard background to visualize cells clearly.
- **Snake movement and growth**
  - Arrow keys to control direction.
  - Snake grows each time it eats food.
- **Food and Poison**
  - Food increases snake length and score.
  - Poison shortens the snake (and may reduce score).
- **Score and Timer**
  - shows current score and elapsed time at the bottom of the screen.
- **Pause and Resume**
  - Press SPACE to pause the game, press again to resume.
- **Game Over detection**
  - Game ends when the snake hits a wall or its own body.
  - Semi‑transparent “GAME OVER” overlay with instructions to return to menu (ESC).



------------------------------------------------------------------------
## Game Algorithm

 ![Snake Game](./game-screenshots/Snake%20game%20algorithm.png)

------------------------------------------------------------------------

## Tech Stack

- **Programming Language:** Python 3
- **Main Library:** Pygame
- **Other Standard Libraries:** `random`, `time`
- **Math Utilities:** `pygame.math.Vector2` (for grid coordinates)

------------------------------------------------------------------------

## Project Structure
   snake-game-project/
```bash
│
├── main.py           # Main game source code
├── README_template.md# Project README
├── appa.png          # Food (apple image)
└── poison.png        # Poison ( rotten apple image)
```
------------------------------------------------------------------------

## Setup Instructions

### 1. Clone the repository
``` bash
git clone https://github.com/anaistheresabengala0-netizen/snake-game-project.git
cd snake-game-project
```

### 2. Install dependencies

``` bash
pip install pygame
```

### 4. Run the project

Make sure you are inside the `snake-game-project` folder, and then run
``` bash
python main.py
```

------------------------------------------------------------------------

## Usage


### Controls

- **Mouse**
  - Click **EASY**, **MEDIUM**, or **HARD** in the menu to start the game at that difficulty.
- **Keyboard**
  - **Arrow keys** change the snake’s direction.
  - **SPACE key:** pause/resume the game while playing.
  - **ESC key:**
    - In GAME scene: return to the main menu.

------------------------------------------------------------------------

## Example Output

*Menu Screen**
  - A teal background with three rounded buttons labeled EASY, MEDIUM, HARD.
  ![Menu Screens](./game-screenshots/Screenshot%202026-04-12%20180714.png)

**Gameplay**
  - A green checkerboard grid.
  - A purple snake moving in 20×20 pixel steps.
  - A food icon (apple) and a poison icon appear at random grid positions.
  - Score and elapsed time shown at the bottom.
    ![Game Screen](./game-screenshots/Screenshot%202026-04-12%20181551.png)

 **Game Over**
  - Darkened screen with GAME OVER in large red text and instructions to return to menu.
   ![Game Over Screens](./game-screenshots/Screenshot%202026-04-12%20181857.png)

------------------------------------------------------------------------

## Challenges & Limitations

-   Self collision and wall collison were harder to implement
-   Pygame functions based on one scene, so you have to clear an entire scene
-   The timer still continuous even if the game is lost or paused.
-   To find the pictures for the snake and poison that pygame could accept was a tricky and tedious
- All logic is on one main.py file which makes it harder to maintain as more features are added.

------------------------------------------------------------------------

## Future Improvements
- We are going to improve the graphics of the snake.
- We are also going to add a possiblity for two players to play th game
------------------------------------------------------------------------

## References
- https://www.pygame.org/docs/
- https://petlja.org/sr-Latn-RS/biblioteka/r/lekcije/pajtonzasvakoga/03_pygame-03_pygame_eng_02_basics
- https://www.geeksforgeeks.org/python/pygame-tutorial/

------------------------------------------------------------------------

## License
MIT License
