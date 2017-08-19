from sprite import *
import time
import random
import pygame


game_on = True
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1280, 720))
background = pygame.transform.scale(pygame.image.load("background.png"), (1280, 720))
FRAME_RATE = 60


#CREATE A PLAYER WITH THE IMAGE 'cat.jpg' and start them at (150, 150)
player = Sprite('cat.jpg', 150, 150)



while game_on:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
				game_on = False
	screen.blit(background, (0,0))
	pressed = pygame.key.get_pressed()




	pygame.display.flip()
	clock.tick(FRAME_RATE)
print("GAME OVER")