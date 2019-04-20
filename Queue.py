from week2.LinkedList import LinkedList


class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def enqueue(self, obj):
        self.queue.add(obj)

    def dequeue(self):
        return self.queue.poll_first()

    def size(self):
        return self.queue.size()

    def isEmpty(self):
        return self.queue.is_empty()


if __name__ == '__main__':
    pass
