import pygame
from random import randint 

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Stone Class')
pygame.display.set_caption('Rabbit Class')

WHITE = (255, 255, 255)

clock = pygame.time.Clock()
playing = True



last_spawn_stone = pygame.time.get_ticks()
stones = [] 




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

#----------rabbit-----------
class Rabbit:
    def __init__(self):
        self.x = (DISPLAY_WIDTH * 0.45)
        self.y = (DISPLAY_HEIGHT * 0.75)
        self.speed_x = 5
        self.direction_x = 0
        self.rabbitImg = pygame.image.load('rabbit.jpg')

    def move(self):
 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.direction_x = -1
            elif event.key == pygame.K_RIGHT:
                self.direction_x = 1
                
    def move_stop(self):
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.direction_x = 0

    def update(self):
        self.x += self.direction_x * self.speed_x
        if self.x <= 0:
            self.x = 0
        elif self.x + 100 >= 800:
            self.x = 700
xrange
    def draw(self):
        gameDisplay.blit(self.rabbitImg, (self.x, self.y))

rabbit = Rabbit()
#---------------------------
while playing:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			playing = False
		rabbit.move()
		rabbit.move_stop()
		
	now = pygame.time.get_ticks()
	if now - last_spawn_stone >= 1000:
		stones.append(Stone())
		last_spawn_stone = now
#----------rabbit-----------
	rabbit.update()
#---------------------------
	for stone in stones:
		stone.update()
		if stone.pos_y >= 600:
			stones.remove(stone)

		
	gameDisplay.fill(WHITE)
#----------rabbit-----------
	rabbit.draw()
#---------------------------
	for stone in stones:
		stone.draw()

   
	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()
