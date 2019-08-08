import pygame
from random import randint

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
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

class Rabbit:
    def __init__(self):
        self.x = (DISPLAY_WIDTH * 0.45)
        self.y = (DISPLAY_HEIGHT * 0.75)
        self.rabbitImg = pygame.image.load('fox.jpg')
        self.direction_x = 0
        self.speed_x = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            rabbit.direction_x = -1
        elif keys[pygame.K_RIGHT]:
            rabbit.direction_x = 1
        else:
            rabbit.direction_x = 0
        rabbit.x += (rabbit.direction_x * rabbit.speed_x)
        if rabbit.x <= 0:
            rabbit.x = 0
        elif rabbit.x + 100 >= 800:
            rabbit.x = 700

    def draw(self):
        gameDisplay.blit(self.rabbitImg, (self.x, self.y))

rabbit = Rabbit()

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    now = pygame.time.get_ticks()
    if now - last_spawn_stone >= 1000:
        stones.append(Stone())
        last_spawn_stone = now

    for stone in stones:
        stone.update()
        if stone.pos_y >= 600:
            stones.remove(stone)
		
    gameDisplay.fill(WHITE)
    rabbit.update()
    rabbit.draw()

    for stone in stones:
        stone.draw()
   
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()