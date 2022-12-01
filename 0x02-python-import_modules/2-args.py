#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    l = len(argv)
    if l == 1:
        print("{} arguments.".format(l - 1))
    elif l == 2:
        print("{} argument:".format(l - 1))
        print("{}: {}".format(l - 1, argv[1]))
    else:
        print("{} arguments:".format(l - 1))
        i = 1
        for arg in argv[1:]:
            print("{}: {}".format(i, argv[i]))
            i += 1
