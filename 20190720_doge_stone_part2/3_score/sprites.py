import pygame
from random import randint
from settings import *

class Rabbit:
	def __init__(self, game):
		self.game = game
		self.pos_x = (DISPLAY_WIDTH * 0.45)
		self.pos_y = (DISPLAY_HEIGHT * 0.75)
		self.direction_x = 0
		self.speed_x = 5
		self.rabbitImg = pygame.image.load('rabbit.jpg') # 記得自己去找一張圖片
		self.rect = self.rabbitImg.get_rect()
		self.rect.topleft = (self.pos_x, self.pos_y)
	
	def update(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			self.direction_x = -1 
		elif keys[pygame.K_RIGHT]:
				self.direction_x = 1 
		else:
			self.direction_x = 0
			
		self.pos_x += self.direction_x * self.speed_x
		if self.pos_x <= 0:
			self.pos_x = 0
		elif self.pos_x + 100 >= 800:
			self.pos_x = 700
			
		self.rect.topleft = (self.pos_x, self.pos_y)
			
	def draw(self):
		self.game.gameDisplay.blit(self.rabbitImg, (self.pos_x, self.pos_y))

class Stone:
	def __init__(self, game):
		self.game = game
		self.pos_x = randint(0, 750)
		self.pos_y = -50
		self.speed_y = randint(3, 7)
		self.stoneImg = pygame.image.load('stone.png')
		self.rect = self.stoneImg.get_rect()
		self.rect.topleft = (self.pos_x, self.pos_y)
	
	def update(self):
		self.pos_y += self.speed_y
		self.rect.topleft = (self.pos_x, self.pos_y)
	
	def draw(self):
		self.game.gameDisplay.blit(self.stoneImg, (self.pos_x, self.pos_y))