Clear.bat
cp main.py launcher_win.py
python -m PyInstaller --onefile --windowed --noconsole --icon=golfit.ico launcher_win.py
python -m PyInstaller --onefile --windowed --noconsole --icon=golfit.ico installer_updater.py
python -m PyInstaller --onefile --windowed --noconsole --name="GolfItLauncher" --icon=golfit.ico launch_game.py
echo 1.0.2 > version_win_launcher.txt