def main():
    a = popolno(28)
    print(a)


def popolno(n):
    vsota = 0
    for i in range(1, n):
        if n % i == 0:
            vsota += i
    return vsota == n


if __name__ == '__main__':
    main()
