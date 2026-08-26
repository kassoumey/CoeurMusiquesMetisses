# EXERCICE 2 : une boucle
from georges import *

melodie = [do(), re(), mi(), sol(), sol(), mi(), re(), do()]
musique = creer_musique(tempo=110)

for i, hauteur in enumerate(melodie):
    joue(musique, hauteur, i)

enregistre(musique, "exercice_2.mid")
