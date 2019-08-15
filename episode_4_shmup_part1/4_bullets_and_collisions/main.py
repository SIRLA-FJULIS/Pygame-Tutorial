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
		self.mobs = pygame.sprite.Group()
		self.player = Player(self) # 修改
		self.all_sprites.add(self.player)
		for i in range(8):
			m = Mob()
			self.all_sprites.add(m)
			self.mobs.add(m)
		self.bullets = pygame.sprite.Group() # 新增
			
	def new(self):
		self.playing = True
		
	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.quitgame()
	
	def update(self):
		self.all_sprites.update()

		if len(self.mobs) < 8:
			m = Mob()
			self.all_sprites.add(m)
			self.mobs.add(m)

	# ---------------------------------------新增---------------------------------------
	def collision_check(self):
		bullet_hits = pygame.sprite.groupcollide(self.mobs, self.bullets, True, True)
		for hit in bullet_hits:
			m = Mob()
			self.all_sprites.add(m)
			self.mobs.add(m)
		
		mob_hits = pygame.sprite.spritecollide(self.player, self.mobs, False)
		if mob_hits:
			self.quitgame()
	# ----------------------------------------------------------------------------------

	def draw(self):
		self.gameDisplay.fill(BLACK)
		self.all_sprites.draw(self.gameDisplay)
		pygame.display.update()
	
	def run(self):
		while self.playing:
			self.events()
			self.update()
			self.collision_check() # 新增
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