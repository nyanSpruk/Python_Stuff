# Izracun n-tega Fibonaccijega stevila

def fibonacci(n, a = 1, b = 1):
    for i in range(n):
        a, b = b, a+b
    return a

# print(fibonacci(10, 2, 6))

# for i in range(10):
#     print(fibonacci(i, "a", "t"))