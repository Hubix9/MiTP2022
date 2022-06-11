# pierwsza pentla wykona sie tylko dwa razy, 1 -> 4 x-> 7 (7 jest wieksze od 6)
# kod wypisze: 1 Justin 4 Justin 4 Bieberin
# Rozna kolejnosc wypisania zalezy od tego ze zbiory w pythonie sa nieupozadkowane

for i in range(1, 6, 3):
    for j in {'Just', 'Bieber'}:
        if i > len(j) - 4:
            print(i, j, end="in ")


