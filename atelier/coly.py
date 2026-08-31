import wavesynth
from midiutil import MIDIFile
# -------------------------
# Musique MIDI
# -------------------------

DO, RE, MI, FA, SOL, LA, SI = 60, 62, 64, 65, 67, 69, 71


def creer_musique(tempo=100):
    musique = MIDIFile(1)
    musique.addTempo(0, 0, tempo)
    return musique


def enregistre(musique, nom="ma_musique.mid"):
    with open(nom, "wb") as fichier:
        musique.writeFile(fichier)
    print("Fichier MIDI créé :", nom)


def jouer(nom):
    wave = sa.WaveObject.from_wave_file(nom)
    wave.play().wait_done()

def joue(musique, hauteur, debut, duree=1, volume=100):
    musique.addNote(0, 0, hauteur, debut, duree, volume)


# def enregistre(musique, nom="ma_musique.mid"):
    # with open(nom, "wb") as fichier:
        # musique.writeFile(fichier)
    # print("Fichier créé :", nom)


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
