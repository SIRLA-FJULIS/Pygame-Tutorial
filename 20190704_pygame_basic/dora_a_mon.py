import pygame

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Dora A Mon")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHT_BLUE = (59, 183, 255)
PINK = (255, 133, 133)

clock = pygame.time.Clock()

playing = True
while playing:
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				playing = False
	gameDisplay.fill(WHITE)
	# head
	pygame.draw.circle(gameDisplay, LIGHT_BLUE, (400, 300), 250)
	pygame.draw.circle(gameDisplay, WHITE, (400, 340), 200)
	# left eye
	pygame.draw.circle(gameDisplay, WHITE, (350, 150), 50)
	pygame.draw.circle(gameDisplay, BLACK, (370, 150), 15)
	pygame.draw.circle(gameDisplay, WHITE, (370, 150), 5)
	# right eye
	pygame.draw.circle(gameDisplay, WHITE, (450, 150), 50)
	pygame.draw.circle(gameDisplay, BLACK, (430, 150), 15)
	pygame.draw.circle(gameDisplay, WHITE, (430, 150), 5)
	# nose
	pygame.draw.circle(gameDisplay, RED, (400, 250), 20)
	# left beard
	pygame.draw.line(gameDisplay, BLACK, (370, 300), (270, 270), 2)
	pygame.draw.line(gameDisplay, BLACK, (370, 330), (270, 330), 2)
	pygame.draw.line(gameDisplay, BLACK, (370, 360), (270, 390), 2)
	# right beard
	pygame.draw.line(gameDisplay, BLACK, (430, 300), (530, 270), 2)
	pygame.draw.line(gameDisplay, BLACK, (430, 330), (530, 330), 2)
	pygame.draw.line(gameDisplay, BLACK, (430, 360), (530, 390), 2)
	# mouse
	pygame.draw.ellipse(gameDisplay, RED, (300, 430, 200, 100))
	pygame.draw.ellipse(gameDisplay, PINK, (340, 460, 120, 70))
	pygame.display.update()
	clock.tick(30)

pygame.quit()
quit()