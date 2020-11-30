from datetime import datetime
from itertools import repeat
from os.path import basename, getsize
from pathlib import Path
from subprocess import call
from sys import argv

VERSION = "1.0"
ENV_PATH = Path("./env")
SCRIPTS_PATH = ENV_PATH / "Scripts"
PYTHON_PATH = SCRIPTS_PATH / "python.exe"
PIP_PATH = SCRIPTS_PATH / "pip.exe"


def paragraph(s = "", *args, **kwargs):
    return print("\n" + s, *args, **kwargs)


def pip_install(name: str, label: str = None):
    if label:
        print(f"{name} ({label})")

    call(f"{PIP_PATH} install --upgrade --quiet {name}".split()) 
    

def upgrade():
    paragraph("Upgrading pip...")
    call(f"{PYTHON_PATH} -m pip install --upgrade --quiet pip".split())


def create():
    paragraph(f"Creating environment in {ENV_PATH}...")
    call(f"python -m venv {ENV_PATH}".split())

    upgrade()

    paragraph("Installing main packages...")
    pip_install("wheel", "packages")
    pip_install("pylint", "static code analysis")
    pip_install("rope", "refactoring")


def science():
    paragraph("Installing scientific packages...")
    pip_install("ipykernel", "variable explorer")
    pip_install("numpy", "fast arrays")
    pip_install("pandas", "data manipulation")
    pip_install("scipy", "signal processing")
    pip_install("matplotlib", "plotting")


def install():
    paragraph("Install custom packages, enter no name to skip")
    for names in (input(x).strip() for x in repeat("Package name(s): ")):
        if names:
            pip_install(names, "custom")
        else:
            break


if __name__ == "__main__":
    if any(x in argv for x in "-h --help".split()):
        with open("README.md") as readme_f:
            print(readme_f.read().replace("\n```", ""))
    else:
        paragraph(f"Python virtual environment manager, v{VERSION}")

        if len(argv) == 1:
            paragraph("Running all operations")
            create()
            science()
            install()
        else:
            if any(x in argv for x in "-c --create".split()):
                create()  
            
            if any(x in argv for x in "-u --upgrade".split()):
                upgrade()
            
            if any(x in argv for x in "-s --science".split()):
                science()      
            
            if any(x in argv for x in "-i --install".split()):
                install()
        
        total_size_B = sum(map(getsize, ENV_PATH.glob("**/*.*")))
        paragraph(f"{total_size_B / 2**20:.1f} MiB in {ENV_PATH}")
    
    input("Press Enter to finish")
