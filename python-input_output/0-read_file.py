# /usr/bin/python3

def read_file(filename=""):
    with open(filename) as fic:
        content = fic.read()
        print(content)
