@echo off
setlocal
cd /d "%~dp0\.."
echo === Atelier Coeur Musiques Metisses ===
where py >nul 2>nul
if %errorlevel%==0 (set "PY=py") else (set "PY=python")
%PY% --version >nul 2>nul
if errorlevel 1 (
 echo Python 3 n'est pas installe.
 echo Installez-le depuis https://www.python.org/downloads/windows/
 pause
 exit /b 1
)
if not exist ".venv\Scripts\python.exe" %PY% -m venv .venv
".venv\Scripts\python.exe" -m pip install -r requirements.txt
".venv\Scripts\python.exe" atelier\test_installation.py
pause
