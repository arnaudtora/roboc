# -*-coding:Utf-8 -*

from carte import Carte

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

	"""Classe représentant un labyrinthe."""

	def __init__(self, robot, obstacles):
		self.robot = robot
		self.grille = {}
		self.obstacles = obstacles
		self.sizeX = 0
		self.sizeY = 0
 

	def setGrille(self, carte):
		"""Méthode récupérant la carte. Elle fourni aussi les tailles"""
		self.grille = carte.labyrinthe
		self.sizeX  = carte.sizeX
		self.sizeY  = carte.sizeY


	def returnPos(self, pos):
		"""Retourne le contenu d'un position"""
		x, y = pos
		return self.grille[x][y]


	def affichePos(self, pos):
		"""Affiche le contenu d'une position de la carte,
			suivant son abcisse et son ordonnée"""
		x, y = pos
		contenu = self.returnPos(x, y)
		print("Contenu de la case {}x{}: '{}'".format(x, y, contenu))


	def afficheCarte(self):
		""" Méthode d'affichage de la carte
			- un 0 représente un mur
			- un . une porte
			- un X la position du robot"""
		sizeX = 0
		print("\n\t 0123456789")
		while sizeX < self.sizeX:
			line = self.grille[sizeX]
			print("{}\t {}".format(sizeX, line))
			sizeX += 1
		print()


	def replacementObstacles(self):
		"""Méthode rajoutant les obstacles,
			car les portes sont temporairement cachées par le robot"""
		lineNum = 0
		while lineNum < self.sizeX:
			for pos in self.obstacles:
				posX, posY = pos
				if posX == lineNum:
					# 1 obstacle sur cette ligne
					line = self.grille[lineNum]
					line = line[:posY] + "." + line[posY+1:]
					self.grille[lineNum] = line
			lineNum += 1


	def getRobotPosition(self):
		""" Méthode renvoyant la position du robot, sous forme d'un tuple"""
		return (self.robot[0],self.robot[1])


	def afficheRobotPosition(self):
		""" Méthode affichant la position du robot"""
		robot = self.getRobotPosition()
		print("Le robot se trouve en position {}".format(robot))


	def deplacementRobot(self, newPos):
		""" Méthode déplaçant notre robot dans le labyrinthe
			- effacement de la dernière position ('X' -> ' ')
			- déplacement du robot ('X')
			- enregistrement des nouvelles positions"""
		robotX, robotY = self.getRobotPosition()
		newPosX, newPosY = newPos
		print("Déplacement du Robot : {} => ({}x{})"
			.format(self.robot, newPosX, newPosY))
		# Effacement dernière position (' ')
		line = self.grille[robotX]
		line = line[:robotY] + ' ' + line[robotY +1:]
		self.grille[robotX] = line

		# On appel la fonction rajoutant les obstacles,
		# maintenant que nous avons bougé le robot
		self.replacementObstacles()

		# Déplacement du robot
		line = self.grille[newPosX]
		line = line[:newPosY] + 'X' + line[newPosY +1:]
		self.grille[newPosX] = line
		self.robot = (newPosX, newPosY)


	def sortieTrouvee(self, newPos):
		""" Méthode vérifiant si la position pointée vise la sortie, 
			renvoi un booléen"""
		if self.returnPos(newPos) == 'U':
			return True
		else:
			return False
