# -*-coding:Utf-8 -*

import os
from carte import Carte

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

	"""Classe représentant un labyrinthe."""

	def __init__(self, robot, obstacles):
		""" Constructeur de notre labyrinthe, qui contient les objets
			- robot (tuple de position)
			- grille du labyrinthe
			- liste des obstacles
			- taille en X
			- taille en Y   """
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

		if x >= self.sizeX or y >= self.sizeY:
			return "-"
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
		print("\n\t 01234567890")
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


	def isDeplacementValid(self, newPos):
		"""Méthode vérifiant si le déplacement est valide
			- on doit rester sur la carte
			- on ne peut pas traverser de mur
			La fonction revoi un booleen"""
		robotX, robotY = self.getRobotPosition()
		newPosX, newPosY = newPos

		# Selon quel axe se déplace t'on ?
		if robotX == newPosX:    # Déplacement selon l'axe Y
			if robotY < newPosY: # Déplacement vers la droite
				while robotY < newPosY:
					robotY += 1
					if self.returnPos((robotX, robotY)) == "O":
						print("Nous sommes sur un mur, déplacement invalide")
						return False
			else:                # Déplacement vers la gauche
				while robotY > newPosY:
					robotY -= 1
					if self.returnPos((robotX, robotY)) == "O":
						print("Nous sommes sur un mur, déplacement invalide")
						return False
		else:                    # Déplacement selon X
			if robotX < newPosX: # Déplacement vers le bas
				while robotX < newPosX:
					robotX += 1
					if self.returnPos((robotX, robotY)) == "O":
						print("Nous sommes sur un mur, déplacement invalide")
						return False
			else:                # Déplacement vers le haut
				while robotX > newPosX:
					robotX -= 1
					if self.returnPos((robotX, robotY)) == "O":
						print("Nous sommes sur un mur, déplacement invalide")
						return False

		# Vérification si nous sommes toujours sur la carte
		if robotX >= self.sizeX or robotY >= self.sizeY:
			print("Nous sommes hors carte, déplacement invalide")
			return False

		# Toutes les positions traversées sont valides
		return True


	def demandeNewPosition(self, entree):
		"""Méthode permettant de trouver la position voulue, en lisant l'entrée utilisateur
			elle renvoi un tuple de position
			L'entrée est sous forme E4 (direction et distance)
			Une entrée avec seulement une direction veut dire E1
			Il faut aussi vérifier le type d'entrée (une lettre, et un chiffre optionnel"""
		robotX, robotY = self.getRobotPosition()

		# Lecture, et vérification des données
		if len(entree) == 0:
			print("Err : valeur d'entrée invalide")
			return (-1,-1)

		direction = entree[0]
		if direction.isalpha():
			direction = direction.upper()
		else:
			print("Err : valeur d'entrée invalide")
			return (-1,-1)

		if len(entree) == 1:
			distance = 1
		else:
			distance = entree[1:]
			if distance.isnumeric():
				distance = int(distance)
			else:
				print("Err : valeur d'entrée invalide")
				return (-1,-1)

		# Conversion de l'entrée en position (tuple)
		if direction == "E":     # Droite
			robotY += distance
		elif direction == "W":   # Gauche
			robotY -= distance
		elif direction == "S":   # Bas
			robotX += distance
		elif direction == "N":   # Haut
			robotX -= distance
		
		return (robotX,robotY)


	def sortieTrouvee(self, newPos):
		""" Méthode vérifiant si la position pointée vise la sortie, 
			renvoi un booléen"""
		if self.returnPos(newPos) == 'U':
			return True
		else:
			return False

	def sauvegardeJeu(self, nom):
		""" Méthode sauvegardant le jeu pour y revenir ultérieurment"""
		nomFichier = "sauvegarde/" + nom + "Save.txt"
		with open(nomFichier, "w") as fichier:
			lineNum = 0
			while lineNum < self.sizeX:
				# Saut de ligne, sauf pour la 1ere ligne
				if not lineNum == 0:
					ligne = "\n"
				else:
					ligne = ""
				ligne += self.grille[lineNum] 

				# Ecriture dans le fichier
				fichier.write(ligne)
				lineNum += 1