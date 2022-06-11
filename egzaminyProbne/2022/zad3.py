from collections import Counter

songs = ["Baby", "Somebody to Love", "Never Let You Go",
"That Should Be Me", "Right Here"]

sortedSongs = sorted(songs, reverse=True) #Domyslnie python sortuje stringi alfabetycznie, odwracamy wiec sortowanie za pomoca parametru reverse
for song in sortedSongs:
    print(song)

#Tworze string zawierajacy wszystie slowa uzyte w nazwach piosenek
songsJoined = " ".join(songs) #String na ktorym zostaje wywolany join zostaje uzyty jako separator
songsJoined = songsJoined.lower() # caly string bedzie zapisany malymi literami
wordList = songsJoined.split(" ") # Dziele string na liste slow
wordCounter = Counter(wordList) #Uzywam klasy Counter do policzenia wystapien slow
print(dict(wordCounter.items()))

