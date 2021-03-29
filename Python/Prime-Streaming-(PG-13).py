from timeit import timeit

class Primes:
    @staticmethod
    def stream():
        yield 2
        primes = []
        current_number = 3
        while True:
            prime = True
            for p in primes:
                if p**2 > current_number:
                    break
                if current_number % p == 0:
                    prime = False
                    break
            if prime:
                primes.append(current_number)
                yield current_number
            current_number += 2

def run():
    stream = Primes.stream()

    for i in range(1_000_000): next(stream)

if __name__ == "__main__":
    print("Starting")
    time = timeit(stmt = run, number = 1)
    print(time)
