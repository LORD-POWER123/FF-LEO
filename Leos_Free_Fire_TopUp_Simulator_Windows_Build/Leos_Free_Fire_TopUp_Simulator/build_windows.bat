@echo off
title Build Leo's Top-Up Simulator
python -m pip install --upgrade pip
python -m pip install pyinstaller
pyinstaller --onefile --windowed --name LeosTopUpSimulator leos_topup_simulator.py
echo.
echo Build complete. Your EXE is in the dist folder.
pause
