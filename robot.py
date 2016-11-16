# -*-coding:Utf-8 -*

""" Ce module contient la classe Robot."""

class Robot:
	""" Classe du robot, le définissant, et gérant sa position"""

	def __init__(self, nom, posX, posY):
		""" Constructeur de notre robot, il peut être défini par
			- une position
			- un nom, santé, couleur ..."""
		self.nom  = nom
		self.posX = posX
		self.posY = posY

	def __repr__(self):
		return "Je m'appel {} et je me trouve en {}".format(self.nom, (self.posX, self.posY))

	def afficheRobotPosition(self):
		""" Méthode affichant la position du robot"""
		pos = self.getRobotPosition()
		print("Le robot se trouve en position {}".format(pos))


	def setPosition(self, posX, posY):
		""" Méthode pour setter une position du robot """
		self.posX = posX
		self.posY = posY


	def getRobotPosition(self):
		""" Méthode getter, renvoyant la position du robot, sous forme d'un tuple"""
		return (self.posX, self.posY)