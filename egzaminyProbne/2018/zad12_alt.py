# Interpretacja numer 2, "wybieramy" litery z wersu poprzez ich usunięcie, usuwamy litery które tworzą napis "zero"
# Nie jestem przekonany rowniez do tej interpretacji zadania

class Wiersz:
    def __init__(self):
        self.wersy = ("Coś ty Atenom zrobił, Sokratesie",
                      "Że ci ze złota statuę lud niesie",
                      "Otruwszy pierwej?")
        self.slowa = self.wersy[0].split()

    def __str__(self):
        print(self.slowa)
        slowa = "".join(self.slowa)
        for litera in "zero":
            slowa = slowa.replace(litera, "")
            print(litera)

        return slowa




moj_wiersz = Wiersz()
print(moj_wiersz)
