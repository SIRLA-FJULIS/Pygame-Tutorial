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
		self.shoot_delay = 300
		self.shield = 100
		self.lives = 3
		self.hidden = False
		self.hide_timer = pygame.time.get_ticks()
		self.power = 1
		self.power_time = pygame.time.get_ticks()

	def update(self):
		if self.power >= 2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
			self.power -= 1
			self.power_time = pygame.time.get_ticks()

		if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
			self.hidden = False
			self.rect.centerx = DISPLAY_WIDTH / 2
			self.rect.bottom = DISPLAY_HEIGHT - 10

		self.speedx = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speedx = -8
		if keystate[pygame.K_RIGHT]:
			self.speedx = 8
		now = pygame.time.get_ticks()
		if keystate[pygame.K_SPACE] and now - self.last_shoot_time > self.shoot_delay:
			self.last_shoot_time = now
			self.shoot()

		self.rect.x += self.speedx
		if self.rect.right > DISPLAY_WIDTH:
			self.rect.right = DISPLAY_WIDTH
		if self.rect.left < 0:
			self.rect.left = 0
	
	def powerup(self):
		self.power += 1
		self.power_time = pygame.time.get_ticks()
	
	def shoot(self):
		if self.power == 1:				
			bullet = Bullet(self.game, self.rect.centerx, self.rect.top)
			self.game.all_sprites.add(bullet)
			self.game.bullets.add(bullet)
			self.game.shoot_sound.play()
		if self.power >= 2:
			bullet1 = Bullet(self.game, self.rect.left, self.rect.centery)
			bullet2 = Bullet(self.game, self.rect.right, self.rect.centery)
			self.game.all_sprites.add(bullet1)
			self.game.all_sprites.add(bullet2)
			self.game.bullets.add(bullet1)
			self.game.bullets.add(bullet2)
			self.game.shoot_sound.play()

	def hide(self):
		self.hidden = True
		self.hide_timer = pygame.time.get_ticks()
		self.rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT + 200)

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

class Pow(pygame.sprite.Sprite):
	def __init__(self, game, center):
		pygame.sprite.Sprite.__init__(self)
		self.game = game
		self.type = random.choice(['shield', 'gun'])
		self.image = self.game.powerup_images[self.type]
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.speedy = 2

	def update(self):
		self.rect.y += self.speedy
		if self.rect.top > DISPLAY_HEIGHT:
			self.kill()