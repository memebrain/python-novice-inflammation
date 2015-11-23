import sys
import numpy as np

def main():
    script = sys.argv[0]
    if len(sys.argv) == 1: # no arguments, so print help message
        print 'Usage: python readings-08.py action filenames\n \
               action must be one of --min --mean --max\n \
               if filenames is blank, input is taken from stdin;\n \
               otherwise, each filename in the list of arguments is processed in turn'
        return

    action = sys.argv[1]
    filenames = sys.argv[2:]
    assert action in ['--min', '--mean', '--max'], \
           'Action is not one of --min, --mean, or --max: ' + action
    if len(filenames) == 0:
        process(sys.stdin, action)
    else:
        for f in filenames:
            process(f, action)

def process(filename, action):
    data = np.loadtxt(filename, delimiter=',')

    if action == '--min':
        values = np.min(data, axis=1)
    elif action == '--mean':
        values = np.mean(data, axis=1)
    elif action == '--max':
        values = np.max(data, axis=1)

    for m in values:
        print m

main()
