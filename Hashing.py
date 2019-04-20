from week2.IO import read_from_file, append
from week2.LinkedList import LinkedList


class Hashing:
    def __init__(self):

        self.list = []

    def display_hash(self):

        for i in range(11):
            if self.list[i].is_empty():
                continue
            print(i, " = ", end="")
            self.list[i].display()
            print()

    def get_number(self):

        try:
            n = int(input("Enter number : "))
            if not n/100:
                raise ValueError
        except ValueError:
            print("Error : Invalid input..")
        else:
            res = n % 11
            if self.list[res].search(str(n)):
                self.list[res].remove(str(n))
            else:
                self.list[res].sort(str(n))

    def hashing_num(self):
        for i in range(11):
            self.list.append(LinkedList())
        number = read_from_file("number.txt")
        for i in range(len(number)):
            res = int(number[i]) % 11
            self.list[res].sort(number[i])
            # print(number[i])
        self.display_hash()
        self.get_number()
        self.display_hash()

        try:
            f = open("number.txt", 'r+')
        except IOError:
            print("number.txt file not found.")
        else:
            f.truncate()
            for i in range(11):
                if self.list[i].is_empty():
                    continue
                append("number.txt", self.list[i])


if __name__ == '__main__':

    h = Hashing()
    h.hashing_num()