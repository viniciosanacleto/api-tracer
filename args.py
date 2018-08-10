import sys

def solveArgs(args):
    treatedArgs = dict()
    for i in range(3, len(args)):
        if(args[i] == '-t'):
            treatedArgs['threads'] = int(args[i+1])
            i += 1
    return treatedArgs
