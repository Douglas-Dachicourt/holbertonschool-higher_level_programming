#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    len_args = len(sys.argv)

    if len_args == 1:
        print("0 arguments")
    elif len_args == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(len_args - 1))
        for i in range(1, len_args):
            print("{}: {}".format(i, sys.argv[i]))
