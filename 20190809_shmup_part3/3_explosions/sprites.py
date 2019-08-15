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
		self.shield = 100

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
		self.game.shoot_sound.play()

class Mob(pygame.sprite.Sprite):
	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game 
		self.image_orig = random.choice(self.game.mob_images)
		self.image = self.image_orig.copy()
		self.rect = self.image.get_rect()
		self.radius = int(self.rect.width * .85 / 2)
		self.rect.x = random.randrange(DISPLAY_WIDTH - self.rect.width)
		self.rect.y = random.randrange(-100, -40)
		self.speed_y = random.randrange(1, 8)
		self.speed_x = random.randrange(-3, 3)
		self.rot = 0
		self.rot_speed = random.randrange(-8, 8)
		self.last_update = pygame.time.get_ticks()
	
	def rotate(self):
		now = pygame.time.get_ticks()
		if now - self.last_update > 50:
			self.last_update = now
			self.rot = (self.rot + self.rot_speed) % 360
			new_image = pygame.transform.rotate(self.image_orig, self.rot)
			old_center = self.rect.center
			self.image = new_image
			self.rect = self.image.get_rect()
			self.rect.center = old_center

	def update(self):
		self.rotate()
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

# --------------------------------新增------------------------------
class Explosion(pygame.sprite.Sprite):
	def __init__(self, game, center, size):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		self.size = size
		self.image = self.game.explosion_anim[self.size][0]
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.frame = 0
		self.last_update = pygame.time.get_ticks()
		self.frame_rate = 50

	def update(self):
		now = pygame.time.get_ticks()
		if now - self.last_update > self.frame_rate:
			self.last_update = now
			self.frame += 1
			if self.frame == len(self.game.explosion_anim[self.size]):
				self.kill()
			else:
				center = self.rect.center
				self.image = self.game.explosion_anim[self.size][self.frame]
				self.rect = self.image.get_rect()
				self.rect.center = center
# -------------------------------------------------------------------