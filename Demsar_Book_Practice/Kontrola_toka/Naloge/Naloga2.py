import math


def main():
    trojka(1, 50)


def trojka(minc, maxc):
    for c in range(minc, maxc + 1):
        for a in range(1, 1 + int(c//math.sqrt(2))):
            b = math.sqrt(c**2 - a**2)
            if(b % 1 < 1e-6):
                print(a, int(b), c)


if __name__ == '__main__':
    main()
