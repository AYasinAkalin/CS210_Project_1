# definition.py
# from pathlib import Path


def salutation():
    print("Hello")


def init():
    from pathlib import Path
    import os

    salutation()

    # DIR_SRC points to project directory which is CS210_Project_1/src
    # and can be reached from definitions.DIR_SRC after
    # running definitions.init() just once
    global DIR_SRC
    DIR_SRC = Path(__file__).parent

    global DIR_DATA
    DIR_DATA = DIR_SRC / 'data'

    # Changes active directory to project directory
    os.chdir(DIR_SRC)
