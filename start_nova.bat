@echo off
cd /d "%~dp0"

REM Find main.py — it may be in this folder or a nested subfolder
if exist "main.py" (
    python main.py
    pause
    exit /b
)

for /d %%D in (*) do (
    if exist "%%D\main.py" (
        cd "%%D"
        python main.py
        pause
        exit /b
    )
)

echo Could not find main.py. Make sure the NOVA files are in the project folder.
pause
