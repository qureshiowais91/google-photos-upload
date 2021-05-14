from os import listdir
from os.path import isfile, join


def getFileNames(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles
