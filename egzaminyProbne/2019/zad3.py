from collections import Counter
songs = {
2016: "Cold Water",
2019: "I Don't Care",
2017: "Friends",
2018: "2U"
}

#sortowanie
print(songs.items())

#key=Lambda w ponizszym wyrazeniu jest opcjonalne, domyslnie sortowanie i tak odbedzie sie po zerowym elemencie listy/krotki
for entry in sorted(songs.items(), key=lambda x: x[0]):
    print(entry[1])

#najdluzszy tytul
longestName = ""
for _, name in songs.items():
    if len(name) > len(longestName):
        longestName = name
print("Najdluzszy tytul opcja 1:", longestName)
#druga opcja na najdluzszy tytul
print("Najdluzszy tytul opcja 2:", max(songs.values(), key=len))


#najczestsza litera
# W obu metodach usuwam spacje oraz apostrof z racji ze zadanie dotyczy liter a nie wszystkich znakow

# Opcja 1
songNames = "".join(songs.values())
songNames = [x.lower() for x in songNames if x != " " and x != "'"]

countedLetters = Counter(songNames)
print(f"najczestsza litera 1: {max(countedLetters, key=countedLetters.get)}")

# Opcja 2
songNames = "".join(songs.values()).lower().replace(" ", "").replace("'", "")
countedLetters = Counter(songNames)
print(f"najczestsza litera 2: {max(countedLetters, key=countedLetters.get)}")

