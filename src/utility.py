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
                if getConsent('Do you want to rerun '
                              + command_name
                              + ' ? Y/N\t'):
                    # returns True on success
                    return rerun(command=response.args)
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


def countdown(seconds=None):
    import time

    while True:
        while not seconds or type(seconds) is not int:
            uin = input(">> ")
            try:
                seconds = abs(int(uin))
            except KeyboardInterrupt:
                break
            except:
                print("Not a number!")

        for second in reversed(range(seconds)):
            m, s = divmod(second, 60)
            h, m = divmod(m, 60)
            time_left = str(h).zfill(2) \
                + ":" + str(m).zfill(2) \
                + ":" + str(s).zfill(2)
            # '\r' helps to print over the same line
            print(time_left + "\r", end="")
            time.sleep(1)  # Pauses execution for 1 second so countdown works
        print()
        break
