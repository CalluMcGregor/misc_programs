import pygame
import sys
import random

class MyBall:
    def __init__(self, radius, colour, position, speed) -> None:
        self.radius = radius
        self.colour = colour
        self.position = position
        self.speed = speed

# Initialize Pygame
pygame.init()

# Set up display
width, height = 500, 500
centre = [width // 2, height // 3]
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball")

# Set up colours
black = (0, 0, 0)
white = (255, 255, 255)

first_ball = MyBall(20, (255, 0, 0), centre, [5, 5])
second_ball = MyBall(10, (255, 0, 0), [10, 10], [-5, -5])

my_balls = [first_ball]

ball_object = pygame.draw.circle(surface=screen, color=first_ball.colour, center=centre, radius=first_ball.radius)

# Set up clock to control frame rate
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(white)
    first_ball.speed[1] += 0.5

    ball_object = ball_object.move(first_ball.speed)

    if ball_object.left <= 0 or ball_object.right >= width:
        first_ball.speed[0] = -first_ball.speed[0]
    if ball_object.top <= 0 or ball_object.bottom >= height:
        first_ball.speed[1] = -first_ball.speed[1]

    pygame.draw.circle(surface=screen, color=first_ball.colour, center=(int(first_ball.position[0]), int(first_ball.position[1])), radius=first_ball.radius)
        
    pygame.display.flip()

    clock.tick(60)





    #     ball.speed[1] += 0.5
    #     ball.position[0] += ball.speed[0]
    #     ball.position [1] += ball.speed[1]

    # if ball.position[0] < ball.radius or ball.position[0] > width - ball.radius:
    #     ball.speed[0] = -ball.speed[0]
    #     ball.colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    # if ball.position[1] < ball.radius or ball.position[1] > width - ball.radius:
    #     ball.speed[1] = -ball.speed[1]
    #     ball.colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    #     # Ensure the ball doesn't get stuck at the bottom
    #     ball.position[1] = height - ball.radius

    # # Fill the screen with a black background
    # screen.fill(white)

    # # Draw the ball
    # for ball in my_balls:
    #     pygame.draw.circle(screen, ball.colour, (int(ball.position[0]), int(ball.position[1])), ball.radius)

    # # Update the display
    # pygame.display.flip()

    # # Cap the frame rate
    # clock.tick(60)
