"""
For this program, you will tell Tina the Turtle to draw 
a pentagon.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.
"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina

# Use tina.forward() and tina.left() to draw a pentagon
# Make each side of the pentagon a different color with 
# tina.pencolor()

lef = 75
top = 90
sides = 100

tina.pencolor('red')
tina.forward(sides)
tina.left(lef)
tina.pencolor('yellow')
tina.forward(sides)
tina.left(lef)
tina.pencolor('blue')
tina.forward(top)
tina.left(65)
tina.pencolor('purple')
tina.forward(90)
tina.left(lef)
tina.pencolor('green')
tina.forward(sides) # Your code here

turtle.exitonclick()                    # Close the window when we click on it