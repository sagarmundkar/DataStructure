from week2 import IO
from week2.LinkedList import LinkedList


class UnOrderedList:

    def __init__(self):

        self.list = LinkedList()

    def unorderedList(self):
        word = IO.read_from_file("abc.txt")
        for j in word:
            self.list.add(j)
        self.list.display()
        w = input('\nEnter word :').strip()
        if self.list.search(w):
            self.list.remove(w)
            print("Removed")
        else:
            self.list.add(w)
            print("Added")
        self.list.display()
        IO.write_to_file("abc.txt", self.list)


if __name__ == '__main__':

    obj = UnOrderedList()
    obj.unorderedList()
