import pygame
import random
pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption("DVD")

WHITE = (255, 255, 255)
color = (67,158,232)

ball_x = 400
ball_y = 0
y = 1 # 這是代表方向，所以加個direction會好點
x = 1
clock = pygame.time.Clock()

def change_color():
        a = random.randint(0,225) # 這邊使用r, g, b作為變數名稱會好點 
        b = random.randint(0,225)
        c = random.randint(0,225)
        color = (a,b,c)
        return color
        

playing = True
while playing:
      for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        playing = False
      ball_y += 10 * y
      ball_x += 12 * x
      if ball_y <= 0:
            y = 1
            color = change_color()
            
      elif ball_y + 60 >= 600:
            y = -1
            x = -1
            color = change_color()
      if ball_x + 140 >= 800:
              x = -1
              color = change_color()

      elif ball_x <= 0:
              x = 1
              color = change_color()
            
      gameDisplay.fill(WHITE)
      pygame.draw.ellipse(gameDisplay, color, (ball_x, ball_y,140,60))
      pygame.display.update()
      clock.tick(30)

pygame.quit()
quit()