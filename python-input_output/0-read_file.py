# /usr/bin/python3

def read_file(filename=""):
    with open(filename) as fic:
        print(fic.read())
