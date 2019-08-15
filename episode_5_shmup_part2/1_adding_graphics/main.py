import pygame
from sprites import *
from settings import *
from os import path # 新增

class Game:
	def __init__(self):
		pygame.init()
		
		self.gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
		pygame.display.set_caption(TITLE)

		self.clock = pygame.time.Clock()
		self.running = True
		self.playing = False

		# -------------------新增----------------
		self.img_dir = path.join(path.dirname(__file__), 'img')
		self.load_data()
		# ---------------------------------------

		self.all_sprites = pygame.sprite.Group()
		self.mobs = pygame.sprite.Group()
		self.player = Player(self)
		self.all_sprites.add(self.player)
		for i in range(8):
			m = Mob(self) # 修改
			self.all_sprites.add(m)
			self.mobs.add(m)
		self.bullets = pygame.sprite.Group()
	
	# ---------------------------------------------------新增-----------------------------------------------
	def load_data(self):
		self.background = pygame.image.load(path.join(self.img_dir, 'starfield.png')).convert()
		self.background_rect = self.background.get_rect()
		self.player_img = pygame.image.load(path.join(self.img_dir, 'playerShip1_orange.png')).convert()
		self.player_img = pygame.transform.scale(self.player_img, (50, 38))
		self.player_img.set_colorkey(BLACK)
		self.mob_img = pygame.image.load(path.join(self.img_dir, 'meteorBrown_med1.png')).convert()
		self.mob_img.set_colorkey(BLACK)
		self.bullet_img = pygame.image.load(path.join(self.img_dir, 'laserRed16.png')).convert()
		self.bullet_img.set_colorkey(BLACK)
	# -------------------------------------------------------------------------------------------------------

	def new(self):
		self.playing = True
		
	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.quitgame()
	
	def update(self):
		self.all_sprites.update()

		if len(self.mobs) < 8:
			m = Mob(self) # 修改
			self.all_sprites.add(m)
			self.mobs.add(m)

	def collision_check(self):
		bullet_hits = pygame.sprite.groupcollide(self.mobs, self.bullets, True, True)
		for hit in bullet_hits:
			m = Mob(self) # 修改
			self.all_sprites.add(m)
			self.mobs.add(m)
		
		mob_hits = pygame.sprite.spritecollide(self.player, self.mobs, False)
		if mob_hits:
			self.quitgame()

	def draw(self):
		# self.gameDisplay.fill(BLACK) 刪除
		self.gameDisplay.blit(self.background, self.background_rect) # 新增
		self.all_sprites.draw(self.gameDisplay)
		pygame.display.update()
	
	def run(self):
		while self.playing:
			self.events()
			self.update()
			self.collision_check()
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