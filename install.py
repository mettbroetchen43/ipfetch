# This script is meant to be an installer for dependencies. 

import subprocess
import importlib

def install_dependency(package):
    try:
        importlib.import_module(package)
    except ImportError:
        subprocess.run(["pip", "install", package])

# Lesen der requirements.txt und Installieren der Abhängigkeiten
with open("requirements.txt") as f:
    dependencies = f.read().splitlines()

for dependency in dependencies:
    install_dependency(dependency)
