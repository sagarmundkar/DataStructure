from math import trunc


class Calendar:
    def __init__(self):
        self.arr = []
        self.week = ["S", "M", "T", "W", "Th", "F", "S"]
        self.month_days = [3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]

    def leap(self, year):
        # year = int(input("Enter the year:"))
        if year % 400 == 0 and year % 100 != 0 or year % 4 == 0:
            # print("Year is Leap year!")
            return True
        else:
            # print("Year is not leap year")
            return False

    def display(self, arr, month, year):

        print("------------", month, year, "---------------")
        for i in self.week:
            print(i, end="    ")
        for i in range(len(arr)):
            if i % 7 == 0:
                print()
            if arr[i] == 0:
                print(end="     ")
            elif arr[i] < 10:
                print(arr[i], end="    ")
            else:
                print(arr[i], end="   ")

    def initial(self, m, y):

        day_of_year = (y * 365 + trunc((y - 1) / 4) - trunc((y - 1) / 100) +
                       trunc((y - 1) / 400)) % 7
        month = self.month_days[m - 1] + 28
        for i in range(m - 1):
            day_of_year += self.month_days[i]
        if self.leap(y):
            if m == 2:
                month += 1
            day_of_year += 1
        day_of_year %= 7
        temp = 1
        for i in range(42):
            if day_of_year > 0:
                self.arr.append(0)
                day_of_year -= 1
                continue
            if temp <= month:
                self.arr.append(temp)
                temp += 1
                continue
            self.arr.append(0)
        return self.arr


if __name__ == "__main__":

    c = Calendar()

    try:
        month = int(input("Enter a month : "))
        if month / 10 > 1.2:
            raise ValueError
    except ValueError:
        print("Month input is invalid.")
    else:
        year = int(input("Enter a year : "))
        arr = c.initial(month, year)
        c.display(arr, month, year)
