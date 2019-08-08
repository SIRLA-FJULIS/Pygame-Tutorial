import pygame, sys
import random

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Ball Rebound")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

ball_x = 400
ball_y = 0
direction_x = -1
direction_y = 1
r = 0
g = 50
b = 100

clock = pygame.time.Clock()

playing = True
while playing:
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				playing = False
	ball_x += direction_x
	ball_y += direction_y

	font = pygame.font.SysFont("arial", 24)
	text = font.render("Hello!!!", True, (255, 255, 255))


	if ball_y <= 0:
		direction_y = 1
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
	elif ball_y + 50 >= 600:
		direction_y = -1
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)

	if ball_x <= 0:
		direction_x = 1
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)

	elif ball_x + 80 >= 800:
		direction_x = -1
		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)


	gameDisplay.fill(WHITE)
	pygame.draw.ellipse(gameDisplay, (r, g, b), (ball_x, ball_y, 80, 50))
	gameDisplay.blit(text, (ball_x + 10,ball_y + 10))
	pygame.display.update()
	clock.tick(30)

pygame.quit()
quit()