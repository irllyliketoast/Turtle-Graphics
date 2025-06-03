# =======================================================================================
# Name: Laura Estremera
# Date: December 2nd 2023
# Lab 8 - Turtle Graphics
# Objective: Create a screensaver image or piece of art using turtle graphics and loops.
# I would like to see you use multiple colors and multiple sizes of whatever shapes you
# choose to use. I DO NOT want you to just find an image and display it, I want you to
# create the art work. Be creative.
# References: I looked up multiple youtube videos
# Idea: do something simple like a leaf or a flower
# =======================================================================================

# Import statements
import turtle
import random

# Function to draw a petal
# t as turtle
def draw_petal(t, size):
    """
    First function will draw the petals, it wil take turtle graphics along with the desired size of the petals.
    This function will set the desired color and begin filling in the shape os the petal.
    The arc should be determined by the radius aka size and desired angle, x. Then we will turn the turtle the
    supplementary angle (180-x) of the desired angle, x. Then draw second arc of the petal and then end the fill.
    :param t:
    :param size:
    :return: None
    """
    t.color("purple")  # Set the drawing color
    t.begin_fill()     # Begin filling the shape with the current color
    t.circle(size, 60)  # Draw the first arc of the petal
    t.left(120)         # Turn the turtle to draw the second arc
    t.circle(size, 60)  # Draw the second arc of the petal
    t.end_fill()       # End filling the shape

# Function to draw a flower
def draw_flower(t):
    """
    This function is going to have a repeating function that wll draw random sized petals using
    the prior function and then turn the turtle by the desired angle, x.
    :param t:
    :return: None
    """
    for _ in range(6):  # Six petals to form a flower
        draw_petal(t, random.randint(30, 50))  # Draw a petal with a random size
        t.left(60)  # Turn the turtle for the next petal

# Function to move the turtle to a random position on the screen
def move_to_random_position(t):
    """
    This function will lift the pen and generate a random x and y coordinate in a certain range
    then move the turtle into the position. Lowering the pen to draw.
    :param t:
    :return: None
    """
    t.penup()  # Lift the pen to move without drawing
    x = random.randint(-200, 200)  # Generate a random x-coordinate
    y = random.randint(-200, 0)    # Generate a random y-coordinate
    t.goto(x, y)  # Move the turtle to the specified position
    t.pendown()  # Lower the pen to start drawing again

# Main function
def create_flower_screensaver():
    """
    This function will create the turtle screen and set the background color to white
    Create a turtle artist and then set the desired speed. Once this is done we should repeat
    moving the turtle to a random position and drawing a flower, 5 times.
    Lastly, hide the turtle and keep the screen open.
    :return: None
    """
    # I watched a lot of Youtube videos for this part specifically since I had never used turtle before
    screen = turtle.Screen()  # Create a turtle screen/background
    screen.bgcolor("white")   # Set the background color to white

    artist = turtle.Turtle()  # Create a turtle artist
    artist.speed(2)           # Set the drawing speed

    for i in range(5):  # Draw five flowers to create a screensaver
        move_to_random_position(artist)  # Move the turtle to a random position
        draw_flower(artist)              # Draw a flower using the turtle

    artist.hideturtle()  # Hide the turtle after drawing
    screen.mainloop()   # Keep the window open

# Run the flower screensaver
create_flower_screensaver()
