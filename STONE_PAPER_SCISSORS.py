import turtle
import random
import math

# Settings
NUM_OBJECTS = 50  # Total number of objects (gets divided by 3)
BOX_SIZE = 550    # Size of the box
SPEED =  0.8        # Speed of movement

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

    def change_type(self, new_type):
        self.type = new_type
        self.color(self.get_color(new_type))


# Create the objects
objects = []
for _ in range(NUM_OBJECTS // 3):
    objects.append(GameObject("stone"))
    objects.append(GameObject("paper"))
    objects.append(GameObject("scissors"))


# Logic to handle collisions and type changes
def check_collisions():
    for i, obj1 in enumerate(objects):
        for j, obj2 in enumerate(objects):
            if i != j and distance(obj1, obj2) < 15: 
                handle_collision(obj1, obj2)

                # Handle type changes
                if obj1.type == "stone" and obj2.type == "paper":
                    obj1.change_type("paper")
                elif obj1.type == "paper" and obj2.type == "scissors":
                    obj1.change_type("scissors")
                elif obj1.type == "scissors" and obj2.type == "stone":
                    obj1.change_type("stone")


def distance(obj1, obj2):
    """Calculate the Euclidean distance between two objects."""
    return math.sqrt((obj1.xcor() - obj2.xcor()) ** 2 + (obj1.ycor() - obj2.ycor()) ** 2)


def handle_collision(obj1, obj2):
    """Adjust the direction of objects based on their collision."""
    # Compute relative positions
    dx = obj1.xcor() - obj2.xcor()
    dy = obj1.ycor() - obj2.ycor()
    angle = math.atan2(dy, dx)

    # Update directions based on collision
    obj1.dx = SPEED * math.cos(angle)
    obj1.dy = SPEED * math.sin(angle)
    obj2.dx = -SPEED * math.cos(angle)
    obj2.dy = -SPEED * math.sin(angle)


# Check if all objects belong to the same type
def check_victory():
    types = {obj.type for obj in objects}
    return len(types) == 1


# Update the live leaderboard
def update_leaderboard():
    counts = {"stone": 0, "paper": 0, "scissors": 0}
    for obj in objects:
        counts[obj.type] += 1

    leaderboard.clear()
    leaderboard.write(
        f"Stone ({counts['stone']}): GRAY   Paper ({counts['paper']}): WHITE   Scissors ({counts['scissors']}): ORANGE",
        align="left",
        font=("Arial", 12, "normal"),
    )


# Main loop
def start_simulation():
    while True:
        screen.update()
        for obj in objects:
            obj.move()
        check_collisions()
        update_leaderboard()
        if check_victory():
            winner = objects[0].type
            leaderboard.clear()
            leaderboard.write(
                f"{winner.upper()} WINS! 🎉",                
                font=("Arial", 12),
            )
            break 


# Add a Start button
start_button = turtle.Turtle()
start_button.hideturtle()
start_button.penup()
start_button.goto(0, BOX_SIZE // 2 - 20) 
start_button.write("Click to Start", align="center", font=("Arial", 16, "bold"))

def start_button_click(x, y):
    if -50 < x < 50 and BOX_SIZE // 2 - 30 < y < BOX_SIZE // 2:
        start_button.clear()
        start_simulation()


# Add a leaderboard for counts
leaderboard = turtle.Turtle()
leaderboard.hideturtle()
leaderboard.penup()
leaderboard.goto(-BOX_SIZE // 2 + 65, BOX_SIZE // 2 + 20)
update_leaderboard()

# Keep the window open
screen.onclick(start_button_click)
screen.mainloop()
