import pygame
import random

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("Ball Rebound")

WHITE = (255,255,255)
color = []
RGBLIST = ()
def randomcolor(color,RGBLIST):
    for i in range(0,256):
        color.append(i)
    color = random.sample(color, 3)
    RGBLIST = tuple(color)
    return RGBLIST
RGBLIST = randomcolor(color,RGBLIST)

#左邊
ball_x = 0
#上方
ball_y = 0
direction_x = 1
direction_y = 1

def show_text(ball_x, ball_y):
    ffoonntt = pygame.font.get_fonts()
    font = pygame.font.SysFont(ffoonntt[1], 24)
    text = font.render("DVD", True, (255, 255, 255))
    gameDisplay.blit(text, (ball_x + 50, ball_y + 20))

clock = pygame.time.Clock()

playing = True
while playing:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
    ball_y += 10 * direction_y
    ball_x += 10 * direction_x
    if ball_y <= 0:
        direction_y = 1
        RGBLIST = randomcolor(color,RGBLIST)
    elif ball_y + 80 >= 600:
        direction_y = -1
        RGBLIST = randomcolor(color,RGBLIST)
    if ball_x <= 0:
        direction_x = 1
        RGBLIST = randomcolor(color,RGBLIST)
    elif ball_x + 160 >= 800:
        direction_x = -1
        RGBLIST = randomcolor(color,RGBLIST)
    gameDisplay.fill(WHITE)
    #左邊,上方,寬度,高度
    pygame.draw.ellipse(gameDisplay, RGBLIST, (ball_x, ball_y, 160, 80))
    show_text(ball_x, ball_y)
    pygame.display.update()
    clock.tick(30)

pygame.quit()
quit()