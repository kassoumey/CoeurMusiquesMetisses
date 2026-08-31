print("TEST DE L'ATELIER")
print("==================")
print()

ok = True

try:
    import wavesynth
    print("OK - wavesynth")
except ImportError as e:
    print("NON - wavesynth :", e)
    ok = False

try:
    from midiutil.MidiFile import MIDIFile
    print("OK - MIDIUtil")
except ImportError as e:
    print("NON - MIDIUtil :", e)
    ok = False

try:
    from georges import avance, gauche, droite, tourne
    print("OK - georges.py")
except Exception as e:
    print("NON - georges.py :", e)
    ok = False

print()
print("TOUT EST PRET." if ok else "INSTALLATION INCOMPLETE.")
