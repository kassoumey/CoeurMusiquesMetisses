"""Interface simplifiée de l'atelier."""
# Module python formation atelier coeur des musiques metisses
# Simplifie la programmation
import random
import turtle
import wavesynth
from midiutil import MIDIFile

couleurs = [
    "red", "blue", "green", "orange",
    "purple", "cyan", "magenta", "brown"
]
def nouvelle_couleur():
    t.color(random.choice(couleurs))

# Dessin

t = turtle.Turtle()
t.speed(3)


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


def attendre()
    nouvelle_couleur()
    turtle.done()
    
    
DO, RE, MI, FA, SOL, LA, SI = 60, 62, 64, 65, 67, 69, 71

def creer_musique(tempo=100):
    m = MIDIFile(1)
    m.addTempo(0, 0, tempo)
    return m

def joue(musique, hauteur, debut, duree=1, volume=100):
    musique.addNote(0, 0, hauteur, debut, duree, volume)

def enregistre(musique, nom="ma_musique.mid"):
    with open(nom, "wb") as f:
        musique.writeFile(f)
    print("Fichier créé :", nom)

def do(): return DO
def re(): return RE
def mi(): return MI
def fa(): return FA
def sol(): return SOL
def la(): return LA
def si(): return SI
