import sys
import numpy as np

def main():
    script = sys.argv[0]
    action = sys.argv[1]
    if action not in ['--min', '--mean', '--max']: # if no action given
        action = '--mean'    # set a default action, that being mean
        filenames = sys.argv[1:] # start the filenames one place earlier in the argv list
    else:
        filenames = sys.argv[2:]

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
