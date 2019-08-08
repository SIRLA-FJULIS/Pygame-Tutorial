import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Show Rabbit')

WHITE = (255, 255, 255)

clock = pygame.time.Clock()
playing = True
rabbitImg = pygame.image.load('rabbit.jpg') # 記得自己去找一張圖片

x = (display_width * 0.45)
y = (display_height * 0.75)
direction_x = 0
speed_x = 5

def draw_rabbit(x, y):
    gameDisplay.blit(rabbitImg, (x, y))

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
			
    gameDisplay.fill(WHITE)
    draw_rabbit(x, y)
   
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()