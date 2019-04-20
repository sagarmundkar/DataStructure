from week1.Algorithm.utility.util_class import get_prime_number, get_anagram
from week2.Stack import Stack


class PrimeWithStack:
    def __init__(self):

        self.stack = Stack()

    def prime_with_stack(self, rng):

        prime_number = get_prime_number(rng)
        anagram = get_anagram(prime_number)
        for i in anagram:
            self.stack.push(i)
        for i in range(self.stack.size()):
            print(self.stack.pop(), end=" ")


if __name__ == '__main__':

    obj = PrimeWithStack()
    rng = int(input("Enter range : "))
    obj.prime_with_stack(rng)
