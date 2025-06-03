# =======================================================================================
# Name: Laura Estremera
# Date: December 2nd, 2023 (Updated in 2025)
# Project: Flower Screensaver – Turtle Graphics (OOP Python Project at UNCW)
# Objective: Create an animated flower-drawing screensaver using Turtle graphics.
# Enhancements:
#   - Prevent flowers from overlapping
#   - Screen size mimics iPhone dimensions (390x844 px)
#   - Gradient coloring (purples & pinks)
#   - Cleaner, more modular code with better documentation
# =======================================================================================

import turtle
import random
import colorsys  # Used to create smooth gradients

# Store previous positions to avoid overlapping flowers
used_positions = []

# Set screen dimensions to mimic iPhone (in turtle units)
SCREEN_WIDTH = 390
SCREEN_HEIGHT = 844

# Minimum distance between flowers to avoid overlap
MIN_DIST = 100

def draw_petal(t, size, color):
    """
    Draws a single petal with a given turtle, size, and color.
    The shape is formed by two arcs, and the petal is filled with the given color.
    """
    t.color(color)        # Set pen and fill color
    t.begin_fill()        # Start fill
    t.circle(size, 60)    # Draw first arc
    t.left(120)           # Turn to draw second arc
    t.circle(size, 60)    # Draw second arc
    t.end_fill()          # Complete the fill

def draw_flower(t, base_size, color):
    """
    Draws a 6-petal flower using the given turtle, petal size, and base color.
    Each petal is slightly randomized in size for organic variation.
    """
    for _ in range(6):
        petal_size = random.randint(base_size - 5, base_size + 5)
        draw_petal(t, petal_size, color)
        t.left(60)  # Rotate to position next petal

def move_to_safe_position(t):
    """
    Moves turtle to a random position on the screen, avoiding overlap with previous flowers.
    """
    attempts = 0
    while attempts < 50:  # Limit search attempts to avoid infinite loops
        x = random.randint(-SCREEN_WIDTH//2 + 50, SCREEN_WIDTH//2 - 50)
        y = random.randint(-SCREEN_HEIGHT//2 + 50, SCREEN_HEIGHT//2 - 50)
        
        # Ensure position is far enough from existing flower positions
        if all(((x - px) ** 2 + (y - py) ** 2) ** 0.5 >= MIN_DIST for px, py in used_positions):
            used_positions.append((x, y))
            t.penup()
            t.goto(x, y)
            t.pendown()
            return
        attempts += 1

def get_gradient_color(index, total):
    """
    Returns a smooth purple-to-pink gradient color based on the flower's index.
    Uses HSV color space for interpolation.
    """
    # Hue range from purple (~0.83) to pink (~0.95)
    hue = 0.83 + (0.12 * index / max(total - 1, 1))  # avoid divide-by-zero
    r, g, b = colorsys.hsv_to_rgb(hue, 0.6, 0.9)  # Saturation and brightness fixed
    return (r, g, b)

def create_flower_screensaver(num_flowers=10):
    """
    Sets up the screen and draws multiple non-overlapping gradient-colored flowers.
    """
    # Set up the turtle screen
    screen = turtle.Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("white")
    screen.colormode(1.0)  # Allow float RGB values for gradient

    artist = turtle.Turtle()
    artist.speed(0)       # Fastest drawing
    artist.width(2)

    for i in range(num_flowers):
        move_to_safe_position(artist)         # Go to a new, unused location
        color = get_gradient_color(i, num_flowers)  # Calculate gradient color
        draw_flower(artist, base_size=30, color=color)

    artist.hideturtle()
    screen.mainloop()  # Keep window open

# Run the updated flower screensaver
create_flower_screensaver()
