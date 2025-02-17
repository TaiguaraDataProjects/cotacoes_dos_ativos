import importlib.util
import subprocess
import sys


class PrepareEnv:

    def prepare_lib(self, package_name):
        # Verifica se o pacote está instalado
        if importlib.util.find_spec(package_name) is None:
            print(f"Instalando {package_name}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name, "--upgrade", "--no-cache-dir"])
        else:
            print(f"{package_name} já está instalado!")
