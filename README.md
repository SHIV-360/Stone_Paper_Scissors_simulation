# Stone Paper Scissors Simulation

## Overview
This project simulates the classic game of Stone, Paper, Scissors using Python's Turtle graphics module. Over three days, the simulation was built to visually demonstrate object interactions, movement, and transformations in a bounded environment.

---

## Day 1: Setting the Foundation
- Created the game environment using Turtle graphics.
- Designed the boundary box for the simulation.
- Initialized three types of objects (`Stone`, `Paper`, and `Scissors`) with random positions and movement.
- Set up basic collision detection between objects.
- Implemented a simple leaderboard to count the number of each type of object.

---

## Day 2: Implementing Interactions
- Enhanced collision logic to make objects bounce off each other and the boundary.
- Added transformation rules:
  - **Stone** becomes **Paper** when colliding with **Paper**.
  - **Paper** becomes **Scissors** when colliding with **Scissors**.
  - **Scissors** becomes **Stone** when colliding with **Stone**.
- Improved movement behavior for smoother object interactions.

---

## Day 3: Final Touches
- Added logic to check when all objects belong to the same type, declaring a winner.
- Introduced a "Start Simulation" button for better user interaction.
- Enhanced the leaderboard to dynamically update during the simulation.
- Added a final message to announce the winner when the game ends.
- Cleaned up the code for better readability and maintainability.

---

## How to Run the Simulation
1. Install Python if not already installed.
2. Clone the repository:
   ```bash
   git clone https://github.com/SHIV-360/Stone_Paper_Scissors_simulation.git
   cd Stone_Paper_Scissors_simulation
