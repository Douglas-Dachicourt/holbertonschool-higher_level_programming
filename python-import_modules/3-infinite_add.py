#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    len_args = len(sys.argv)
    result = 0

    for i in range(1, len_args):
        if len_args == 1:
            print("0")
            break
        else:
            result = result + int(sys.argv[i])

    print(result)
