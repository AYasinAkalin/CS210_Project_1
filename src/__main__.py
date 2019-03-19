import subprocess as sp  # subprocess.run() requires Python 3.5 or higher.
import definitions


def init():
    import utility
    definitions.init()
    response = sp.run("sh sh/openJupyter.sh",
                      shell=True)
    if not utility.checkResponse(response, 'Jupyter', verbose=True):
        print("Program did not work correctly.")


init()
