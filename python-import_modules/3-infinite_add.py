#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    len_args = len(sys.argv)
    result = 0

    if len_args == 1:
        print("0")
    else:
        for i in range(1, len_args):
            result = result + int(sys.argv[i])

    print(result)
