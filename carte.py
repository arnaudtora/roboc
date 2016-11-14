# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""

class Carte:
	"""Objet de transition entre un fichier et un labyrinthe."""

	def __init__(self, nom, chaine):
		self.nom = nom
		self.labyrinthe = {}
		self.sizeX = 0
		self.sizeY = 0

	def __repr__(self):
		return "<Carte {}, dont la taille est {}x{}>" \
			.format(self.nom, self.sizeX, self.sizeY)

	def creerLabyrintheDepuisChaine(self, chaine):
		"""Méthode permettant la création d'un labyrinthe à partir
			d'une chaine de caractères"""
		sizeX = 0
		sizeY = -1

		# Lecture de la chaine, et sauvegarde en grille
		for line in chaine.split("\n"):
			sizeY += 1
			self.labyrinthe[sizeY] = line
			if sizeX < len(line):
				sizeX = len(line)

		# Enregistrement de nos données
		self.sizeX = sizeX
		self.sizeY = sizeY

	def rechercheRobot(self):
		"""Cette fonction recherche le robot (X) dans la carte, 
			et renvoi sa position sous forme d'un tupple"""

		for numLine in self.labyrinthe:
			posY = self.labyrinthe[numLine].find("X")
			if posY >= 0:
				pos = (numLine, posY)
				return pos

		raise TypeError ("La carte ne contient pas de robot")