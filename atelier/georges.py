# Module python formation atelier Coeur Musiques Metisses
# Simplifie la programmation

import turtle
import random



# -------------------------
# Dessin
# -------------------------

t = turtle.Turtle()
t.speed(3)
t.penup()
t.goto(-200, 0)
t.pendown()
t.shape("turtle")
t.turtlesize(5, 5)

couleurs = [
    "red", "blue", "green", "orange",
    "purple", "cyan", "magenta", "brown"
]


def nouvelle_couleur():
    t.color(random.choice(couleurs))


def avance(distance):
    nouvelle_couleur()
    t.forward(distance)


def tourne(angle):
    nouvelle_couleur()
    t.left(angle)


def gauche():
    nouvelle_couleur()
    t.left(90)


def droite():
    nouvelle_couleur()
    t.right(90)


def leve_crayon():
    nouvelle_couleur()
    t.penup()


def baisse_crayon():
    nouvelle_couleur()
    t.pendown()


def attendre():
    turtle.done()


# -------------------------
# Musique MIDI
# -------------------------

DO, RE, MI, FA, SOL, LA, SI = 60, 62, 64, 65, 67, 69, 71


def creer_musique(tempo=100):
    musique = MIDIFile(1)
    musique.addTempo(0, 0, tempo)
    return musique


def joue(musique, hauteur, debut, duree=1, volume=100):
    musique.addNote(0, 0, hauteur, debut, duree, volume)


def enregistre(musique, nom="ma_musique.mid"):
    with open(nom, "wb") as fichier:
        musique.writeFile(fichier)
    print("Fichier créé :", nom)


def do():
    return DO


def re():
    return RE


def mi():
    return MI


def fa():
    return FA


def sol():
    return SOL


def la():
    return LA


def si():
    return SI
