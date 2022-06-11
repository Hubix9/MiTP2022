# points == 0, to nie przypisanie wartosci, poprawnie bedzie points = 0
# Brak dwukropka po "if guess in associations[word]"
# brak przecinka w princie w ostatniej linii

# Dzialajacy kod
associations = {'zwierze': ['pies','kot','chomik'],
'owoc': ['jablko','gruszka','pomarańcza'],
'roslina': ['kaktus','storczyk','drzewo']
}
points = 0
for word in associations:
    guess = input('Co ci sie kojarzy z {}? '.format(word))
    if guess in associations[word]:
        points += 1
print("Masz punktów:", points)
