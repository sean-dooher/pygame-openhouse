import pygame
class Sprite:
	def __init__(self, image, x, y):
		self.image = pygame.image.load(image)
		self.x = x
		self.y = y
		self.x_speed = 0
		self.y_speed = 0

	def move(self, x, y):
		self.x += x
		self.y += y

	def update(self):
		self.x += self.x_speed
		self.y += self.y_speed
	
	def draw(self, screen):
		screen.blit(self.image, (self.x, self.y))