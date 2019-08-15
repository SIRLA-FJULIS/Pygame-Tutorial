import pygame

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Ball Drop")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

ball_x = 400
ball_y = 0

clock = pygame.time.Clock()

playing = True
while playing:
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				playing = False
	ball_y += 5
	gameDisplay.fill(WHITE)
	pygame.draw.circle(gameDisplay, GREEN, (ball_x, ball_y), 25)
	pygame.display.update()
	clock.tick(30)

pygame.quit()
quit()