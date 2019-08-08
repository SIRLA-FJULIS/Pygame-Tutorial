import pygame
import random

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("DVD Screen Protection")

WHITE = (255, 255, 255)
R = 0
G = 0
B = 0

ball_x = 400
ball_y = 0
direction_x = 1
direction_y = 1

clock = pygame.time.Clock()

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
    
    ball_y += 10 * direction_y
    ball_x += 10 * direction_x
    collision = 0

    if ball_y <= 0:
        direction_y = 1
        collision = 1
    elif ball_y + 75 >= 600:
        direction_y = -1
        collision = 1
    elif ball_x <= 0:
        direction_x = 1
        collision = 1
    elif ball_x + 150 >= 800:
        direction_x = -1
        collision = 1
    else:
        collision = 0
        
    
    if collision == 1:
        R = random.randint(0, 255)
        G = random.randint(0, 255)
        B = random.randint(0, 255)

    COLOR = (R, G, B)
    gameDisplay.fill(WHITE)     # fill the canvas with white to clean the screen
    pygame.draw.ellipse(gameDisplay, COLOR, pygame.Rect(ball_x, ball_y, 150, 75))
    pygame.display.update()
    clock.tick(30)      # fps

pygame.quit()
quit()