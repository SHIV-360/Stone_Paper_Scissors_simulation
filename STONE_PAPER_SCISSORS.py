import turtle
import random
import math

# Settings
NUM_OBJECTS = 50  # Total number of objects (gets divided by 3)
BOX_SIZE = 550    # Size of the box
SPEED =  3        # Speed of movement

# Initialize the screen
screen = turtle.Screen()
screen.title("Stone Paper Scissors Simulation")
screen.setup(width=BOX_SIZE + 300, height=BOX_SIZE + 170)
screen.tracer(0)
screen.bgcolor("light green")

# Draw the boundary box (playing field)
border = turtle.Turtle()
border.hideturtle()
border.penup()
border.goto(-BOX_SIZE // 2, BOX_SIZE // 2)
border.pendown()
border.pensize(8)
border.speed(0)
for _ in range(4):
    border.forward(BOX_SIZE)
    border.right(90)

# Add a Start button
start_button = turtle.Turtle()
start_button.hideturtle()
start_button.penup()
start_button.goto(0, BOX_SIZE // 2 - 20)
start_button.write("Click to Start", align="center", font=("Arial", 16, "bold"))

# Keep the window open
screen.mainloop()
