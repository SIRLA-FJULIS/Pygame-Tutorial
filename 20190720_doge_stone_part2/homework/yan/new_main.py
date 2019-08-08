import pygame
from random import randint
import time
from settings import *
from sprites import Rabbit, Stone, Carrot, Specialcarrot

class Game:
	def __init__(self):
		pygame.init()
		
		self.gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
		pygame.display.set_caption(TITLE)

		self.clock = pygame.time.Clock()
		self.playing = False
		self.intro = True 

		self.last_spawn_stone = pygame.time.get_ticks()
		self.last_spawn_carrot = pygame.time.get_ticks()
		self.last_spawn_specialcarrot = pygame.time.get_ticks()
		self.stones = []
		self.carrots = []
		self.specialcarrots = []

		self.rabbit = Rabbit(self)
		
		self.doged_stone = 0
		self.doged_carrot = 0

	def new(self):
		self.intro = False
		self.playing = True
		self.stones = []
		self.carrots = []
		self.specialcarrots = []
		self.rabbit = Rabbit(self)
		self.doged_stone = 0
		self.doged_carrot = 0
		self.run()
	
	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.quitgame()
	
	def update(self):
		now = pygame.time.get_ticks()
		if now - self.last_spawn_stone >= 2000:
			self.stones.append(Stone(self))
			self.last_spawn_stone = now
		
		if now - self.last_spawn_carrot >= 5000:
			self.carrots.append(Carrot(self))
			self.last_spawn_carrot = now

		if now - self.last_spawn_specialcarrot >= 10000:
			self.specialcarrots.append(Specialcarrot(self))
			self.last_spawn_specialcarrot = now
			
		self.rabbit.update()
		
		for stone in self.stones:
			stone.update()
			if stone.pos_y >= 600:
				self.stones.remove(stone)
				self.doged_stone += 1
		
		for carrot in self.carrots:
			carrot.update()
			if self.collision_check(self.rabbit, carrot):
				self.carrots.remove(carrot)
				self.doged_carrot += 1

		for specialcarrot in self.specialcarrots:
			specialcarrot.update()
			if self.collision_check(self.rabbit, specialcarrot):
				self.specialcarrots.remove(specialcarrot)
				self.rabbit.speed_x += 10

		for stone in self.stones:
			if self.collision_check(self.rabbit, stone):
				self.playing = False
				self.gameover()

	def collision_check(self, obj_one, obj_two):
		'''
		Check collision using rect attribute from your object.
		You can get rect using Surface.get_rect()
		'''
		pos_one = obj_one.rect.topleft
		pos_two = obj_two.rect.topleft
		width_one = obj_one.rect.width
		height_one = obj_one.rect.height
		width_two = obj_two.rect.width
		height_two = obj_two.rect.height
		
		if (pos_two[1] < pos_one[1] and pos_two[1] + height_two >= pos_one[1]) or \
		   (pos_two[1] >= pos_one[1] and pos_two[1] + height_two <= pos_one[1] + height_one) or \
		   (pos_two[1] <= pos_one[1] + height_one and pos_two[1] + height_two > pos_one[1] + height_one):
			if (pos_two[0] < pos_one[0] and pos_two[0] + width_two >= pos_one[0]) or \
			   (pos_two[0] >= pos_one[0] and pos_two[0] + width_two <= pos_one[0] + width_one) or \
			   (pos_two[0] <= pos_one[0] + width_one and pos_two[0] + width_two > pos_one[0] + width_one):
			   return True
			   
		return False
	
	def draw(self):
		self.gameDisplay.blit(background, (0,0))
		self.draw_text("Doged Stone: " + str(self.doged_stone), 25, BLACK, 100, 30)
		self.draw_text("Carrot Bonus: " + str(self.doged_carrot), 25, BLACK, 100, 70)
		self.rabbit.draw()
		for stone in self.stones:
			stone.draw()
		pygame.display.update()
		
		for carrot in self.carrots:
			carrot.draw()
		pygame.display.update()

		for specialcarrot in self.specialcarrots:
			specialcarrot.draw()
		pygame.display.update()
	
	def run(self):
		# Game Loop
		while self.playing:
			self.events()
			self.update()
			self.draw()
			self.clock.tick(FPS)
	
	def draw_text(self, text, size, color, x, y):
		font = pygame.font.SysFont('arial', size)
		text_surface = font.render(text, True, color)
		text_rect = text_surface.get_rect()
		text_rect.center = (x, y)
		self.gameDisplay.blit(text_surface, text_rect)

	def button(self, text, posX, posY, width, height, inActiveColor, activeColor, action=None):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		if (mouse[0] > posX and mouse[0] < posX+width) and (mouse[1] > posY and mouse[1] < posY+height):
			pygame.draw.rect(self.gameDisplay, activeColor, (posX, posY, width, height))
			if click[0] == 1 and action != None:
				action()
		else:
			pygame.draw.rect(self.gameDisplay, inActiveColor, (posX, posY, width, height))
		self.draw_text(text, 25, WHITE, posX+(width/2), posY+(height/2))
	
	def quitgame(self):
		pygame.quit()
		quit()
		
	def game_intro(self):
		self.intro = True
		while self.intro:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.quitgame()
			self.gameDisplay.fill(WHITE)
			self.draw_text("Rabbit Run!", 80, BLACK, 400, 200)
			self.button("Start", 200, 450, 100, 50, RED, LIGHT_RED, action=self.new)
			self.button("Quit", 500, 450, 100, 50, GREEN, LIGHT_GREEN, action=self.quitgame)
			pygame.display.update()
			self.clock.tick(30)
	
	def gameover(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						self.game_intro()
				if event.type == pygame.QUIT:
					self.quitgame()
			self.draw_text("Lose!", 80, WHITE, 400, 250)
			self.draw_text("Press space to restart", 25, WHITE, 400, 300)
			pygame.display.update()


game = Game()
game.game_intro()
pygame.quit()
quit()