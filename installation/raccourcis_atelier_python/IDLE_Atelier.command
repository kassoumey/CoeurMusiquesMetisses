#!/bin/bash
# Ouvre IDLE directement dans le dossier de l'atelier.
# Le dossier est cree automatiquement s'il n'existe pas encore.

DOSSIER="$HOME/Desktop/Atelier Python"
mkdir -p "$DOSSIER"
cd "$DOSSIER"

/usr/bin/python3 -m idlelib &
