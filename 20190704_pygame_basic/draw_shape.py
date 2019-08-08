import pygame

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Draw Shapes")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()

playing = True
while playing:
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				playing = False
				
	gameDisplay.fill(WHITE)
	pygame.draw.rect(gameDisplay, RED, pygame.Rect(100, 100, 40, 40))
	pygame.draw.circle(gameDisplay, GREEN, (200, 100), 25)
	pygame.draw.line(gameDisplay, BLUE, (300, 100), (300, 400))
	pygame.draw.line(gameDisplay, BLUE, (350, 100), (350, 400), 5)
	pygame.display.update()
	clock.tick(30)

pygame.quit()
quit()