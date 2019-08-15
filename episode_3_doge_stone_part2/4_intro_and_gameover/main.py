import pygame
from random import randint # 引入randint
import time # 新增
from settings import *
from sprites import Rabbit, Stone

class Game:
	def __init__(self):
		pygame.init()
		
		self.gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
		pygame.display.set_caption(TITLE)

		self.clock = pygame.time.Clock()
		self.playing = False # 修改
		self.intro = True # 新增

		self.last_spawn_stone = pygame.time.get_ticks()
		self.stones = []

		self.rabbit = Rabbit(self)
		
		self.doged_stone = 0
	
	# -------------------新增------------------
	def new(self):
		self.intro = False
		self.playing = True
		self.stones = []
		self.rabbit = Rabbit(self)
		self.doged_stone = 0
		self.run()
	# ----------------------------------------
	
	def events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.quitgame() # 修改
	
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
				self.doged_stone += 1

		for stone in self.stones:
			if self.collision_check(self.rabbit, stone):
				self.playing = False
				self.gameover() # 新增

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
		self.gameDisplay.fill(WHITE)
		self.draw_text("Doged Stone: " + str(self.doged_stone), 25, BLACK, 80, 15)
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
	
	def draw_text(self, text, size, color, x, y):
		font = pygame.font.SysFont('arial', size)
		text_surface = font.render(text, True, color)
		text_rect = text_surface.get_rect()
		text_rect.center = (x, y)
		self.gameDisplay.blit(text_surface, text_rect)
	
	# -----------------------------------------------------新增----------------------------------------
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
		self.draw_text("Lose!", 80, BLACK, 400, 250)
		pygame.display.update()
		time.sleep(2)
		self.game_intro()
	
	# ----------------------------------------------------------------------------------------------

game = Game()
game.game_intro() # 修改
pygame.quit()
quit()