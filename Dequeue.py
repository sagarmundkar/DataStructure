from week2.LinkedList import LinkedList


class DeQueue:
    def __init__(self):
        self.queue = LinkedList()

    def enqueue_from_rear(self, obj):
        self.queue.add(obj)

    def enqueue_from_front(self, obj):
        self.queue.add_first(obj)

    def dequeue_from_rear(self):
        return self.queue.poll_last()

    def dequeue_from_front(self):
        return self.queue.poll_first()

    def size(self):
        return self.queue.size()

    def is_empty(self):
        return self.queue.is_empty()
