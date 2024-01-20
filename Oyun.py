
# Modification date: Sun Apr  9 18:24:12 2023

# Production date: Sun Sep  3 15:44:14 2023

"""

Yapılacaklar:
Aşama 1
-Bölüm okuma sistemi kur(bir txt dosyasından bölüm oluşturabilsin)
-Karakter oluştur
-Karo tipi seçimini kolaylaştır(?)
-Duvar oluştur
-Büyütme/küçültme sistemi oluştur

Aşama 2
-Ana menü oluştur
-Ağaç/düşman kesme ve eşya sistemi oluştur.
-Envanter sistemi oluştur
-Kaydetme sistemi oluştur

Aşama 3
-Düşmanlar için yol bulma sistemi oluştur

"""



import pygame
from random import randint
from os import listdir
from Karakter import Karakter
from Karo import Karo
from Agac import Agac

pygame.init()

ekran_buyuklugu = (800, 800)
orijinal_resim_boyutu = 16
oranti = 4
oranli_resim_boyutu = int(orijinal_resim_boyutu * oranti)
bayraklar = pygame.SCALED | pygame.FULLSCREEN | pygame.NOFRAME
ana_pencere = pygame.display.set_mode(ekran_buyuklugu, bayraklar)

cimen_resimleri = []
agac_resimleri = []
karolar = []
agaclar = []
parcaciklar = []


cimen_isimleri = listdir("Icerik/Cimen/")
for sayac, cimen_resmi in enumerate(cimen_isimleri):
	cimen_resimleri.append(pygame.image.load("Icerik/Cimen/" + cimen_resmi).convert_alpha())
	cimen_resimleri[-1] = pygame.transform.scale(cimen_resimleri[-1], (oranli_resim_boyutu, oranli_resim_boyutu))


agac_isimleri = listdir("Icerik/Agac/")
for agac_resmi in agac_isimleri:
	agac_resimleri.append(pygame.image.load("Icerik/Agac/" + agac_resmi).convert_alpha())
	agac_resimleri[-1] = pygame.transform.scale(agac_resimleri[-1], (oranli_resim_boyutu, oranli_resim_boyutu))



def kaydir(karo, kaydirx, kaydiry):
	karo.x = karo.x + kaydirx
	karo.y = karo.y + kaydiry
	return karo


for x in range((400//oranli_resim_boyutu)*4 + 1):
	for y in range((400//oranli_resim_boyutu)*4 + 1):
		rastgele = randint(0, len(cimen_resimleri)-1)
		if y == 8 or y == 9:
			while rastgele%2 == 0:
				rastgele = randint(0, len(cimen_resimleri)-1)
		else:
			while rastgele%2 == 1:
				rastgele = randint(0, len(cimen_resimleri)-1)
		karolar.append(Karo(x * oranli_resim_boyutu, y * oranli_resim_boyutu, rastgele))
		


for x in range(((ekran_buyuklugu[0]//oranli_resim_boyutu)*4 + 1)//8):
	for y in range(((ekran_buyuklugu[0]//oranli_resim_boyutu)*4 + 1)//8):
		#if 2 == randint(0, 5):
		#rastgele = randint(0, len(agac_resimleri)-1)
		rastgele = x%2
		agaclar.append(Agac(x * oranli_resim_boyutu, y * oranli_resim_boyutu, 100, 20, rastgele))
#print(agaclar)




sayac = pygame.time.Clock()
kare_hizi = 60
dongu_calisiyor = True
while dongu_calisiyor:
    sayac.tick(kare_hizi)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dongu_calisiyor = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                dongu_calisiyor = False

    for karo in karolar:
        #karo = kaydir(karo, -1, -1)
        karo.ekrana_ciz(ana_pencere, cimen_resimleri[karo.id])
    for agac in agaclar:
        #agac = kaydir(agac, -1, -1)
        agac.ekrana_ciz(ana_pencere, agac_resimleri[agac.id])


    #agaclar[-1].hasar_al_parcacik(oranli_resim_boyutu, 5, parcaciklar)
    
    for parcacik in parcaciklar:
        parcacik.hareket_et()
        parcacik.ekrana_ciz(ana_pencere)
        yok_et = parcacik.sayac(parcaciklar)
        if yok_et:
            parcaciklar.remove(parcacik)
	
    pygame.display.flip()
pygame.quit()
