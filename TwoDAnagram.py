from week1.Algorithm.utility.util_class import get_prime_number, is_anagram
import numpy

class TwoDAnagram:
    def __init__(self):

        self.arr = numpy.full((2, 395), 0)

    def two_d_anagram(self, rng):

        prime_number = get_prime_number(rng)
        b_value = True
        cnt = 0
        for i in range(len(prime_number)):
            for j in range(len(prime_number)):
                if i == j:
                    continue
                b_value = True
                if is_anagram(str(prime_number[i]), str(prime_number[j])):
                    self.arr[0][cnt] = prime_number[i]
                    # cnt += 1
                    # self.arr[0][cnt] = prime_number[j]
                    cnt += 1
                    b_value = False
                    break
            if b_value:
                self.arr[1][i] = prime_number[i]
        for x in range(2):
            for y in range(395):
                if self.arr[x][y] == 0:
                    continue
                print(int(self.arr[x][y]), end=" ")
            print()


if __name__ == '__main__':

    obj = TwoDAnagram()
    rng = int(input("Enter range : "))
    try:
        if rng > 1000:
            raise ValueError
    except ValueError:
        print("Range exceeded.")
    else:
        obj.two_d_anagram(rng)
