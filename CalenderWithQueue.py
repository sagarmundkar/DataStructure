from week2.Calender import Calendar
from week2.Queue import Queue
import numpy

class CalendarWithQueue:
    def __init__(self):

        self.queue = Queue()

    def display(self, month, year):

        calendar = Calendar()
        print("------------", month, year, "---------------")
        for i in calendar.week:
            print(i, end="    ")
        for i in range(self.queue.size()):
            temp = self.queue.dequeue()
            if i % 7 == 0:
                print()
            if int(temp) == 0:
                print(end="     ")
            elif int(temp) < 10:
                print(temp, end="    ")
            else:
                print(temp, end="   ")

    def calendar_with_queue(self, month, year):

        calendar = Calendar()
        arr = calendar.initial(month, year)
        arr1 = numpy.array(arr).reshape(6, 7)
        for i in range(6):
            for j in range(7):
                self.queue.enqueue(arr1[i][j])
        return self.queue


if __name__ == '__main__':

    calendar_with_queue = CalendarWithQueue()
    try:
        month = int(input("Enter a month : "))
        if month / 10 > 1.2:
            raise ValueError
    except ValueError:
        print("Month input is invalid.")
    else:
        year = int(input("Enter a year : "))
        calendar_with_queue.calendar_with_queue(month, year)
        calendar_with_queue.display(month, year)
