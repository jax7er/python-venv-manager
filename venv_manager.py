from argparse import ArgumentParser, RawTextHelpFormatter
from datetime import datetime
from itertools import repeat
from os.path import getsize
from pathlib import Path
from subprocess import call
from sys import argv

DESCRIPTION = "Python virtual environment manager"
VERSION = "1.0"

ENV_PATH = Path("./env")
SCRIPTS_PATH = ENV_PATH / "Scripts"
PYTHON_PATH = SCRIPTS_PATH / "python.exe"
PIP_PATH = SCRIPTS_PATH / "pip.exe"

MAIN_NAMES, MAIN_LABELS = zip(
    ("wheel", "packages"),
    ("pylint", "static code analysis"),
    ("rope", "refactoring"),
)

SCIENCE_NAMES, SCIENCE_LABELS = zip(
    ("ipykernel", "interactive, variable explorer"),
    ("debugpy", "IPython debugging"),
    ("numpy", "fast arrays"),
    ("pandas", "data manipulation"),
    ("scipy", "signal processing"),
    ("matplotlib", "plotting"),
    ("nptdms", "TDMS file support"),
    ("attrs", "data class support"),
)


def parse_arguments():
    main_str = "\n\t".join(
        sorted(map(": ".join, zip(MAIN_NAMES, MAIN_LABELS)))
    )
    sci_str = "\n\t".join(
        sorted(map(": ".join, zip(SCIENCE_NAMES, SCIENCE_LABELS)))
    )
    parser = ArgumentParser(
        description=DESCRIPTION + ", no options is the same as all options",
        epilog=(
            f"main installs:\n\t{main_str}\n"
            f"--science installs:\n\t{sci_str}"
        ),
        formatter_class=RawTextHelpFormatter,
    )
    parser.add_argument(
        "-c", "--create", 
        action="store_true", dest="create", 
        help="Create new environment, upgrade pip, and install main packages"
    )
    parser.add_argument(
        "-u", "--upgrade", 
        action="store_true", dest="upgrade", 
        help="Upgrade pip"
    )
    parser.add_argument(
        "-s", "--science", 
        action="store_true", dest="science", 
        help="Install scientific packages"
    )
    parser.add_argument(
        "-i", "--install", 
        action="store_true", dest="install", 
        help="Install custom packages"
    )
    
    return parser.parse_args()


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
    for name, label in zip(MAIN_NAMES, MAIN_LABELS):
        pip_install(name, label)


def science():
    paragraph("Installing scientific packages...")
    for name, label in zip(SCIENCE_NAMES, SCIENCE_LABELS):
        pip_install(name, label)


def install():
    paragraph("Install custom packages, enter no name to finish")
    for names in (input(x).strip() for x in repeat("Package name(s): ")):
        if names:
            pip_install(names, "custom")
        else:
            break


if __name__ == "__main__":
    args = parse_arguments()

    paragraph(f"{DESCRIPTION}, v{VERSION}")

    if not any(vars(args).values()):
        paragraph("Running all operations")
        create()  # also executes upgrade()
        science()
        install()
    else:
        if args.create:
            if (
                not ENV_PATH.exists()
                or input(f"{ENV_PATH} already exists, overwrite? [y|N] ").strip().lower().startswith("y")
            ):
                create()
        elif not ENV_PATH.exists():
            create()

        if args.upgrade:
            upgrade()

        if args.science:
            science()

        if args.install:
            install()
    
    total_size_B = sum(map(getsize, ENV_PATH.glob("**/*.*")))
    paragraph(f"{total_size_B / 2**20:.1f} MiB in {ENV_PATH}")
    
    input("Press Enter to finish")
