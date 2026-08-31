from coly import *

musique = creer_musique(tempo=100)

# Octave 2 : do2 à si2
# Octave 3 : do3 à si3

do2 = 48
re2 = 50
mi2 = 52
fa2 = 53
sol2 = 55
la2 = 57
si2 = 59

do3 = 60
re3 = 62
mi3 = 64
fa3 = 65
sol3 = 67
la3 = 69
si3 = 71

# 1/2 soupir
temps = 0.5
croche = 0.5
noire = croche * 2
blanche = croche *4 

# do re re en croches
joue(musique, do3, temps, croche
joue(musique, re3, temps + 0.5, croche)
joue(musique, re3, temps + 1, croche)

# mi en blanche
joue(musique, mi3, temps + 1.5, blanche)

# re do en noires
joue(musique, re3, temps + 3.5, noire)
joue(musique, do3, temps + 4.5, noire)

# do noire pointée, do croche
joue(musique, do3, temps + 5.5, 1.5)
joue(musique, do3, temps + 7, 0.5)

# do2 la2 fa2 fa2 en croches
joue(musique, do2, temps + 7.5, 0.5)
joue(musique, la2, temps + 8, 0.5)
joue(musique, fa2, temps + 8.5, 0.5)
joue(musique, fa2, temps + 9, 0.5)

# mi2 noire, sol2 mi2 en croches
joue(musique, mi2, temps + 9.5, 1)
joue(musique, sol2, temps + 10.5, 0.5)
joue(musique, mi2, temps + 11, 0.5)

# re2 mi2 fa2 fa2 en croches
joue(musique, re2, temps + 11.5, 0.5)
joue(musique, mi2, temps + 12, 0.5)
joue(musique, fa2, temps + 12.5, 0.5)
joue(musique, fa2, temps + 13, 0.5)

# mi2 en blanche
joue(musique, mi2, temps + 13.5, 2)

enregistre(musique, "alpha")

