from week2.Calender import Calendar
from week2.CalenderWithQueue import CalendarWithQueue
from week2.Stack import Stack

class CalendarWithStack:
    def __init__(self):

        self.stack1 = Stack()
        self.stack2 = Stack()

    def display(self, month, year):

        calendar = Calendar()
        print("------------", month, year, "---------------")
        for i in calendar.week:
            print(i, end="    ")
        for i in range(self.stack2.size()):
            temp = self.stack2.pop()
            if i % 7 == 0:
                print()
            if int(temp) == 0:
                print(end="     ")
            elif int(temp) < 10:
                print(temp, end="    ")
            else:
                print(temp, end="   ")

    def calendar_with_stack(self, month, year):

        queue = CalendarWithQueue()
        queue = queue.calendar_with_queue(month, year)
        for i in range(queue.size()):
            self.stack1.push(queue.dequeue())
        for i in range(self.stack1.size()):
            self.stack2.push(self.stack1.pop())


if __name__ == '__main__':

    calendar_with_stack = CalendarWithStack()
    try:
        month = int(input("Enter a month : "))
        if month / 10 > 1.2:
            raise ValueError
    except ValueError:
        print("Month input is invalid.")
    else:
        year = int(input("Enter a year : "))
        calendar_with_stack.calendar_with_stack(month, year)
        calendar_with_stack.display(month, year)





