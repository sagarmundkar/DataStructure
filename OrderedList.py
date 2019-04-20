from week2 import IO
from week2.LinkedList import LinkedList


class OrderedList:

    def __init__(self):

        self.list = LinkedList()

    def orderedList(self):
        number = IO.read_from_file("number.txt")
        for j in number:
            self.list.add(j)
        self.list.display()
        n = input('\nEnter number :').strip()
        if self.list.search(n):
            self.list.remove(n)
            print("Removed")
        else:
            self.list.add(n)
            print("Added")
        self.list.display()
        IO.write_to_file("number.txt", self.list)


if __name__ == '__main__':

    obj = OrderedList()
    obj.orderedList()
