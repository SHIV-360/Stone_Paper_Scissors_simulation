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

# Classes for objects
class GameObject(turtle.Turtle):
    def __init__(self, obj_type):
        super().__init__(shape="circle")
        self.penup()
        self.color(self.get_color(obj_type))
        self.goto(random.randint(-BOX_SIZE // 2 + 45, BOX_SIZE // 2 - 45),
                  random.randint(-BOX_SIZE // 2 + 45, BOX_SIZE // 2 - 45))
        self.dx = random.choice([-SPEED, SPEED])
        self.dy = random.choice([-SPEED, SPEED])
        self.type = obj_type

    def move(self):
        # Move the object
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

        # Bounce off walls (boundary limits)
        if self.xcor() >= BOX_SIZE // 2 - 20 or self.xcor() <= -BOX_SIZE // 2 + 20:
            self.dx *= -1
        if self.ycor() >= BOX_SIZE // 2 - 15 or self.ycor() <= -BOX_SIZE // 2 + 15:
            self.dy *= -1

    def get_color(self, obj_type):
        return {"stone": "gray", "paper": "white", "scissors": "orange"}[obj_type]

# Create the objects
objects = []
for _ in range(NUM_OBJECTS // 3):
    objects.append(GameObject("stone"))
    objects.append(GameObject("paper"))
    objects.append(GameObject("scissors"))

# Keep the window open
screen.mainloop()
