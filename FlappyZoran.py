"""
	TO DO:
		pozadina
		okvir
		MENI
		Score
		HighScore
"""
# nesto zbog cega ne radi program 

import pygame
import time
import random
import math


black = (0, 0 , 0)
white = (255, 255, 255)
green = (0, 200, 0)
red = (255, 0, 0)
siva = (100, 100, 100)
ljubicasta = (128, 0, 128)
plava = (0, 0, 255)


sirina = 1280
duzina = 720





pygame.init()
pygame.mixer.init()
print("TriPitagorineTeoreme")

pygame.display.set_caption('GlupaZoranovaGlava')
ekran = pygame.display.set_mode((sirina, duzina))

sat = pygame.time.Clock()
font = pygame.font.SysFont(None, 75)
skokSound = pygame.mixer.Sound('gameover.wav')


"""Vrednosti"""

dimZid = (120, 170) #  nisu dimenzije zida vec otvora
dimZoran = (100, 100)


brzina_skoka = -1 #  -2
odraz = -50 #  -25
g = 0.4 #  0.3
brzina_igrice = -10 #  -15
zid_prored = 2*sirina/3 #  2/3


strDaNe = "GLUPiraj se ponovo?? (y/n)"
strEndGame = "Glup si brate"
strPrd = 'fart.png'
strZoran = 'zoran.png'
strZid = 'prepreka.png'
pozdravniSTR = 'Enter!'
radi = True	




"""KLASE & FUNKCIJE"""


def poruka(msg, boja, koordinate):
	tekst = font.render(msg, True, boja)
	ekran.blit(tekst, koordinate)

class TKarakter(object):
	"""Karakter i njegova kinematika"""
	def __init__(self, str, dim):
		self.img = pygame.image.load(str)
		self.img = pygame.transform.scale(self.img, (math.floor(dim[0]), math.floor(dim[1])))

		self.aY = 0

		self.x = self.y = self.xV = self.yV = 0

		self.dim = dim
	
	def crtaj(self, ekran):
		ekran.blit(self.img, (self.x, self.y))

	def updejt(self):
		self.x += self.xV
		self.y += self.yV

		self.yV += self.aY
		



class TSkok(object):
	"""Slika skoka i njeno kretanje"""
	def __init__(self, str):
		self.img = pygame.image.load(str)
		self.img = pygame.transform.scale(self.img, (zoran.dim[0], zoran.dim[1]))

		self.x = zoran.x
		self.y = zoran.y + zoran.dim[1]

		self.xV = zid.xV
		self.yV = zoran.yV / 2
		self.aY = -g/3


	def crtaj(self, ekran):
		ekran.blit(self.img, (self.x, self.y))

	def updejt(self):
		self.x += self.xV	
		self.y += self.yV

		self.yV += self.aY

class TSkokovi(object):
	"""niz svih skokova"""
	def __init__(self):
		self.skokovi = []

	def dodaj(self, str):
		temp = TSkok(str)
		self.skokovi.append(temp)	

	def crtaj(self, ekran):
		# for i in range(0, 1):
		# i = self.skokovi[0]
		# self.skokovi[i].crtaj(ekran)			
		for i in self.skokovi:
			i.crtaj(ekran)

	def updejt(self):
		for i in self.skokovi:
			i.updejt()






class TPrepreka(object):
	"""crtanje zida"""
	def __init__(self, str, dim, poz):
		temp = pygame.image.load(str)
		
		(self.x, self.y) = poz
		self.dim = dim		

		# dim[1] = self.y
		self.imgG = pygame.transform.scale(temp, (int(dim[0]), int(self.y)))

		# dim[1] = duzina - self.y - self.dim[1]
		self.imgD = pygame.transform.scale(temp, (int(dim[0]), int(duzina - self.y - self.dim[1])))
		
		self.xV = self.yV = 0

		self.ziv = True


	def crtaj(self, ekran):
		ekran.blit(self.imgG, (self.x, 0))
		ekran.blit(self.imgD, (self.x, self.y + self.dim[1]))


	def updejt(self):
		self.x += self.xV
		self.y += self.yV

		if self.x <= -self.dim[0]:
			# self.x = sirina
			# self.y = random.randint(150, duzina - 150)
			self.ziv = False




def sudar(obj1, obj2):
	if obj1.x + obj1.dim[0] >= obj2.x and obj1.x <= obj2.x + obj2.dim[0]:
		if not (obj1.y > obj2.y and obj1.y + obj1.dim[1] < obj2.y + obj2.dim[1]):
			return True
	return False


