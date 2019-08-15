import pygame
from settings import *
import random

class Player(pygame.sprite.Sprite):
	# 修改，game加入建構子參數
	def __init__(self, game):
		pygame.sprite.Sprite.__init__(self)
		self.game = game # 新增
		self.image = pygame.Surface((50, 40))
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		self.rect.centerx = DISPLAY_WIDTH / 2
		self.rect.bottom = DISPLAY_HEIGHT - 10
		self.speedx = 0
		self.last_shoot_time = pygame.time.get_ticks() # 新增
	
	def update(self):
		self.speedx = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speedx = -8
		if keystate[pygame.K_RIGHT]:
			self.speedx = 8
		# ------------------------------新增-----------------------------------
		now = pygame.time.get_ticks()
		if keystate[pygame.K_SPACE] and now - self.last_shoot_time > 300:
			self.last_shoot_time = now
			self.shoot()
		# ---------------------------------------------------------------------

		self.rect.x += self.speedx
		if self.rect.right > DISPLAY_WIDTH:
			self.rect.right = DISPLAY_WIDTH
		if self.rect.left < 0:
			self.rect.left = 0
	
	# ----------------------------新增---------------------------
	def shoot(self):
		bullet = Bullet(self.rect.centerx, self.rect.top)
		self.game.all_sprites.add(bullet)
		self.game.bullets.add(bullet)
	# -----------------------------------------------------------

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

# ----------------------新增-----------------------
class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((10, 20))
		self.image.fill(YELLOW)
		self.rect = self.image.get_rect()
		self.rect.bottom = y
		self.rect.centerx = x
		self.speed_y = -10
	
	def update(self):
		self.rect.y += self.speed_y
		if self.rect.bottom < 0:
			self.kill()
# -------------------------------------------------