# Prirejanje =
# Ex: a, b = "xy"
#  a -> 'x'    b -> 'y'


t = (7, 12, "tine")
a, b, c = t

# lahko tudi

a, b, c = (7, 12, "tine")

# ali pa

a, b, c = 7, 12, "tine"


# Menjanje vrednosti spremenljivk
a, b = b, a

# Mogoce je razpakirati  tudi celotne strukture, s pomocjo oklepajev
t = 1, (2, 3)
a, (b, c) = t


# Matematicne operacije
# / vraca realna stevila
# // vraca integer stevila
# 1//2 -> 0
# 4.5//1.4 -> 3.0

# ** Pomeni potenciranje


# Logicne operatorje pisemo z besedam: or, and, not
# Ko nastopajo v logicnih izrazih poleg False, so neresnicni tudi 0, None, prazen niz, seznam, slovar... vse prazno
# Vse ostalo se steje za resnicno

# >>> True or False
# True
# >>> True and False
# False
# >>> 5 and False
# False
# >>> 5 and 12
# 12
# >>> 5 or 12
# 5
# >>> "Miran" or "Andrej"
# 'Miran'
# >>> 1 and 2 and 0 and 3 or 4 and 5 or 6
# 5
# >>> None or 0 or ""
# ''

# Ni nujno True ali False rezultat, ampak lahko je vrednost pri kateri se je racunanje koncalo
# Example:
# >>> ime = "Miran"
# >>> "Vaše spletno mesto je obiskal " + (ime or "Anonymous")
# 'Vaše spletno mesto je obiskal Miran'
# >>>
# >>> "Vaše spletno mesto je obiskal " + (ime or "Anonymous")
# 'Vaše spletno mesto je obiskal Anonymous'

# Instead of ternay  a ? b : c, imamo b if a else c

# Imamo tudi == in !=
# Primerjanja lahko nizamo
# >>> 1 < 2 < 3 < 4 != 5
# True
# >>> 1 < 2 < 3 < 4 != 5 < 4
# False


# Operatorji ~ | & ^ predsatvlajo negacijo, ali, in, eksluzivni ali na Bitih
# << >> pomilk v levo in v desno za doloceno stevilo bitov
