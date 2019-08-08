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
		self.playing = False
		
		self.all_sprites = pygame.sprite.Group()
		self.mobs = pygame.sprite.Group() # 新增

		self.player = Player()
		self.all_sprites.add(self.player)
		# ----------------新增---------------------
		for i in range(8):
			m = Mob()
			self.all_sprites.add(m)
			self.mobs.add(m)
		# -----------------------------------------
			
	def new(self):
		self.playing = True
		
	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.quitgame()
	
	def update(self):
		self.all_sprites.update()
		
		# --------------------新增----------------
		if len(self.mobs) < 8:
			m = Mob()
			self.all_sprites.add(m)
			self.mobs.add(m)
		# -----------------------------------------
		
	def draw(self):
		self.gameDisplay.fill(BLACK)
		self.all_sprites.draw(self.gameDisplay)
		pygame.display.update()
	
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
while game.running:
	game.new()
	game.run()
	game.gameover()