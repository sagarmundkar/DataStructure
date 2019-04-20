from week2.Node import Node


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, obj):
        newNode = Node(obj)

        if self.head is None:
            self.head = newNode
        else:
            tempNode = self.head
            while tempNode.next is not None:
                tempNode = tempNode.next
            tempNode.next = newNode

    def display(self):
        tempNode = self.head
        while tempNode is not None:
            print(tempNode.object, end=" ")
            tempNode = tempNode.next

    def poll_first(self):
        tempNode = self.head
        if tempNode is None:
            return -1
        self.head = tempNode.next
        return tempNode.object

    def poll_last(self):
        tempNode = self.head
        previous = self.head
        if tempNode is None:
            return -1
        if tempNode.next is None:
            self.head = None
        while tempNode.next is not None:
            previous = tempNode
            tempNode = tempNode.next
        previous.next = None
        return tempNode.object

    def remove(self, obj):
        tempNode = self.head
        previous = self.head
        if tempNode.object == obj:
            self.head = tempNode.next
        else:
            while hash(tempNode.object) != hash(obj):
                previous = tempNode
                tempNode = tempNode.next
            previous.next = tempNode.next

    def size(self):
        tempNode = self.head
        cnt = 0
        while tempNode is not None:
            cnt += 1
            tempNode = tempNode.next
        return cnt

    def search(self, obj):
        tempNode = self.head
        while tempNode is not None:
            if hash(tempNode.object) == hash(obj):
                return True
            tempNode = tempNode.next
        return False

    def sort(self, obj):
        newNode = Node(obj)
        if self.head is None:
            self.head = newNode
        else:
            tempNode = self.head
            if tempNode.object > obj:
                newNode.next = tempNode
                self.head = newNode
            else:
                previous = self.head
                while tempNode is not None:
                    if tempNode.object > obj:
                        newNode.next = previous.next
                        previous.next = newNode
                        return
                    previous = tempNode
                    tempNode = tempNode.next
                previous.next = newNode

    def get_last(self):
        tempNode = self.head
        if tempNode is None:
            return -1
        while tempNode.next is not None:
            tempNode = tempNode.next
        return tempNode.object

    def is_empty(self):
        if self.size() is 0:
            return True
        else:
            False

    def add_first(self, obj):
        newNode = Node()
        newNode.object = obj
        newNode.next = self.head
        self.head = newNode

    def get_head(self):
        return self.head

    def get_by_index(self, index):
        tempNode = self.head
        # try:
        #     if self.size()<index:
        #         raise ValueError
        # except ValueError:
        #     print("Index not available.")
        #     return
        # else:
        for i in range(index):
            tempNode = tempNode.next
        return tempNode.object

    def delete_by_index(self, index):
        temp = self.head
        pre = temp
        if index == 0:
            self.head = temp.next
        while index > 0:
            pre = temp
            temp = temp.next
            index -= 1
        pre.next = temp.next