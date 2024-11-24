# Stone_Paper_Scissors_simulation

# Stone Paper Scissors Simulation - Day 1

## Overview
This is a simulation of the classic game Stone, Paper, Scissors using Python's Turtle graphics module. On Day 1, the focus was on setting up the basic environment, initializing the objects, and implementing basic movement and collision detection.

## Day 1 Tasks:
- Set up the initial game window using Turtle graphics.
- Created a boundary box to represent the playing field.
- Initialized 3 types of objects (stone, paper, scissors) and assigned random movement.
- Implemented collision detection between objects.
- Set up a leaderboard that tracks the number of each type of object in the simulation.

## Next Steps:
- Implement object interactions where objects change type upon collision (e.g., Stone vs Paper, Paper vs Scissors).
- Start working on the game logic to declare a winner.


# Stone Paper Scissors Simulation - Day 2

## Overview
On Day 2, the focus was on implementing the core game logic and enhancing the interactions between objects in the simulation.

## Day 2 Tasks:
- Implemented collision response logic:
  - Objects now change direction when they collide.
  - Objects bounce off the boundaries of the playing field.
- Added game mechanics where objects change type upon collision:
  - **Stone** becomes **Paper** when it collides with **Paper**.
  - **Paper** becomes **Scissors** when it collides with **Scissors**.
  - **Scissors** becomes **Stone** when it collides with **Stone**.
- Optimized the collision detection function for efficiency.
- Verified that all object interactions work as expected through testing.

## Next Steps:
- Add a mechanism to check if all objects belong to the same type and declare a winner.
- Implement a graphical user interface (GUI) element to display the leaderboard dynamically during the simulation.

