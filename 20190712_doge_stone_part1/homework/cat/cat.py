import pygame
from random import randint

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Neko Run')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()
playing = True

# ------------------------------------------------------------------------------------
class NekoSensei:
    def __init__(self):
        self.position_x = DISPLAY_WIDTH * 0.45
        self.position_y = DISPLAY_HEIGHT * 0.75
        self.direction_x = 0
        self.speed_x = 5
        self.nekoImg = pygame.image.load('./_images/neko_sensei.jpg') # 100 * 86 pixel

    def move(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.direction_x = -1
            elif event.key == pygame.K_RIGHT:
                self.direction_x = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.direction_x = 0
    
    def update(self):
        self.position_x += self.direction_x * self.speed_x
        if self.position_x <= 0:
            self.position_x = 0
        elif self.position_x + 100 >= 800:
            self.position_x = 700

    def draw(self):
        gameDisplay.blit(self.nekoImg, (self.position_x, self.position_y))


class Stone:
    def __init__(self):
        self.position_x = randint(0, 750)
        self.position_y = -50
        self.speed_y = randint(3, 7)
        self.stoneImg = pygame.image.load('./_images/stone.jpg') # 50 * 50 pixel
    
    def update(self):
        self.position_y += self.speed_y

    def draw(self):
        gameDisplay.blit(self.stoneImg, (self.position_x, self.position_y))

neko = NekoSensei()
last_time_spawned_stone = pygame.time.get_ticks()
stones = []

# ------------------------------------------------------------------------------------

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        neko.move()
   
    now = pygame.time.get_ticks()
    time_rand = randint(500, 3000)
    if now - last_time_spawned_stone >= time_rand:
        stones.append(Stone())
        last_time_spawned_stone = now

    neko.update()
    
    for stone in stones:
        stone.update()
        if stone.position_y >= 600:
            stones.remove(stone)

    gameDisplay.fill(BLACK)
    neko.draw()
    for stone in stones:
        stone.draw()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()