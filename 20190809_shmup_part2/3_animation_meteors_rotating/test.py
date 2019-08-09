import pygame
from os import path

pygame.init()
gameDisplay = pygame.display.set_mode((250, 250))
clock = pygame.time.Clock()
pygame.display.set_caption('TEST')

img_dir = path.join(path.dirname(__file__), 'img')
mob_img_orig = pygame.image.load(path.join(img_dir, 'meteorBrown_med1.png')).convert()

mob_img = mob_img_orig.copy()
mob_img_rect = mob_img.get_rect()
mob_img_rect.center = (100, 100)
rot = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    gameDisplay.fill((255, 255, 255))
    rot += 10
    mob_img = pygame.transform.rotate(mob_img_orig, rot)
    mob_img_rect = mob_img.get_rect()
    gameDisplay.blit(mob_img, mob_img_rect)
    pygame.display.update()
    clock.tick(10)