
# Modification date: Sat Apr  8 20:28:34 2023

# Production date: Sun Sep  3 15:44:14 2023

import pygame

pygame.init()

class Parcacik:
    def __init__(self, x, y, boyut, renk, vektor, sure):
        self.x, self.y, self.boyut, self.renk, self.vektor, self.sure = x, y, boyut, renk, vektor, sure
    
    def sayac(self, liste):
        self.sure -= 1
        return self.sure <= 0
    
    def hareket_et(self):
        self.x += self.vektor[0]
        self.y += self.vektor[1]
    
    def ekrana_ciz(self, pencere):
        pygame.draw.rect(pencere, self.renk, pygame.Rect((self.x, self.y), (self.boyut, self.boyut)))