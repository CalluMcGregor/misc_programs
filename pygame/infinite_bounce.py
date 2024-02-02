import pygame
import random

# Initialize Pygame 
pygame.init()

# Set up display
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Ball properties  
ball_x = 250
ball_y = 200
ball_radius = 15
ball_colour = (255, 0, 0)
ball_speed_y = 0
ball_speed_x = 2
gravity = 0.5

def colour_picker():
    return random.randint(0, 255)

# Clock for limiting frame rate  
clock = pygame.time.Clock()

# Run until quit
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # Apply gravity
    ball_speed_y += gravity
        
    # Move ball  
    ball_y += ball_speed_y
    ball_x += ball_speed_x

    # Bounce logic  
    if ball_y > screen_height - ball_radius:
        ball_speed_y = -ball_speed_y
        ball_y = screen_height - ball_radius
        ball_colour = tuple(colour_picker() for _ in range(3))

    if ball_y < ball_radius:
        ball_speed_y = -ball_speed_y
        ball_y = ball_radius
        ball_colour = tuple(colour_picker() for _ in range(3))

    if ball_x > screen_width - ball_radius:
        ball_speed_x =- ball_speed_x
        ball_colour = tuple(colour_picker() for _ in range(3))
    
    if ball_x < 0 + ball_radius:
        ball_speed_x = abs(ball_speed_x)
        ball_colour = tuple(colour_picker() for _ in range(3))

    # Draw and update        
    screen.fill('white') 
    pygame.draw.circle(screen, ball_colour, (ball_x, ball_y), ball_radius)
    pygame.display.update()
    
    # Limit to 60 fps 
    clock.tick(60) 