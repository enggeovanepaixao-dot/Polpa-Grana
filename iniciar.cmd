@echo off
cd /d "%~dp0"
set "PG_PYTHON=%~dp0.venv\Scripts\python.exe"
if not exist "%PG_PYTHON%" set "PG_PYTHON=%USERPROFILE%\Music\POSTAGEM\poupa-grana\.venv\Scripts\python.exe"
if not exist "%PG_PYTHON%" (
 echo Ambiente Python nao encontrado. Abra a instalacao completa do Poupa Grana.
 pause
 exit /b 1
)
start "" http://127.0.0.1:5090/entrar/
"%PG_PYTHON%" scripts\abrir_local.py
pause
