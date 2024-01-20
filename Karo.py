
# Modification date: Thu Mar  2 22:20:30 2023

# Production date: Sun Sep  3 15:44:14 2023

import pygame

pygame.init()

class Karo:
	def __init__(self, x, y, id=0):
		self.x, self.y = x, y
		self.id = id
		
		
	
	def ekrana_ciz(self, pencere, resim):
		pencere.blit(resim, (self.x, self.y))