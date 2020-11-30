Python virtual environment manager

Creates/modifies a virtual environment with the main packages needed to perform numerical operations, data manipulation, signal processing, and plotting. Also installs the IPython kernel so the environment can be used in Interactive mode in VSCode with the variable explorer etc. 

Author: Jack Mehmet
Date: 2020-11-30

## Command line options

```
  -c --create  : Create new virtual environment
  -u --upgrade : Upgrade pip (included in --create)
  -s --science : Install scientific packages
  -i --install : Install custom packages  
  no options   : Same as including all options
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