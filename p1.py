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

# Square settings
square_x = screen_width // 2
square_y = screen_height // 2
square_size = 100
square_speed_x = 0.5
square_speed_y = 0.5
last_time = time.time()

# Game loop
running = True
while running:
    # Handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
    # Points
    points = 0        

    # Time
    current_time = time.time()
    
    # Update square position
    square_x += square_speed_x
    square_y += square_speed_y
    
    # Change square color by Screen Edge Collision
    if square_x - square_size < 0 or square_x + square_size > screen_width:
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        square_speed_x = -square_speed_x  # Reverse direction

    if square_y - square_size < 0 or square_y + square_size > screen_height:
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        square_speed_y = -square_speed_y  # Reverse direction
        
    # Check if square is close to the corner of the screen
    if (square_x - square_size <= 20 and square_y - square_size <= 20) or \
    (square_x + square_size >= screen_width - 20 and square_y - square_size <= 20) or \
    (square_x - square_size <= 20 and square_y + square_size >= screen_height - 20) or \
    (square_x + square_size >= screen_width - 20 and square_y + square_size >= screen_height - 20):
        points += 1
        print("Corner Hit!")

    # Mouse Annoyances
    # Changes the color of the square when the mouse is clicked over it
    if pg.mouse.get_pressed()[0]:
        if current_time - last_time > 0.2:
            last_time = current_time
            mouse_x, mouse_y = pg.mouse.get_pos()
            distance = ((square_x - mouse_x) ** 2 + (square_y - mouse_y) ** 2) ** 0.5
            if distance < square_size:
                red = random.randint(0, 255)
                green = random.randint(0, 255)
                blue = random.randint(0, 255)
    
    # Changes the direction of the square when the mouse is clicked over it
    if pg.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pg.mouse.get_pos()
        if (square_x - square_size < mouse_x < square_x + square_size and
            square_y - square_size < mouse_y < square_y + square_size):
            square_speed_x = -square_speed_x
            square_speed_y = -square_speed_y

    # Fill the screen with gray color
    screen.fill(gray)

    # Draw the square
    pg.draw.rect(screen, (red, green, blue), (square_x - square_size, square_y - square_size, square_size * 2, square_size * 2))
    
    # Print the points in terminal
    print("Points: ", points)
    
    # Update the display
    pg.display.flip()

# Quit the game
pg.quit()
sys.exit()
