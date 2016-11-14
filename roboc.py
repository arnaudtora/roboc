#!/usr/bin/python3
# -*-coding:Utf-8 -*

import os
from carte import Carte
from labyrinthe import Labyrinthe

"""Ce fichier contient le code principal du jeu.
Exécutez-le avec Python pour lancer le jeu.
"""


# On charge les cartes existantes
cartes = []
for nomFichier in os.listdir("cartes"):
	if nomFichier.endswith(".txt"):
		chemin = os.path.join("cartes", nomFichier)
		nomCarte = nomFichier[:-3].lower()
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
print()
carte = cartes[0]
print("La carte choisi est {}".format(carte.nom))
print("Affichage carte: {}".format(carte))

# On cherche la position du robot dans la carte
robot = carte.rechercheRobot()

#Instanciation du labyrinthe
labyrinthe = Labyrinthe(robot, "")
labyrinthe.setGrille(carte)

# Affichage de la carte
labyrinthe.afficheCarte()
labyrinthe.afficheRobotPosition()

# Test déplacement Robot
labyrinthe.deplacementRobot(5,8)
labyrinthe.afficheCarte()

# Si il y a une partie sauvegardée, on l'affiche, à compléter

# ... Complétez le programme ...
