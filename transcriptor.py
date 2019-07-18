import os
import sys


def load_file(filename):
    try:
        f = open(filename, "rw+")
        return f
    except:
        print("Error loading file: " + filename)
        return None


def main(file, outfilename):
    outfile = open(outfilename, "rw+")
    lines = file.readlines()
    i = j = 1
    while i < len(lines):
        if i % 3:
            if j % 2:
                outfile.write(lines[i])
                outfile.seek(-1, os.SEEK_CUR)
                outfile.write(" ")
            j += 1
        i += 1
    outfile.close()


########################################
args = sys.argv
f = load_file(args[1])

main(f, args[2])
