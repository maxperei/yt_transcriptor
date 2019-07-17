from optparse import OptionParser


def load_file(filename):
    try:
        f = open(filename, "w+")
        return f
    except:
        print("Error loading file: " + filename)
        return None


def main(file, outfilename):
    outfile = open(outfilename, "w+")
    for x in file.readlines():
        # todo catch pattern w/ regex
        outfile.write(x)
    outfile.close()


########################################
parser = OptionParser(usage="usage: %prog input_file output_file")
(args) = parser.parse_args()

(f) = load_file(args[0])

if len(args[1]) == 0:
    args[1] = args[0]

main(f, args[1])
