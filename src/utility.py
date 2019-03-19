# utility.py
import subprocess as sp  # subprocess.run() requires Python 3.5 or higher.


def checkResponse(response, command_name='required package(s)', verbose=False):
    '''
    Input:
        response is a subprocess.CompletedProcess type
        command_name is a string and used to call command by its name
    '''
    if response.returncode is 0:
        if verbose:
            print(command_name, "run correctly.")
        return True
    elif response.returncode is 1:
        print("ERROR CODE: 1")
        if verbose:
            print(command_name, "encountered an error with a generic code.")
            print("Read above messages if any in the terminal screen to",
                  "get more info.")
        return False
    elif response.returncode is 126:
        print("ERROR CODE: 126")
        if verbose:
            print("Command invoked. Probably a permission error.")
        return False
    elif response.returncode is 127:
        print("ERROR CODE: 127")
        if verbose:
            print(command_name, "is not installed on this system or could not",
                  "found in your PATH.")
        if getConsent('Do you want to install ' + command_name + ' ? Y/N\t'):
            if verbose:
                print('Installing', command_name)
            flag = installRequirements()  # flag will be True on success
            if flag:
                return rerun(command=response.args)  # returns True on success
        return False
    else:
        print("echo Something else happened.")
        return False


def getConsent(message='', trial=1):
    acceptedAnswers = {'Y': True, 'N': False}
    reply_ORG = input(message)
    reply = reply_ORG.capitalize().strip()
    if reply in acceptedAnswers.keys():
        return acceptedAnswers[reply]
    elif trial < 3:
        print("Unrecognized reply:", reply_ORG)
        if getConsent(message, trial=trial+1):
            return True
        else:
            sp.run('exit 0', shell=True)
    else:
        return False


def installRequirements():
    response = sp.run("sh sh/installRequirements.sh", shell=True)
    return checkResponse(response, "requirements installation", verbose=True)


def rerun(command):
    response = sp.run(command, shell=True)
    return checkResponse(response, verbose=False)
