"""1. Feladat
Készíts egy programot, amely a felhasználótól bekér egy egész számot, majd megvizsgálja, hogy a megadott szám
- pozitív páros vagy
- negatív páratlan.
Az eredményről tájékoztatja a felhasználót.
"""

beker = int(input('Adj meg egy számot: \t'))
if beker %2 == 0:
    if beker > 0:
        print('Az általad megadott szám: pozitív páros.')
if beker %2 != 0:
    if beker < 0:
        print('Az általad megadott szám: negatív páratlan.')