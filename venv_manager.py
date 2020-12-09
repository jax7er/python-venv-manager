from itertools import repeat
from os.path import getsize
from pathlib import Path
from subprocess import call
from sys import argv

ENV_PATH = Path("./env")
SCRIPTS_PATH = ENV_PATH / "Scripts"
PYTHON_PATH = SCRIPTS_PATH / "python.exe"
PIP_PATH = SCRIPTS_PATH / "pip.exe"

MAIN_PACKAGES, MAIN_LABELS = zip(
    ("wheel", "common package installation format"),
    ("flake8", "static code analysis, Python 3.8 supported"),
    ("rope", "code refactoring"),
)

SCIENCE_PACKAGES, SCIENCE_LABELS = zip(
    ("numpy", "numerical processing + C-style arrays -> numpy.array()"),
    ("pandas", "data manipulation + CSV file support -> pandas.read_csv()"),
    ("xlrd", "Excel file support -> pandas.read_excel()"),
    ("scipy", "signal processing + MAT file support -> scipy.io.loadmat()"),
    ("matplotlib", "plotting -> matplotlib.pyplot"),
    ("nptdms", "TDMS file support -> nptdms.TdmsFile()"),
    ("ipykernel", "IPython, variable explorer"),
    ("debugpy", "IPython debugging"),
)


def paragraph(s = "", *args, **kwargs):
    return print("\n" + s, *args, **kwargs)


def pip_install(names: str, label: str = None):
    if label:
        print(f"{names} ({label})")

    call(f"{PIP_PATH} install --upgrade --quiet {names}".split()) 
    

def upgrade():
    paragraph("Upgrading pip...")
    call(f"{PYTHON_PATH} -m pip install --upgrade --quiet pip".split())


def create():
    paragraph(f"Creating environment in {ENV_PATH}...")
    call(f"python -m venv {ENV_PATH}".split())

    upgrade()

    paragraph("Installing main packages...")
    for package, label in zip(MAIN_PACKAGES, MAIN_LABELS):
        pip_install(package, label)


def science():
    paragraph("Installing scientific packages...")
    for package, label in zip(SCIENCE_PACKAGES, SCIENCE_LABELS):
        pip_install(package, label)


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
        paragraph(f"Python virtual environment manager")

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
        
        paragraph("Calculating size...")
        total_size_B = sum(map(getsize, ENV_PATH.glob("**/*.*")))
        print(f"{total_size_B / 2**20:.1f} MiB in {ENV_PATH}")
    
    input("Press Enter to finish")
