# Stejemo od 0 logically.
# Intervali so [a,b)
# Torej 5 do 10 -> 5, 6, 7, 8, 9
# Imamo tudi negativne korake: 12 do 6 -> 12, 11, 10, 9, 8, 7
# Privzeta vrednost zacetka je 0 in privzeti korak je 1.

# >>> range(5, 12)
# [5, 6, 7, 8, 9, 10, 11]
# >>> range(5, 12) + range(12, 15)
# [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# >>> len(range(5, 12))
# 7
# >>> range(5, 12, 4)
# [5, 9]
# >>> range(12)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# >>> len(range(12))
# 12
# >>> range(12, 5, -1)
# [12, 11, 10, 9, 8, 7, 6]
# >>> range(12, 5, -4)
# [12, 8]