def randPozicija(prepreka):
	return (sirina, random.randint(50, duzina-prepreka[1]))




"""MENI"""

ekran.fill(ljubicasta)

pygame.draw.rect(ekran, black, (0, duzina/5, sirina, duzina/6))
poruka(pozdravniSTR, plava, [sirina/3, duzina/5])

pygame.draw.rect(ekran, black, (0, 4*duzina/5, sirina, duzina/6))


pygame.display.update()


promenljiva = True

while promenljiva:
	
	for dogadjaj in pygame.event.get():

		if dogadjaj.type == pygame.QUIT:
			radi = promenljiva = False

		if dogadjaj.type == pygame.KEYDOWN:
			if dogadjaj.key == pygame.K_ESCAPE:
				radi = promenljiva =  False
			
			if dogadjaj.key == pygame.K_RETURN:
				promenljiva = False
				







"""GLAVNA PETLJA"""
while radi:

	""" inicijalizacije """

	skor = 0

	zoran = TKarakter(strZoran, dimZoran)

	zoran.x = sirina/10
	zoran.y = duzina/3
	zoran.aY = g


	zid = TPrepreka(strZid, dimZid, randPozicija(dimZid))

	zid.x = sirina 


	zid1 = TPrepreka(strZid, dimZid, randPozicija(dimZid))

	zid1.x = sirina + zid_prored

	zid.xV = zid1.xV = brzina_igrice

	skokovi = TSkokovi()
	skokovi.dodaj(strPrd)


	# brojac = 50
	# o = 5
	nijeIzgubio = True
	providnost = 255

	while nijeIzgubio:
		zid.xV = zid1.xV = brzina_igrice

		"""dogadjaji sa tastature"""
		
		for dogadjaj in pygame.event.get():

			if dogadjaj.type == pygame.QUIT:
				nijeIzgubio = False

			if dogadjaj.type == pygame.KEYDOWN:
				if dogadjaj.key == pygame.K_ESCAPE:
					nijeIzgubio = False
				if dogadjaj.key == pygame.K_UP:
					# skokSound.play()
					skokovi.dodaj(strPrd)
					zoran.xV = 0
					zoran.y += odraz
					zoran.yV = brzina_skoka

				if dogadjaj.key == pygame.K_SPACE:
					zoran.xV = 0
					zoran.yV = 0


		"""ispitivanje sudara"""


		if zoran.x >= sirina - zoran.dim[0] or zoran.x <= 0:
			zoran.xV = -zoran.xV
		if zoran.y >= duzina - zoran.dim[1] or zoran.y <= 0:
			zoran.yV = -zoran.yV	
	 
		if sudar(zoran, zid) or sudar(zoran, zid1):
			nijeIzgubio = False


		"""
			stvaranje prepreka
		"""

		if not zid.ziv:
			zid = TPrepreka(strZid, dimZid, randPozicija(dimZid))
			zid.x = zid1. x + zid_prored
			skor += 1
		
		if not zid1.ziv:
			zid1 = TPrepreka(strZid, dimZid, randPozicija(dimZid))
			zid1.x = zid.x + zid_prored
			skor += 1


		"""crtanje i updejt"""

		ekran.fill(ljubicasta)


		poruka("Skaci!!!", white, [200, 200])
		msg = "Skor: " + str(skor)
		poruka(msg, green, [300, 300])

		zoran.crtaj(ekran)
		zid.crtaj(ekran)
		zid1.crtaj(ekran)
		skokovi.crtaj(ekran)

		pygame.display.update()
		
		sat.tick(35)

		zoran.updejt()
		zid.updejt()
		zid1.updejt()
		skokovi.updejt()
		

	"""restart ili quit ekran"""

	skokSound.play()
	time.sleep(2)
	ekran.fill(red)
	poruka(strEndGame, white, [sirina/2, duzina/3])
	# print("ovde")
	poruka(strDaNe, green, [sirina/5, duzina/2])


	pygame.display.update()
	q = True
	while q:
		for dogadjaj in pygame.event.get():
			if dogadjaj.type == pygame.KEYDOWN:
				if dogadjaj.key == pygame.K_y:
					q = False
				if dogadjaj.key == pygame.K_n or dogadjaj.key == pygame.K_ESCAPE:
					q = False	
					radi = False

pygame.quit()
quit()
