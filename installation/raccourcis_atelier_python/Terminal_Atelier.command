#!/bin/bash
# Ouvre une invite Python (Terminal) directement dans le
# dossier de l'atelier. Le dossier est cree automatiquement
# s'il n'existe pas encore.

DOSSIER="$HOME/Desktop/Atelier Python"
mkdir -p "$DOSSIER"
cd "$DOSSIER"

echo "=== Atelier Python : dossier de travail ==="
echo "$DOSSIER"
echo ""

python3
exec $SHELL
