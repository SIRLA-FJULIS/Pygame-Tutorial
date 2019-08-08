import pygame
from random import randint

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("DVD Screensaver")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

ellipse_x = 300
ellipse_y = 100
dir_x = 1
dir_y = 1
color = (255, 0, 0)

clock = pygame.time.Clock()

playing = True
while playing:
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				playing = False
	ellipse_x += 5 * dir_x
	ellipse_y += 5 * dir_y
	if ellipse_x <= 0:
		dir_x = 1
		color = (randint(0, 255), randint(0, 255), randint(0, 255))
	elif ellipse_x + 200 >= 800:
		dir_x = -1
		color = (randint(0, 255), randint(0, 255), randint(0, 255))
	if ellipse_y <= 0:
		dir_y = 1
		color = (randint(0, 255), randint(0, 255), randint(0, 255))
	elif ellipse_y + 100 >= 600:
		dir_y = -1
		color = (randint(0, 255), randint(0, 255), randint(0, 255))
	gameDisplay.fill(WHITE)
	pygame.draw.ellipse(gameDisplay, color, pygame.Rect(ellipse_x, ellipse_y, 200, 100))
	pygame.display.update()
	clock.tick(30)

pygame.quit()
quit()