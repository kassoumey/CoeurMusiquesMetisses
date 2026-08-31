@echo off
setlocal
cd /d "%~dp0\.."

echo ==========================================
echo   CoeurMusiquesMetisses - Atelier
echo   Installation Windows
echo ==========================================
echo.

where py >nul 2>nul
if %errorlevel%==0 (
    set "PY=py"
    goto python_ok
)

where python >nul 2>nul
if %errorlevel%==0 (
    set "PY=python"
    goto python_ok
)

echo Python 3 n'est pas installe.
echo Installez Python 3 puis relancez ce fichier.
echo https://www.python.org/downloads/windows/
pause
exit /b 1

:python_ok
%PY% --version
echo.
echo Installation de wavesynth et MIDIUtil...
%PY% -m pip install wavesynth MIDIUtil

if errorlevel 1 (
    echo.
    echo L'installation a rencontre un probleme.
    pause
    exit /b 1
)

echo.
echo Installation terminee.
echo Test de l'atelier :
%PY% atelier\test_installation.py
echo.
pause
