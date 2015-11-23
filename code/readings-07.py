import sys
import numpy as np

def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]
    assert action in ['-n', '-m', '-x'], \
           'Action is not one of -n, -m, or -x: ' + action
    if len(filenames) == 0:
        process(sys.stdin, action)
    else:
        for f in filenames:
            process(f, action)

def process(filename, action):
    data = np.loadtxt(filename, delimiter=',')

    if action == '-n':
        values = np.min(data, axis=1)
    elif action == '-m':
        values = np.mean(data, axis=1)
    elif action == '-x':
        values = np.max(data, axis=1)

    for m in values:
        print m

main()
