import pygame
from sprites import *
from settings import *
from os import path
import random

class Game:
	def __init__(self):
		pygame.init()
		pygame.mixer.init()

		self.gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
		pygame.display.set_caption(TITLE)

		self.clock = pygame.time.Clock()
		self.running = True
		self.playing = False

		self.img_dir = path.join(path.dirname(__file__), 'img')
		self.snd_dir = path.join(path.dirname(__file__), 'snd')
		self.load_data()

		self.font_filename = pygame.font.match_font('arial')

		self.all_sprites = pygame.sprite.Group()
		self.mobs = pygame.sprite.Group()
		self.player = Player(self)
		self.all_sprites.add(self.player)
		for i in range(8):
			m = Mob(self)
			self.all_sprites.add(m)
			self.mobs.add(m)
		self.bullets = pygame.sprite.Group()

		self.score = 0
	
	def load_data(self):
		self.background = pygame.image.load(path.join(self.img_dir, 'starfield.png')).convert()
		self.background_rect = self.background.get_rect()
		self.player_img = pygame.image.load(path.join(self.img_dir, 'playerShip1_orange.png')).convert()
		self.player_img = pygame.transform.scale(self.player_img, (50, 38))
		self.player_img.set_colorkey(BLACK)
		self.mob_images = []
		mob_list = ['meteorBrown_big1.png', 'meteorBrown_med1.png', 'meteorBrown_med1.png',
					'meteorBrown_med3.png', 'meteorBrown_small1.png', 'meteorBrown_small2.png',
					'meteorBrown_tiny1.png']
		for img_name in mob_list:
			mob_img = pygame.image.load(path.join(self.img_dir, img_name)).convert()
			mob_img.set_colorkey(BLACK)
			self.mob_images.append(mob_img)
		self.bullet_img = pygame.image.load(path.join(self.img_dir, 'laserRed16.png')).convert()
		self.bullet_img.set_colorkey(BLACK)
		# -----------------------------------新增----------------------------------
		self.explosion_anim = {}
		self.explosion_anim['lg'] = []
		self.explosion_anim['sm'] = []
		for i in range(9):
			filename = 'regularExplosion0{}.png'.format(i)
			img = pygame.image.load(path.join(self.img_dir, filename)).convert()
			img.set_colorkey(BLACK)
			img_lg = pygame.transform.scale(img, (75, 75))
			self.explosion_anim['lg'].append(img_lg)
			img_sm = pygame.transform.scale(img, (32, 32))
			self.explosion_anim['sm'].append(img_sm)
		# -------------------------------------------------------------------------

		self.shoot_sound = pygame.mixer.Sound(path.join(self.snd_dir, 'pew.wav'))
		self.expl_sounds = []
		for snd in ['expl3.wav', 'expl6.wav']:
			self.expl_sounds.append(pygame.mixer.Sound(path.join(self.snd_dir, snd)))
		pygame.mixer.music.load(path.join(self.snd_dir, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
		pygame.mixer.music.set_volume(0.4)
	
	def draw_text(self, surf, text, size, x, y):
		font = pygame.font.Font(self.font_filename, size)
		text_surface = font.render(text, True, WHITE)
		text_rect = text_surface.get_rect()
		text_rect.midtop = (x, y)
		surf.blit(text_surface, text_rect)

	def draw_shield_bar(self, surf, x, y, shield):
		if shield < 0:
			shield = 0
		BAR_LENGTH = 100
		BAR_HEIGHT = 10
		fill = (shield / 100) * BAR_LENGTH
		outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
		fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
		pygame.draw.rect(surf, GREEN, fill_rect)
		pygame.draw.rect(surf, WHITE, outline_rect, 2)

	def new(self):
		self.playing = True
		pygame.mixer.music.play(loops=-1)
		
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
			self.score += 50 - hit.radius
			random.choice(self.expl_sounds).play()
			# -----------------------新增-------------------
			expl = Explosion(self, hit.rect.center, 'lg')
			self.all_sprites.add(expl)
			# ----------------------------------------------
			m = Mob(self)
			self.all_sprites.add(m)
			self.mobs.add(m)
		
		mob_hits = pygame.sprite.spritecollide(self.player, self.mobs, True, pygame.sprite.collide_circle)
		for hit in mob_hits:
			self.player.shield -= hit.radius * 2
			random.choice(self.expl_sounds).play()
			# -----------------------新增-------------------
			expl = Explosion(self, hit.rect.center, 'sm')
			self.all_sprites.add(expl)
			# ----------------------------------------------
			m = Mob(self)
			self.all_sprites.add(m)
			self.mobs.add(m)
			if self.player.shield <= 0:
				self.quitgame()

	def draw(self):
		self.gameDisplay.blit(self.background, self.background_rect)
		self.all_sprites.draw(self.gameDisplay)
		self.draw_text(self.gameDisplay, str(self.score), 40, DISPLAY_WIDTH / 2, 30)
		self.draw_shield_bar(self.gameDisplay, 5, 5, self.player.shield)
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