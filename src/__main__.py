import subprocess as sp  # subprocess.run() requires Python 3.5 or higher.
import definitions


def init():
    import utility
    definitions.init()

    response = sp.run("sh sh/runProject.sh",
                      shell=True)
    utility.checkResponse(response,
                          "Project Script",
                          verbose=True)
    if utility.getConsent("Do you want to open Jupyter notebook? Y/N\t"):
        print("Jupyter notebook will be opened after countdown.")
        utility.countdown(5)
        response = sp.run("sh sh/openJupyter.sh",
                          shell=True)
        if not utility.checkResponse(response,
                                     'Jupyter',
                                     verbose=True):
            print("Program did not work correctly.")


init()
