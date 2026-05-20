import os
import sys
import shutil
import zipfile
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

    # Rutas de archivos y carpetas
    game_exe = base_path / "unsteam_loader64.exe"
    zip_maps = base_path / "mapas.zip"
    flag_file = base_path / "mods-instalados.txt"
    
    # Ruta en AppData Local para los mapas personalizados
    local_appdata = os.environ.get("LOCALAPPDATA")
    if local_appdata:
        target_dir = Path(local_appdata) / "GolfIt" / "Saved" / "SaveGames" / "CustomMap"
        
        # Comprobar si los mods ya están marcados como instalados
        mods_ok = False
        if flag_file.exists():
            try:
                if flag_file.read_text(encoding="utf-8").strip() == "si":
                    mods_ok = True
            except Exception:
                pass

        if not mods_ok:
            # Si no están instalados o el archivo no es correcto, limpiamos CustomMap si existe
            if target_dir.exists():
                for item in target_dir.iterdir():
                    try:
                        if item.is_dir():
                            shutil.rmtree(item)
                        else:
                            item.unlink()
                    except Exception:
                        pass
            else:
                target_dir.mkdir(parents=True, exist_ok=True)

            # Descomprimir el contenido de mapas.zip en la carpeta de destino
            if zip_maps.exists():
                try:
                    with zipfile.ZipFile(zip_maps, 'r') as zip_ref:
                        zip_ref.extractall(target_dir)
                    # Crear el archivo de marca para no repetir el proceso
                    flag_file.write_text("si", encoding="utf-8")
                except Exception:
                    pass

    if game_exe.exists():
        try:
            # os.startfile inicia el programa y libera el script inmediatamente
            os.startfile(str(game_exe))
        except Exception:
            pass

if __name__ == "__main__":
    main()