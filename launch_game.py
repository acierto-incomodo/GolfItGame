import os
import sys
from pathlib import Path

def main():
    # Obtenemos la ruta del directorio donde está el ejecutable del lanzador
    # Esto asegura que encuentre la carpeta 'GolfIt' sin importar desde dónde se ejecute
    if getattr(sys, 'frozen', False):
        # Ruta cuando es un .exe compilado
        base_path = Path(sys.executable).parent
    else:
        # Ruta cuando se ejecuta como script .py
        base_path = Path(__file__).parent

    # Construimos la ruta al ejecutable objetivo
    game_exe = base_path / "GolfIt" / "Binaries" / "Win64" / "GolfIt-Win64-Shipping.exe"

    if game_exe.exists():
        try:
            # os.startfile inicia el programa y libera el script inmediatamente
            os.startfile(str(game_exe))
        except Exception:
            pass

if __name__ == "__main__":
    main()