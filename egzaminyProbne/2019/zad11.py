# Klasa Bieber dziedziczy metody zawarte w klasie Singer
# mozemy to zaobserwowac w momencie tworzenia klasy Bieber ktora bedzie wymagac parametru zawartego w metodzie init klasy Singer
# Klasa Bibeber nadpisuje metode sing, w zwiazku z czym bedzie ona dzialac inaczej niz w klasie Singer

class Singer:
    def __init__(self, name):
        self.name = name

    def sing(self):
        print("Teraz spiewa", self.name)

    def dance(self):
        print("Teraz tanczy", self.name)


class Bieber(Singer):
    def sing(self):
        print(self.name, "If I was your boyfriend")


singer = Singer("123")
singer.sing()

bieber = Bieber("baby")
bieber.sing()
