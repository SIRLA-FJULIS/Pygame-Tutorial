import pygame
from random import randint # 引入randint

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Stone Class')

WHITE = (255, 255, 255)

clock = pygame.time.Clock()
playing = True

last_spawn_stone = pygame.time.get_ticks()
stones = []

class Rabbit:
	def __init__(self):
		self.pos_x = (DISPLAY_WIDTH * 0.45)
		self.pos_y = (DISPLAY_HEIGHT * 0.75)
		self.direction_x = 0
		self.speed_x = 5
		self.rabbitImg = pygame.image.load('rabbit.jpg') # 記得自己去找一張圖片
	
	def update(self):
		for event in input:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					self.direction_x = -1
				if event.key == pygame.K_RIGHT:
					self.direction_x = 1
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					self.direction_x = 0
			
		self.pos_x += self.direction_x * self.speed_x
		if self.pos_x <= 0:
			self.pos_x = 0
		elif self.pos_x + 100 >= 800:
			self.pos_x = 700
			
	def draw(self):
		gameDisplay.blit(self.rabbitImg, (self.pos_x, self.pos_y))

class Stone:
	def __init__(self):
		self.pos_x = randint(0, 750)
		self.pos_y = -50
		self.speed_y = randint(3, 7)
		self.stoneImg = pygame.image.load('stone.png')
	
	def update(self):
		self.pos_y += self.speed_y
	
	def draw(self):
		gameDisplay.blit(self.stoneImg, (self.pos_x, self.pos_y))

rabbit = Rabbit()
		
while playing:
	input = pygame.event.get()
	for event in input:
		if event.type == pygame.QUIT:
			playing = False
	
	now = pygame.time.get_ticks()
	if now - last_spawn_stone >= 1000:
		stones.append(Stone())
		last_spawn_stone = now

	rabbit.update()
	for stone in stones:
		stone.update()
		if stone.pos_y >= 600:
			stones.remove(stone)
		
	gameDisplay.fill(WHITE)
	rabbit.draw()
	for stone in stones:
		stone.draw()
   
	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()