from math import gcd
import sys

def factorization(n):
    def get_factor(n):
        x_fixed = 2
        cycle_size = 2
        x = 2
        factor = 1

        while factor == 1:
            for count in range(cycle_size):
                if factor > 1: break
                x = (x * x + 1) % n
                factor = gcd(x - x_fixed, n)

            cycle_size *= 2
            x_fixed = x

        return factor

    p = get_factor(n)
    q = n // p
    return p, q

def read_numbers(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield int(line.strip())

def main():
    file_path = sys.argv[1]
    for number in read_numbers(file_path):
        p, q = factorization(number)
        print(f'{number}={p}*{q}')

if __name__ == "__main__":
    main()
