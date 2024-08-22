import pygame as pg
import sys
import random

# Initialize Pygame
pg.init()

# Screen settings
screen_width = 800
screen_height = 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Test Program")

# Colors
gray = (200, 200, 200)
red = 255
green = 0
blue = 0

# Circle settings
circle_x = screen_width // 2
circle_y = screen_height // 2
circle_radius = 100
circle_speed_x = 0.5
circle_speed_y = 0.5

# Game loop
running = True
while running:
    # Handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Update circle position
    circle_x += circle_speed_x
    circle_y += circle_speed_y
    
    # Change circle color by Screen Edge Collision
    if circle_x - circle_radius < 0 or circle_x + circle_radius > screen_width:
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        circle_speed_x = -circle_speed_x  # Reverse direction

    if circle_y - circle_radius < 0 or circle_y + circle_radius > screen_height:
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        circle_speed_y = -circle_speed_y  # Reverse direction

    # Fill the screen with gray color
    screen.fill(gray)

    # Draw the circle
    pg.draw.circle(screen, (red, green, blue), (circle_x, circle_y), circle_radius)

    # Update the display
    pg.display.flip()

# Quit the game
pg.quit()
sys.exit()