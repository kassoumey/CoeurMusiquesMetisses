"""Interface simplifiée de l'atelier."""
from midiutil.MidiFile import MIDIFile

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
