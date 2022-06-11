# Nie rozumiem dokladnie opisu zadania, wywnioskowalem ze trzeba stworzyc ascii arta "zero" z liter wybranego wersu
# Jednak nie jestem przekonany czy faktycznie taki jest cel zadania

class Wiersz:
    def __init__(self):
        self.wersy = ("Coś ty Atenom zrobił, Sokratesie",
                      "Że ci ze złota statuę lud niesie",
                      "Otruwszy pierwej?")
        self.slowa = self.wersy[0].split()

    def __str__(self):
        asciiArt = [[1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0],
                    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
                    [0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1],
                    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1],
                    [1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0]]

        wordPointer = 0
        letters = "".join(self.slowa)
        outStr = ""
        for y in range(len(asciiArt)):
            outXStr = ""
            for x in range(len(asciiArt[0])):
                if asciiArt[y][x] == 1:
                    outXStr += letters[wordPointer]
                    wordPointer += 1
                    if wordPointer == len(letters):
                        wordPointer = 0
                else:
                    outXStr += " "
            outStr += outXStr + "\n"
        return outStr


moj_wiersz = Wiersz()
print(moj_wiersz)
