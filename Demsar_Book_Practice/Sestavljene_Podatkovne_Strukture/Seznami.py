# Seznami lahko razlicne tipe v en senzam
# Indeksiranje [0] do [n-1]
# Lahko tudi idneksiramo od zadaj [-1] vrne zadnji element in [-2] predzadnji

# Slicing dobimo podseznam
# s[0:2] - vrne elemente 0, 1
# s[2:5] - vrne elemente 2, 3, 4

# Lahko tudi s[0:2] + s[2:5] bo zavzel elemente 0, 1, 2, 3, 4... kjer se 2 ne ponovi
# Lahko tudi s[2, -2] - seznam bo vse razen prvih in zadnjih dveh elementov
# s[:2] - prva dva elementa
# s[2:] - od drugega elementa.. vsi razen prvih dveh
# s[-2:] - sta zadnja dva elementa vse od -2-gega naprej
# s[:-2] - vsi razen zadnjih dveh - vse do -2-gega

# Lahko dodamo tudi korak s[0:5:2] elementi 0-4 in vsak drugi... 0 2 4
# Lahko je tudi negativen s[5::-1]

# Operacije
# s[4] = "Neki"
# del s[4] - delete
# Ce bi pobrisali element katerega indeks ne vemo
# s.remove("Neki")
# Dodajanje na konec s.append("Drugo")
# K seznamu lanko appendamo drug seznam z s.extend(seznam2)
# Lahko tudi z s += seznam2
# Zadnji in redko uporabljen nacin prirejanja je
# s[3:3] = ["Neki", "Element2"]
# S tem vstavimo element "Neki" na indeks 3, in "Element2" na 4
# ker rezina 3:3 je prazna, saj vsebuje vse elemente od 3 do 3 a brez tretjega.
# s[3:6] = ["Bla", "Bla2"] bo zamenjal element na indeksu 3 in 4, in element na indeksu 5 s praznino
# s[2:4] = [] lahko tudi in nastvimo te indekse na prazno. oz zbrisemo
# ekvivalentno del s[2:4]

# 'Neki' in s
# >>> True
# "Krneki" in s
# >>> False

# Metoda index pove na prvem indeksu ki se nahaja, count pa kolikokrat ga najdemo.
# count vrne 0 ce ni elementa, index pa vrne napako

# Dolzino dobimo z len(s)
# Metoda reverse obrne seznam
# s[::-1] tudi obrne seznam ampak sestavi nov seznam. medtem ko s.reverse() ga obrne na mestu
# MEtoda sort seznam uredi na mestu. Lahko ji damo key=value po katerem bo uredila seznam
# Drugace bo urejeno po velikosti od max to min
# >>> s = ["Ana", "Berta", "Cilka", "Danica", "Eva", "Frančiška"]
# >>> s.sort(key=len)
# >>> s
# ['Ana', 'Eva', 'Berta', 'Cilka', 'Danica', 'Frančiška']
# >>> s.sort()
# >>> s
# ['Ana', 'Berta', 'Cilka', 'Danica', 'Eva', 'Frančiška']

# Dva seznama je mogoce primerjati. Deluje leksiografsko, podobno kot primerjanje nizov
# To dela dokler ne naleti na par ki se razlikuje
# Drugace pa krajsi seznam vrne
# >>> [1, 2, 3, 5] < [1, 2, 4, 5]
# True
# >>> [1, 2, 3, 5] < [1, 2, 4]
# True
# >>> [1, 2, 3] < [1, 2, 3, 5]
# True
# >>> [1, 2, 3] < [1, 2, 3]
# False

# Se nekoliko nervarna rec. Seznam lahko mnozimo s stevilom
# >>> ["Ana", "Berta"] * 3
# ['Ana', 'Berta', 'Ana', 'Berta', 'Ana', 'Berta']

# >>> s = [[]]*5
# >>> s
# [[], [], [], [], []]
# >>> s[0].append(1)
# >>> s
# [[1], [1], [1], [1], [1]]

# Na prvi pogled smo sestavili seznam s 5 praznimi seznami. V resnici je seznam, ki 5x vsebuje isti seznam.
# "Pointer je 5x enak"

# Kako pravilno sestaviti seznam 5 praznih seznamov
# s = []
# for i in range(5):
#     s.append([])

# Resen python rpgoramer bi tako
# s = [[] for i in range(5)]
