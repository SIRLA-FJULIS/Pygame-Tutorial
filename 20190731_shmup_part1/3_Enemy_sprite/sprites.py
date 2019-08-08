import pygame
from settings import *
import random

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((50, 40))
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		self.rect.centerx = DISPLAY_WIDTH / 2
		self.rect.bottom = DISPLAY_HEIGHT - 10
		self.speedx = 0
	
	def update(self):
		self.speedx = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speedx = -8
		if keystate[pygame.K_RIGHT]:
			self.speedx = 8
		self.rect.x += self.speedx
		if self.rect.right > DISPLAY_WIDTH:
			self.rect.right = DISPLAY_WIDTH
		if self.rect.left < 0:
			self.rect.left = 0

# ----------------------------新增-----------------------------
class Mob(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((30, 40))
		self.image.fill(RED)
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(DISPLAY_WIDTH - self.rect.width)
		self.rect.y = random.randrange(-100, -40)
		self.speed_y = random.randrange(1, 8)
		self.speed_x = random.randrange(-3, 3)
		
	def update(self):
		self.rect.x += self.speed_x
		self.rect.y += self.speed_y
		if self.rect.top > DISPLAY_HEIGHT or self.rect.right < 0 or self.rect.left > DISPLAY_WIDTH:
			self.kill()
# --------------------------------------------------------------