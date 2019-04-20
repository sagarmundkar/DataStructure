
from week2.Stack import Stack


class Balancedparentheses:
    def __init__(self):
        self.stack = Stack()

    def balancedparentheses(self, string):
        for i in string:
            if i is '(':
                self.stack.push(i)
            elif i is ')' and self.stack.peak() is '(':
                self.stack.pop()
        if self.stack.size() is 0:
            return True
        else:
            return False


def main():
    obj = Balancedparentheses()
    string = input("Enter the Expression:")
    # (5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3)
    result = obj.balancedparentheses(string)
    print(result)


if __name__ == "__main__":
    main()
