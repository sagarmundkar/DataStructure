from week2.LinkedList import LinkedList


class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def push(self, obj):
        self.stack.add(obj)

    def pop(self):
        return self.stack.poll_last()

    def peak(self):
        return self.stack.get_last()

    def size(self):
        return self.stack.size()

    def isEmpty(self):
        return self.stack.is_empty()
