def read_from_file(filename):
    try:
        f = open(filename, 'r+')
    except IOError:
        print(filename, " not found.")
    else:
        j = ""
        for i in f:
            j = i + j
        word = j.strip().split(" ")
        return word


def write_to_file(filename, ls):
    try:
        f = open(filename, 'w')
    except IOError:
        print(filename, " not found.")
    else:
        size = ls.size()
        for i in range(size):
            f.write(ls.poll_first() + " ")


def append(filename, ls):
    f = open(filename, 'a')
    size = ls.size()
    for i in range(size):
        f.write(ls.poll_first() + " ")