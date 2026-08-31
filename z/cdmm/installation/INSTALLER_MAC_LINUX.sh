#!/usr/bin/env bash
set -e
cd "$(dirname "$0")/.."
if command -v python3 >/dev/null 2>&1; then PYTHON=python3
elif command -v python >/dev/null 2>&1; then PYTHON=python
else
 echo "Python 3 n'est pas installé."
 exit 1
fi
"$PYTHON" --version
[ -x .venv/bin/python ] || "$PYTHON" -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python atelier/test_installation.py
