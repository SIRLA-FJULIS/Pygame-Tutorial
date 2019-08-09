import pygame
from settings import *
import random
from os import path

class Player(pygame.sprite.Sprite):
	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		self.image = self.game.player_img
		self.rect = self.image.get_rect()
		self.radius = 22
		self.rect.centerx = DISPLAY_WIDTH / 2
		self.rect.bottom = DISPLAY_HEIGHT - 10
		self.speedx = 0
		self.last_shoot_time = pygame.time.get_ticks()

	def update(self):
		self.speedx = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speedx = -8
		if keystate[pygame.K_RIGHT]:
			self.speedx = 8
		now = pygame.time.get_ticks()
		if keystate[pygame.K_SPACE] and now - self.last_shoot_time > 300:
			self.last_shoot_time = now
			self.shoot()

		self.rect.x += self.speedx
		if self.rect.right > DISPLAY_WIDTH:
			self.rect.right = DISPLAY_WIDTH
		if self.rect.left < 0:
			self.rect.left = 0
	
	def shoot(self):
		bullet = Bullet(self.game, self.rect.centerx, self.rect.top)
		self.game.all_sprites.add(bullet)
		self.game.bullets.add(bullet)

class Mob(pygame.sprite.Sprite):
	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game 
		self.image = self.game.mob_img
		self.rect = self.image.get_rect()
		self.radius = int(self.rect.width * .85 / 2)
		self.rect.x = random.randrange(DISPLAY_WIDTH - self.rect.width)
		self.rect.y = random.randrange(-100, -40)
		self.speed_y = random.randrange(1, 8)
		self.speed_x = random.randrange(-3, 3)
		
	def update(self):
		self.rect.x += self.speed_x
		self.rect.y += self.speed_y
		if self.rect.top > DISPLAY_HEIGHT or self.rect.right < 0 or self.rect.left > DISPLAY_WIDTH:
			self.kill()

class Bullet(pygame.sprite.Sprite):
	def __init__(self, game, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		self.image = self.game.bullet_img
		self.rect = self.image.get_rect()
		self.rect.bottom = y
		self.rect.centerx = x
		self.speed_y = -10
	
	def update(self):
		self.rect.y += self.speed_y
		if self.rect.bottom < 0:
			self.kill()