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
		self.powerups = pygame.sprite.Group() # 新增

		self.score = 0
	
	def load_data(self):
		self.background = pygame.image.load(path.join(self.img_dir, 'starfield.png')).convert()
		self.background_rect = self.background.get_rect()
		self.player_img_orig = pygame.image.load(path.join(self.img_dir, 'playerShip1_orange.png')).convert()
		self.player_img = pygame.transform.scale(self.player_img_orig, (50, 38))
		self.player_img.set_colorkey(BLACK)
		self.player_mini_img = pygame.transform.scale(self.player_img_orig, (25, 19))
		self.player_mini_img.set_colorkey(BLACK)
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
		self.explosion_anim = {}
		self.explosion_anim['lg'] = []
		self.explosion_anim['sm'] = []
		self.explosion_anim['player'] = []
		for i in range(9):
			filename = 'regularExplosion0{}.png'.format(i)
			img = pygame.image.load(path.join(self.img_dir, filename)).convert()
			img.set_colorkey(BLACK)
			img_lg = pygame.transform.scale(img, (75, 75))
			self.explosion_anim['lg'].append(img_lg)
			img_sm = pygame.transform.scale(img, (32, 32))
			self.explosion_anim['sm'].append(img_sm)
			filename = 'sonicExplosion0{}.png'.format(i)
			img = pygame.image.load(path.join(self.img_dir, filename)).convert()
			img.set_colorkey(BLACK)
			self.explosion_anim['player'].append(img)
		# ----------------------------------------------------新增-----------------------------------------------
		self.powerup_images = {}
		self.powerup_images['shield'] = pygame.image.load(path.join(self.img_dir, 'shield_gold.png')).convert()
		self.powerup_images['shield'].set_colorkey(BLACK)
		self.powerup_images['gun'] = pygame.image.load(path.join(self.img_dir, 'bolt_gold.png')).convert()
		self.powerup_images['gun'].set_colorkey(BLACK)
		# -------------------------------------------------------------------------------------------------------

		self.shoot_sound = pygame.mixer.Sound(path.join(self.snd_dir, 'pew.wav'))
		self.expl_sounds = []
		for snd in ['expl3.wav', 'expl6.wav']:
			self.expl_sounds.append(pygame.mixer.Sound(path.join(self.snd_dir, snd)))
		self.player_die_sound = pygame.mixer.Sound(path.join(self.snd_dir, 'rumble1.ogg'))
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

	def draw_lives(self, surf, x, y, lives, img):
		for i in range(lives):
			img_rect = img.get_rect()
			img_rect.x = x + 30 * i
			img_rect.y = y
			surf.blit(img, img_rect)

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
			expl = Explosion(self, hit.rect.center, 'lg')
			self.all_sprites.add(expl)
			# ----------------------------新增----------------------------
			if random.random() > 0.9:
				pow = Pow(self, hit.rect.center)
				self.all_sprites.add(pow)
				self.powerups.add(pow)
			# ------------------------------------------------------------
			m = Mob(self)
			self.all_sprites.add(m)
			self.mobs.add(m)
		
		mob_hits = pygame.sprite.spritecollide(self.player, self.mobs, True, pygame.sprite.collide_circle)
		for hit in mob_hits:
			self.player.shield -= hit.radius * 2
			random.choice(self.expl_sounds).play()
			expl = Explosion(self, hit.rect.center, 'sm')
			self.all_sprites.add(expl)
			m = Mob(self)
			self.all_sprites.add(m)
			self.mobs.add(m)
			if self.player.shield <= 0:
				self.player_die_sound.play
				self.death_explosion = Explosion(self, self.player.rect.center, 'player')
				self.all_sprites.add(self.death_explosion)
				self.player.hide()
				self.player.lives -= 1
				self.player.shield = 100
		if self.player.lives == 0 and not self.death_explosion.alive():
			self.quitgame()
			
		# ---------------------------------------新增--------------------------------
		pow_hits = pygame.sprite.spritecollide(self.player, self.powerups, True)
		for hit in pow_hits:
			if hit.type == 'shield':
				self.player.shield += random.randrange(10, 30)
				if self.player.shield >= 100:
					self.player.shield = 100
			if hit.type == 'gun':
				pass
		# ----------------------------------------------------------------------------

	def draw(self):
		self.gameDisplay.blit(self.background, self.background_rect)
		self.all_sprites.draw(self.gameDisplay)
		self.draw_text(self.gameDisplay, str(self.score), 40, DISPLAY_WIDTH / 2, 30)
		self.draw_shield_bar(self.gameDisplay, 5, 5, self.player.shield)
		self.draw_lives(self.gameDisplay, DISPLAY_WIDTH - 100, 5, self.player.lives, self.player_mini_img)
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