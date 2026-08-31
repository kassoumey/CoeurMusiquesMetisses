#!/usr/bin/env bash
set -e
cd "$(dirname "$0")/.."

if command -v python3 >/dev/null 2>&1; then
    PYTHON=python3
elif command -v python >/dev/null 2>&1; then
    PYTHON=python
else
    echo "Python 3 n'est pas installé."
    exit 1
fi

echo "Python trouvé :"
"$PYTHON" --version
echo
echo "Installation de wavesynth et MIDIUtil..."
"$PYTHON" -m pip install wavesynth MIDIUtil --break-system-packages
echo
echo "Installation terminée."
echo "Test de l'atelier :"
"$PYTHON" atelier/test_installation.py
