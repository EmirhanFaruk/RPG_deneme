
# Modification date: Thu Apr 13 23:10:16 2023

# Production date: Sun Sep  3 15:44:14 2023

import pygame
from random import randint
from Karo import Karo
from Parcacik import Parcacik

pygame.init()


class Agac(Karo):
    def __init__(self, x, y, can = 100, materyal = 20, id = 0):
        super().__init__(x, y, id)
        self.can = can
        self.materyal = materyal
		
		
    def hasar_al_parcacik(self, resim_boyutu, parcacik_sayisi, parcaciklar):
        for s in range(parcacik_sayisi):
            vektor = []
            for i in range(2):
                rastgele = randint(2, 8)
                pozneg = randint(0, 1)
                if pozneg == 0:
                    vektor.append(rastgele)
                else:
                    vektor.append(-rastgele)
            parcaciklar.append(Parcacik(self.x + resim_boyutu/2, self.y + resim_boyutu/2, 3, (133,94,66), vektor, 10))