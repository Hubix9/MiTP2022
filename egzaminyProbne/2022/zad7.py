# 7 Justinek 5 Justinek 5 Bieber

# ostatnie i = 4
# ostatnie j = Bieber

for i in range(1994, 3, -1):
    for j in ['Justinek', 'Bieber']:
        if i < len(j) and i % 2: # i % 2 oznacza i nie podzielne przez 2, np. dla 8 reszta z dzielenia wyniesie 0, 0 ma wartosc logiczna Fałsz wiec blok If nie zostanie wykonany
            print(i, j, end=" ")
