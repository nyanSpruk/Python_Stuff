# Izracun n-tega Fibonaccijega stevila

def fibonacci(n):
    a = b = 1
    for i in range(n):
        a, b = b, a+b
    return a