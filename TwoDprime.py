from week1.Algorithm.utility.util_class import get_prime_number


class TwoDPrime:
    def __init__(self):
        self.arr = numpy.full((2, 500), 0)

    def two_d_prime(self, rng):
        prime_number = get_prime_number(rng)

    if __name__ == '__main__':

        obj = TwoDPrime()
        rng = int(input("Enter range : "))
        try:
            if rng > 1000:
                raise ValueError
        except ValueError:
            print("Range exceeded.")
        else:
            obj.two_d_prime(rng)
