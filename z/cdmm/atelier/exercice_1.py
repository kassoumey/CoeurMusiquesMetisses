# EXERCICE 1 : une mélodie
from georges import *

musique = creer_musique(tempo=100)

joue(musique, do(), 0)
joue(musique, re(), 1)
joue(musique, mi(), 2)
joue(musique, sol(), 3)
joue(musique, mi(), 4)
joue(musique, re(), 5)
joue(musique, do(), 6)

enregistre(musique, "exercice_1.mid")
