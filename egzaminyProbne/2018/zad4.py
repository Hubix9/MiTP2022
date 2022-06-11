from collections import Counter

fani = {1: "Michal C", 3: "Michal D", 2: "Szymon B", 4: "Bartek P"}
names = [x.split(" ")[0] for x in fani.values()]

for name in names:
    print(name)
namesCounter = Counter(names)

# Najpopularniejsze imie
print("najpopularniejsze imie")
print(max(namesCounter, key=namesCounter.get))

#druga opcja na najpopularniejsze imie
najpopularniejszeImie = ("", 0)
lista = list(namesCounter.items())

for element in lista:
    if element[1] > najpopularniejszeImie[1]:
        najpopularniejszeImie = element
print("wynik alternatywnego rozwiazania")
print(najpopularniejszeImie[0])

