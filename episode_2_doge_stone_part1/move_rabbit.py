import pygame

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Move Rabbit')

WHITE = (255, 255, 255)

clock = pygame.time.Clock()
playing = True
rabbitImg = pygame.image.load('rabbit.jpg') # 記得自己去找一張圖片

x = (DISPLAY_WIDTH * 0.45)
y = (DISPLAY_HEIGHT * 0.75)
# --新增變數--
direction_x = 0
speed_x = 5
# ------------

def draw_rabbit(x, y):
	gameDisplay.blit(rabbitImg, (x, y))

while playing:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			playing = False
		# -----------新增這段-----------
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				direction_x = -1
			elif event.key == pygame.K_RIGHT:
				direction_x = 1
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				direction_x = 0
		# -----------------------------
	# --還有這段--
	x += direction_x * speed_x
	if x <= 0:
		x = 0
	elif x + 100 >= 800:
		x = 700
	# ------------
			
	gameDisplay.fill(WHITE)
	draw_rabbit(x, y)
   
	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()