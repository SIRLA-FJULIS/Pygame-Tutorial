import pygame
from random import randint
pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('DVD')

dvd = pygame.image.load('1024px-DVD_VIDEO_logo.png') #132*60

def RAN():
    a = randint(0, 225)
    b = randint(0, 225)
    c = randint(0, 225)
    return (a,b,c)

color = RAN()
BLACK = (0, 0, 0)

DVD_x = 400
DVD_y = 0
direction_x = 1
direction_y = 1

clock = pygame.time.Clock()

playing = True
while playing:
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				playing = False
	DVD_x += 3*direction_x
	DVD_y += 3*direction_y
	if DVD_y <= 0:
		direction_y = 1
		color = RAN()
	elif DVD_x + 150 >= 800:
		direction_x = -1
		color = RAN()
	elif DVD_y + 68 >= 600:
		direction_y = -1
		color = RAN()
	elif DVD_x  <= 0 :
		direction_x = 1
		color = RAN()

	gameDisplay.fill(BLACK)
	
	pygame.draw.ellipse(gameDisplay,color,(DVD_x,DVD_y, 150,68))
	dvd.fill((color), None, pygame.BLEND_RGB_MULT)
	gameDisplay.blit(dvd, (DVD_x+9,DVD_y+4))
	
	pygame.display.update()
	clock.tick(30)
	
pygame.quit()
quit()

