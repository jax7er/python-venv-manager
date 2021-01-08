# Python virtual environment manager

- Author: Jack Mehmet
- Date: 2021-01-08

Creates/modifies a virtual environment. Can auto-install the main packages needed to perform numerical operations, data manipulation, signal processing, and plotting. Also installs the IPython kernel so the environment can be used in Interactive mode in VSCode with the variable explorer etc. 

## Command line help

```
usage: venv_manager.py [-h] [-c] [-u] [-s] [-i]

Python virtual environment manager, no options is the same as all options

optional arguments:
  -h, --help     show this help message and exit
  -c, --create   Create new environment, upgrade pip, and install main packages
  -u, --upgrade  Upgrade pip
  -s, --science  Install scientific packages
  -i, --install  Install custom packages

main installs:
        pylint: static code analysis
        rope: refactoring
        wheel: packages
--science installs:
        attrs: data class support
        debugpy: IPython debugging
        ipykernel: interactive, variable explorer
        matplotlib: plotting
        nptdms: TDMS file support
        numpy: fast arrays
        pandas: data manipulation
        scipy: signal processing
  ```

## Example usage

Create new virtual environment, upgrade pip, install scientific packages, and install custom packages:

```
  python venv_manager.py
```

Upgrade pip and install custom packages:

```
  python venv_manager.py -u -i
```