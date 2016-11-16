# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""

class Carte:
	"""Objet de transition entre un fichier et un labyrinthe."""

	def __init__(self, nom, chaine):
		self.nom = nom
		self.labyrinthe = {}
		self.obstacles = []
		self.sizeX = 0
		self.sizeY = 0


	def __repr__(self):
		return "<Carte {}, dont la taille est {}x{}>" \
			.format(self.nom, self.sizeX, self.sizeY)


	def creerLabyrintheDepuisChaine(self, chaine):
		"""Méthode permettant la création d'un labyrinthe à partir
			d'une chaine de caractères"""
		sizeY = 0

		# Lecture de la chaine, et sauvegarde en grille
		for lineNum, line in enumerate(chaine.split("\n")):
			self.labyrinthe[lineNum] = line

			# A t'on des obstacles
			posY = line.find(".")
			if posY >= 0:
				posObstacle = (lineNum, posY)
				self.obstacles.append(posObstacle)

			# Récupération taille Max
			if sizeY < len(line):
				sizeY = len(line)

		# Enregistrement de nos données
		self.sizeX = lineNum+1
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
