import sys

def abs2asc(abs_file, asc_output):
    f = open(abs_file)
    rows = int(f.readline().split()[0])
    cols = int(f.readline().split()[0])

    # Reading the junk line
    f.readline()

    numbers = f.read().split()

    #flags
    fl = numbers[0: rows * cols]

    #X coordinates
    x = numbers[rows * cols: rows * cols * 2]

    # Y coordinates
    y = numbers[rows * cols * 2: rows * cols * 3]

    # Z coordinates
    z = numbers[rows * cols * 3: rows * cols * 4]

    # Writing to asc file
    asc_file = file(asc_output, 'w')
    for i in xrange(len(fl)):
        # if it is a valid point
        if fl[i] == '1':
            asc_file.write('%s, %s, %s\n' % (x[i], y[i], z[i]))


def main():
    abs_file = sys.argv[1]
    asc_output = sys.argv[2]
    abs2asc(abs_file, asc_output)

if __name__ == '__main__':
    main()
