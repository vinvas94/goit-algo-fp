import turtle
import math

# Set up the turtle
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("white")
t.color("red")

# Function to draw the Pythagorean Tree
def draw_tree(t, length, level):
    if level == 0:
        return

    # Draw the main trunk
    t.forward(length)
    
    # Save the current position and heading
    current_pos = t.position()
    current_heading = t.heading()

    # Draw the right branch
    t.left(45)
    draw_tree(t, length * math.sqrt(2) / 2, level - 1)
    
    # Go back to the main trunk
    t.setposition(current_pos)
    t.setheading(current_heading)

    # Draw the left branch
    t.right(45)
    draw_tree(t, length * math.sqrt(2) / 2, level - 1)
    
    # Go back to the main trunk
    t.setposition(current_pos)
    t.setheading(current_heading)

# Input: Recursion level
level = int(input("Enter the recursion level: "))

# Starting position and angle
t.up()
t.goto(0, -200)
t.down()
t.left(90)

# Draw the Pythagorean Tree
draw_tree(t, 100, level)

turtle.done()