import pygame as pg
import sys
import random
import time

# Initialize Pygame
pg.init()

# Screen settings
screen_width = 1280     
screen_height = 800
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
last_time = time.time()
points = 0

# Game loop
running = True
while running:
    # Handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Time
    current_time = time.time()
    
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
        
    if circle_x - circle_radius < 0 and circle_y - circle_radius < 0:
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        circle_speed_x = -circle_speed_x
        circle_speed_y = -circle_speed_y
        points += 1

    #Mouse Annoyances
    #Changes the color of the circle when the mouse is clicked over it
    if pg.mouse.get_pressed()[0]:
        if current_time - last_time > 0.2:
            last_time = current_time
            mouse_x, mouse_y = pg.mouse.get_pos()
            distance = ((circle_x - mouse_x) ** 2 + (circle_y - mouse_y) ** 2) ** 0.5
            if distance < circle_radius:
                red = random.randint(0, 255)
                green = random.randint(0, 255)
                blue = random.randint(0, 255)
    
    # Changes the direction of the square when the mouse is clicked over it
    if pg.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pg.mouse.get_pos()
        if (circle_x - circle_radius < mouse_x < circle_x + circle_radius and
            circle_y - circle_radius < mouse_y < circle_y + circle_radius):
            circle_speed_x = -circle_speed_x
            circle_speed_y = -circle_speed_y

    # Fill the screen with gray color
    screen.fill(gray)

    # Draw the circle
    pg.draw.rect(screen, (red, green, blue), (circle_x - circle_radius, circle_y - circle_radius, circle_radius * 2, circle_radius * 2))
    
    # Print the points in terminal
    print("Points: ", points)
    
    # Update the display
    pg.display.flip()

# Quit the game
pg.quit()
sys.exit()