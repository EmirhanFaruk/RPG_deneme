
# Modification date: Sun Apr  9 01:07:52 2023

# Production date: Sun Sep  3 15:44:14 2023

import pygame

pygame.init()

class Karakter:
    def __init__(self, x, y, vektor, araclar, envanter, para):
        self.x, self.y, self.vektor, self.araclar, self.envanter, self.para = x, y, vektor, araclar, envanter, para
    
    def hareket_et(self, etkenler, surtunme):
        vektor[0] += etkenler[0]
        vektor[1] += etkenler[1]
        if abs(vektor[0]) - abs(surtunme) < 0:
            vektor[0] = 0
        else:
            if vektor[0] > 0:
                vektor[0] -= surtunme
            else:
                vektor[0] += surtunme
        
        if abs(vektor[1]) - abs(surtunme) < 0:
            vektor[1] = 0
        else:
            if vektor[1] > 0:
                vektor[1] -= surtunme
            else:
                vektor[1] += surtunme
    
    def cakisma(self, cakisabilecekler_listesinin_listesi, boyut):
        for cakisabilecekler_listesi in cakisabilecekler_listesinin_listesi:
            for cakisabilecek_obje in cakisabilecekler_listesi:
                if 