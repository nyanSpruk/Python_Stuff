# 'pass' ne nardi nicesar.

# Pogojni stvaki
# if izgleda:

# if a > 12 or b == 42:
#     f()
# elif a < 0 or b == 2:
#     g()
# elif a > 10:
#     h()
# else:
#     j()

# Oklepaji niso potrebni, (pri prioriteti seveda so)

# Zanka while:
# i = 1
# while i <= 10:
#     print(i)
#     i += 1


# Zanka for, se obnasa kot foreach
# >>> s = ["Miran", "Miha", "Mitja"]
# >>> for e in s:
# ...  print(e)
# ...
# Miran
# Miha
# Mitja
# >>> for e in "Miran":
# ...  print(e, ord(e))
# ...
# M 77
# i 105
# r 114
# a 97
# n 110

# Za zanko s stevcem
# for i in range(10): Ce zelimo od 0 do n-1 , lahko spodnjo mejo spustimo
#     ...

# for i in range(1, 11):
#     print(i)

# for i in range(10, 0, -1):
#     print(i)

# Cez array je dva nacina (first is worse)
# for i in range(len(s)):
#     print(s[i])
# drugi
# for e in s:
#     print(e)

# Zanka zna tudi razpakirati
# >>> for a, b in [(5, 2), (1, 4), (3, 7)]:
# ...     print(a+b)
# ...
# 7
# 5
# 10

# Tole je uporabno ce zelimo elemeent in njegov indeks. Funkcija 'enumerate'
# Ni cisto res, ampak bomo kasnej izvedeli
# >>> enumerate([5, 42, 6, 9, -3, 12])
# [(0, 5), (1, 42), (2, 6), (3, 9), (4, -3), (5, 12)]


# In tako vzemimo, recimo, programerja, ki mora poiskati indeks največjega
# elementa na seznamu s. Storiti mu je tole:
# naj_i = naj_e = -1
# for i, e in enumerate(s):
# if i < 0 or naj_e < e:
# naj_i, naj_e = i, e
# V zanki bo e element seznama, i pa njegov indeks. Klasična alternativa je
# naj_i = naj_e = -1
# for i in range(len(s)):
# if i < 0 or naj_e < s[i]:
# naj_i, naj_e = i, s[i]
# kar je dolgočasno in ničkaj Pythonovsko, ali
# naj = None
# for ie in enumerate(s):
# if naj is None or naj[1] < ie[1]:
# naj = ie

# Funkcija enumerate ne sprejema le seznamov, temveč vse, prek česar bi bilo
# mogoče z zanko for. Tudi, recimo, nize. Če bi delala, kakor sem si zgoraj izmislil,
# da dela, bi z nizom naredila tole:
# >>> enumerate("Miran")
# [(0, "M"), (1, "i"), (2, "r"), (3, "a"), (4, "n")]

# Se ena podobna funkcija je 'zip'
# Spremeni dva seznama v seznam parov, ali n seznamov v seznam n-terk
# Rezultat je dolg toliko kot najkrajsi od elementov

# >>> zip("Miran", [5, 2, 78, 9, 2])
# [('M', 5), ('i', 2), ('r', 78), ('a', 9), ('n', 2)]
# >>> zip("Miran", "Benjamin", "Ana")
# [('M', 'B', 'A'), ('i', 'e', 'n'), ('r', 'n', 'a')]
# Tale primer je sicer spet izmišljen, vendar malo manj kot enumerate, saj je zip do
# različice 3.0 v resnici deloval tako.
# Funkciji  zip  in  enumerate  sicer  lahko  uporabljamo  v  različnih  okoliščinah,
# vendar ju drugje kot v zanki for malone nikoli ne srečamo.

# Prekinjanje zank
# Lahko uporabimo 'break' ali 'continue
# Za izjeme ko se break ne izvede pa poskrbi else

# vprašanje, ali je katero od prvih stotih Fibonaccijevih
# števil  deljivo s 1131, potešijo radovednost z naslednjim programom.
# a = b = 1
# for i in range(100):
#     if a % 1131 == 0:
#         print(a, "je deljiv s 1131")
#         break
#     a, b = b, a+b
# else:
#     print("Nobeno od prvih 100 Fibonaccijevih stevil"
#           "ni deljivo s 1131")

# Pazimo: else je poravnan s for in ne z if, saj tudi spada k for in ne k if!

# Go to
# Ukaz goto ni v pythonu

# Preprosta definicija funkcija
# Definiramo jo z 'def' nato sledi ime funkcije in imena argumentov v ().
# Python nima funkcij brez rezuktata. Vse funkcije vracajo rezultat.
# Funckija ki ne vrne nicesarvrne 'None'. vrnemo vrednost z 'return vrednost'
# Ce napisemo samo return se vrne None
# Funckija lahko vraca vec vrednosti

# def fibonacci(n):
#     a = b = 1
#     for i in range(n):
#         a, b = b, a + b
#     return a, a**2
# ...
# a, a2 = fibonacci(10) $

# Ce bi poklicali a = fbionacci(10), bi 'a' postal terka ki bi jo nato razpakirali,
# ali pa dostopali z indeksi
