# Nazwy piosenek w pliku sa randomowe
f = open("piosenkiBiebera.txt", "r")

linie = f.readlines()
liczbaLinii = len(linie)
print("liczba linii")
print(liczbaLinii)

lines = linie
# Sposob 1
linesSorted = sorted(lines, key=len, reverse=True)
print("wynik sposobu 1")
print(linesSorted[0])

# Sposob 2
linesMax = max(lines, key=len)
print("wynik sposobu 2")
print(linesMax)
