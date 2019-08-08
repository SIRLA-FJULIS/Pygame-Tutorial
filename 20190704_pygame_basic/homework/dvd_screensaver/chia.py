import pygame, random

def random_color():
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)
	color = tuple([r, g, b])
	return color

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Ball Rebound - DVD")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
default_color = (239, 245, 66)

ball_x = 400
ball_y = 0
direction_y = 1 #控制上下
direction_x = 1 #控制左右

clock = pygame.time.Clock()

bump = 0 #沒撞牆
playing = True
while playing:	
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				playing = False
	
	ball_y += 5 * direction_y
	ball_x += 5 * direction_x

	if ball_y <= 0:
		bump = 1
		ellipse_color = random_color()
		direction_y = 1
	elif ball_y + 60 >= 600: #若加上橢圓的高 >= DISPLAY_HEIGHT (超過下界)，則反彈。
		bump = 1
		ellipse_color = random_color()
		direction_y = -1

	if ball_x <= 0:
		bump = 1
		ellipse_color = random_color()
		direction_x = 1
	elif ball_x + 100 >= 800: #若加上橢圓的寬 >= DISPLAY_WIDTH (超過右界)，則反彈。
		bump = 1
		ellipse_color = random_color()
		direction_x = -1

	if bump == 0:
		ellipse_color = default_color
	else:
		ellipse_color = ellipse_color

	gameDisplay.fill(WHITE)
	pygame.draw.ellipse(gameDisplay, ellipse_color, pygame.Rect(ball_x, ball_y, 100, 60))
	pygame.display.update()
	clock.tick(30)
	print(ellipse_color)

pygame.quit()
quit()