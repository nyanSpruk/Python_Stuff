# Izracun faklutete

def fakRek(n):
    if(n == 1):
        return 1
    return n * fak(n - 1)

def fak(n):
    f = 1
    for i in range(2, n+1):
        f *= i
    return f

# Or shorter

def fakRekShort(n):
    return n * fak(n-1) if n > 1 else 1