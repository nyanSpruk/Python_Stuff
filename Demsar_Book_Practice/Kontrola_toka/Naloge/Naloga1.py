def main():
    a = evklid(323, 291)
    print(a)


def evklid(a, b):
    while(b > 0):
        a, b = b, a % b
    return a


if __name__ == '__main__':
    main()
