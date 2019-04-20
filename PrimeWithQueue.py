from week1.Algorithm.utility import util_class
from week1.Algorithm.utility.util_class import get_prime_number, get_anagram
from week2.Queue import Queue


class PrimeAnagramWithQueue:
    def __init__(self):
        self.queue = Queue()

    def prime_anagram_with_queue(self, rng):

        prime_number = get_prime_number(rng)
        anagram_number = get_anagram(prime_number)
        for i in anagram_number:
            self.queue.enqueue(i)
        for i in range(self.queue.size()):
            print(self.queue.dequeue(), end=" ")


if __name__ == '__main__':
    obj = PrimeAnagramWithQueue()
    rng = int(input("Enter range : "))
    obj.prime_anagram_with_queue(rng)
