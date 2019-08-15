import pygame
from random import randint # 引入randint
from settings import *
from sprites import Rabbit, Stone

class Game:
	def __init__(self):
		pygame.init()
		
		self.gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
		pygame.display.set_caption(TITLE)

		self.clock = pygame.time.Clock()
		self.playing = True

		self.last_spawn_stone = pygame.time.get_ticks()
		self.stones = []

		self.rabbit = Rabbit(self)
	
	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.playing = False
	
	def update(self):
		now = pygame.time.get_ticks()
		if now - self.last_spawn_stone >= 1000:
			self.stones.append(Stone(self))
			self.last_spawn_stone = now
			
		self.rabbit.update()
		
		for stone in self.stones:
			stone.update()
			if stone.pos_y >= 600:
				self.stones.remove(stone)
	
	def draw(self):
		self.gameDisplay.fill(WHITE)
		self.rabbit.draw()
		for stone in self.stones:
			stone.draw()
		pygame.display.update()
	
	def run(self):
		# Game Loop
		while self.playing:
			self.events()
			self.update()
			self.draw()
			self.clock.tick(FPS)

game = Game()
game.run()
pygame.quit()
quit()