import pygame
from random import randint # 引入randint

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Random Spawn Stone per Second')

WHITE = (255, 255, 255)

clock = pygame.time.Clock()
playing = True

rabbitImg = pygame.image.load('rabbit.jpg') # 記得自己去找一張圖片
stoneImg = pygame.image.load('stone.png')

x = (DISPLAY_WIDTH * 0.45)
y = (DISPLAY_HEIGHT * 0.75)
direction_x = 0
speed_x = 5

# ---------------新增與修改----------------
stone_num = 0
stone_x = []
stone_y = []
stone_y_speed = []
last_spawn_stone = pygame.time.get_ticks()
# ------------------------------------------

def draw_rabbit(x, y):
	gameDisplay.blit(rabbitImg, (x, y))

def draw_stone(x, y):
	gameDisplay.blit(stoneImg, (x, y))
	
while playing:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			playing = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				direction_x = -1
			elif event.key == pygame.K_RIGHT:
				direction_x = 1
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				direction_x = 0
				
	# ------------------新增----------------------
	now = pygame.time.get_ticks()
	if now - last_spawn_stone >= 1000:
		stone_x.append(randint(0, 750))
		stone_y.append(-50)
		stone_y_speed.append(randint(3, 7))
		stone_num += 1
		last_spawn_stone = now
	# ----------------------------------------------
	
	x += direction_x * speed_x
	if x <= 0:
		x = 0
	elif x + 100 >= 800:
		x = 700
	
	# --------------新增-------------------
	i = 0
	while i < stone_num:
		stone_y[i] += stone_y_speed[i]
		if stone_y[i] >= 600:
			stone_y.pop(i)
			stone_x.pop(i)
			stone_y_speed.pop(i)
			stone_num -= 1
		else:
			i += 1
	# -------------------------------------
	
	gameDisplay.fill(WHITE)
	draw_rabbit(x, y)
	# --------------新增-------------------
	for i in range(stone_num):
		draw_stone(stone_x[i], stone_y[i])
	# -------------------------------------
   
	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()