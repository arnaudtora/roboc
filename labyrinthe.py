# -*-coding:Utf-8 -*

from carte import Carte

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

	"""Classe représentant un labyrinthe."""

	def __init__(self, robot, obstacles):
		self.robot = robot
		self.grille = {}
		self.sizeX = 0
		self.sizeY = 0
 
	def setGrille(self, carte):
		"""Méthode récupérant la carte. Elle fourni aussi les tailles"""
		self.grille = carte.labyrinthe
		self.sizeX  = carte.sizeX
		self.sizeY  = carte.sizeY

	def returnPos(self, x, y):
		"""Retourne le contenu d'un position"""
		return self.grille[x][y]

	def affichePos(self, x, y):
		"""Affiche le contenu d'une position de la carte,
			suivant son abcisse et son ordonnée"""
		contenu = self.returnPos(x, y)
		print("Contenu de la case {}x{}: '{}'".format(x, y, contenu))

	def afficheCarte(self):
		sizeY = 0
		print("\n\t 0123456789")
		while sizeY <= self.sizeY:
			line = self.grille[sizeY]
			print("{}\t {}".format(sizeY, line))
			sizeY += 1
		print()

	def getPositionRobot(self):
		return (self.robot[0],self.robot[1])

	def afficheRobotPosition(self):
		robot = self.getPositionRobot()
		print("Le robot se trouve en position {}".format(robot))

	def deplacementRobot(self, newPosX, newPosY):
		robotX, robotY = self.getPositionRobot()
		print("Déplacement du Robot : {} => ({}x{})"
			.format(self.robot, newPosX, newPosY))
		# Effacement dernière position (' ')
		line = self.grille[robotX]
		line = line[:robotY] + ' ' + line[robotY +1:]
		self.grille[robotX] = line

		# Déplacement du robot
		line = self.grille[newPosX]
		line = line[:newPosY] + 'X' + line[newPosY +1:]
		self.grille[newPosX] = line
