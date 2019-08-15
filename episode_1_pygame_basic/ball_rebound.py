import pygame

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Ball Rebound")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

ball_x = 400
ball_y = 0
direction = 1

clock = pygame.time.Clock()

playing = True
while playing:
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				playing = False
	ball_y += 10 * direction
	if ball_y - 25 <= 0:
		direction = 1
	elif ball_y + 25 >= 600:
		direction = -1
	gameDisplay.fill(WHITE)
	pygame.draw.circle(gameDisplay, GREEN, (ball_x, ball_y), 25)
	pygame.display.update()
	clock.tick(30)

pygame.quit()
quit()