#!/usr/bin/python3
# -*-coding:Utf-8 -*

import os
from carte import Carte
from labyrinthe import Labyrinthe
from robot import Robot

"""Ce fichier contient le code principal du jeu.
Exécutez-le avec Python pour lancer le jeu.
"""

def choixCarte(nbCartes):
	ret = input("Entrez un numéro de labyrinthe pour commencer à jouer: ")
	if not ret.isnumeric():
		return choixCarte(nbCartes)
	ret = int(ret)

	if ret > nbCartes:
		return choixCarte(nbCartes)

	return ret


def chargementSauvegarde():
	ret = input("Voulez-vous charger la carte sauvegardé? (Oui/Non): ")
	if ret.isalpha():
		ret = ret.capitalize()
		if ret == "Oui":
			print("Chargement de la sauvegarde")
			chemin = os.path.join("sauvegarde", nomFichier)
			with open(chemin, "r") as fichier:
				contenu = fichier.read()
				carte.creerLabyrintheDepuisChaine(contenu)
				print("Affichage carte: {}".format(carte))
		elif ret == "Non":
			print("Ok, voici la carte vierge")
		else:
			chargementSauvegarde()
	else:
		chargementSauvegarde()


# On charge les cartes existantes
cartes = []
for nomFichier in os.listdir("cartes"):
	if nomFichier.endswith(".txt"):
		chemin = os.path.join("cartes", nomFichier)
		nomCarte = nomFichier[:-4].lower()
		with open(chemin, "r") as fichier:
			contenu = fichier.read()
			# Création d'une carte, à compléter
			carte = Carte(nomCarte, contenu)
			carte.creerLabyrintheDepuisChaine(contenu)
			cartes.append(carte)

# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
	print("  {} - {}".format(i + 1, carte.nom))

# Choix de la carte
numeroCarte = choixCarte(len(cartes))
carte = cartes[numeroCarte-1]
print("\nLa carte choisi est {}".format(carte.nom))

# Une sauvegarde existe t'elle pour cette carte ? (sauvegarde/nomCarteSave.txt)
for nomFichier in os.listdir("sauvegarde"):
	if nomFichier.endswith(".txt") and nomFichier.startswith(carte.nom):
		print("\nUne sauvegarde pour {} à été trouvé, au nom de {}".format(carte.nom, nomFichier))
		chargementSauvegarde()


# On cherche la position du robot dans la carte
posRobotX, posRobotY = carte.rechercheRobot()
obstacles = carte.obstacles

# On instancie notre robot
robot = Robot("R2D2", posRobotX, posRobotY)

#Instanciation du labyrinthe
labyrinthe = Labyrinthe(robot, obstacles)
labyrinthe.setGrille(carte)

# Affichage de la carte
labyrinthe.afficheCarte()

# Boucle de jeu
gameInProgress = True
while gameInProgress != False:
	# Affichage de la carte à chaque coup	
	robot.afficheRobotPosition()

	# Sauvegarde automatique du jeu à chaque coup
	labyrinthe.sauvegardeJeu(carte.nom)
	
	newPos = (-1,-1)
	while newPos == (-1,-1):
		entree  = input("Où voulez-vous aller: ")
		if entree == "Q" or entree == "q": # Fin du jeu			
			print("Sortie du jeu")
			exit()
		else:
			newPos = labyrinthe.demandeNewPosition(entree)

	# Vérification du déplacement ?
	if not labyrinthe.isDeplacementValid(newPos):
		print("Le déplacement en {} est invalide".format(newPos))
		continue

	# A t'on trouvé la porte (à faire avant de se déplacer!)
	if labyrinthe.sortieTrouvee(newPos):
		gameInProgress = False
	
	# Déplacement Robot
	labyrinthe.deplacementRobot(newPos)
	labyrinthe.afficheCarte()


print("Félicitations ! Vous avez gagné !")
print("Sortie du jeu")