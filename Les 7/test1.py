def readAge(filename):
    try:
        infile = open(filename)
        strAge = infile.readline()
        age = int(strAge)
    except IOError:
        print("Input error")
    except ValueError:
        print("Value error inhoud")

readAge('filename')
