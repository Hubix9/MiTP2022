# listy itd...

slown = {}
slown["justin"] = "justin"
del slown["justin"]

lista = []
lista.append("justin")
lista.remove("justin")

# Krotki sa niemutowalne (nie da sie ich edytowac po utworzeniu)
# wiec na egzaminie zaznaczylbym ze modyfikacja krotki jest niemozliwa, jednak jesli chcemy koniecznie utworzyc krotke na podstawie poprzedniej krotki to
# jest to opisane ponizej
krotka = ()
krotka = ("justin", *krotka)
krotka = tuple(x for x in krotka if x != "justin")

zbior = set()
zbior.add("justin")
zbior.remove("justin")

print(slown)
print(lista)
print(krotka)
print(zbior)
