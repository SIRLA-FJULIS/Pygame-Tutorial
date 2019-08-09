import pygame
from sprites import *
from settings import *
from os import path

class Game:
	def __init__(self):
		pygame.init()
		
		self.gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
		pygame.display.set_caption(TITLE)

		self.clock = pygame.time.Clock()
		self.running = True
		self.playing = False

		self.img_dir = path.join(path.dirname(__file__), 'img')
		self.load_data()

		self.all_sprites = pygame.sprite.Group()
		self.mobs = pygame.sprite.Group()
		self.player = Player(self)
		self.all_sprites.add(self.player)
		for i in range(8):
			m = Mob(self)
			self.all_sprites.add(m)
			self.mobs.add(m)
		self.bullets = pygame.sprite.Group()
	
	def load_data(self):
		self.background = pygame.image.load(path.join(self.img_dir, 'starfield.png')).convert()
		self.background_rect = self.background.get_rect()
		self.player_img = pygame.image.load(path.join(self.img_dir, 'playerShip1_orange.png')).convert()
		self.player_img = pygame.transform.scale(self.player_img, (50, 38))
		self.player_img.set_colorkey(BLACK)
		# ---------------------------------------修改與新增--------------------------------------
		self.mob_images = []
		mob_list = ['meteorBrown_big1.png', 'meteorBrown_med1.png', 'meteorBrown_med1.png',
					'meteorBrown_med3.png', 'meteorBrown_small1.png', 'meteorBrown_small2.png',
					'meteorBrown_tiny1.png']
		for img_name in mob_list:
			mob_img = pygame.image.load(path.join(self.img_dir, img_name)).convert()
			mob_img.set_colorkey(BLACK)
			self.mob_images.append(mob_img)
		# ---------------------------------------------------------------------------------------
		self.bullet_img = pygame.image.load(path.join(self.img_dir, 'laserRed16.png')).convert()
		self.bullet_img.set_colorkey(BLACK)

	def new(self):
		self.playing = True
		
	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.quitgame()
	
	def update(self):
		self.all_sprites.update()

		if len(self.mobs) < 8:
			m = Mob(self)
			self.all_sprites.add(m)
			self.mobs.add(m)

	def collision_check(self):
		bullet_hits = pygame.sprite.groupcollide(self.mobs, self.bullets, True, True)
		for hit in bullet_hits:
			m = Mob(self)
			self.all_sprites.add(m)
			self.mobs.add(m)
		
		mob_hits = pygame.sprite.spritecollide(self.player, self.mobs, False, pygame.sprite.collide_circle)
		if mob_hits:
			self.quitgame()

	def draw(self):
		self.gameDisplay.blit(self.background, self.background_rect)
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