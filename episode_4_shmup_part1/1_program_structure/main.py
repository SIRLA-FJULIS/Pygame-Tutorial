import pygame
from sprites import *
from settings import *

class Game:
	def __init__(self):
		pygame.init()
		
		self.gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
		pygame.display.set_caption(TITLE)

		self.clock = pygame.time.Clock()
		self.running = True
		
	def new(self):
		self.playing = True
		
	def events(self):
		pass
	
	def update(self):
		pass
		
	def draw(self):
		pass
	
	def run(self):
		while self.playing:
			self.events()
			self.update()
			self.draw()
			self.clock.tick(FPS)
	
	def game_intro(self):
		pass
	
	def gameover(self):
		pass
		
	def quitgame(self):
		pygame.quit()
		quit()

game = Game()
game.game_intro()
while game.running:
	game.new()
	game.run()
	game.gameover()