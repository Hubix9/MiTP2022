from common.termscreen import Screen
from common.compositing import overlayImages
from common.ppmReader import Image
from common.game import Game
from random import shuffle
from time import sleep
import os.path as path


class LandOfDragons(Game):

    def __init__(self):
        super(LandOfDragons, self).__init__()
        self.screen = Screen(64, 32, widthMargin=0, heightMargin=5)
        self.setStateHandler("INIT", self.initHandler)
        self.setStateHandler("GAME", self.gameHandler)
        self.setStateHandler("END", self.endHandler)
        self.changeState("INIT")
        self.gameDirectory = "landOfDragons"
        self.caveImage = Image(path.join(self.gameDirectory, "cave.ppm"))
        self.titleScreen = Image(path.join(self.gameDirectory, "title_screen.ppm"))
        self.backgroundImage = Image(path.join(self.gameDirectory, "background.ppm"))
        self.treasureImage = Image(path.join(self.gameDirectory, "treasure.ppm"))
        self.goodDragonImage = Image(path.join(self.gameDirectory, "good_dragon.ppm"))
        self.evilDragonImage = Image(path.join(self.gameDirectory, "evil_dragon.ppm"))
        self.helpMessage = 'Witaj w grze "Smocza kraina"! twoim zadaniem będzie przejście przez 10 rund' + \
                           '\nW każdej z rund zostanie ci przedstawione parę jaskiń, które może zamieszkiwać smok przyjazny lub żarłoczny' + \
                           '\nSmoki przyjazne podzielą się z tobą swoimi skarbami i pozwolą ci na przejście do kolejnej rundy' + \
                           '\nSmoki żałoczne zaś pożrą cię co będzie skutkowało przegraniem gry' + \
                           '\nAby wybrać którąś z jaskiń wprowadź odpowiadający jej numer i naciśnij enter w momencie gdy gra cię o to poprosi' + \
                           '\nMożesz również w dowolnym momencie gry wprowadzić polecenie "menu" które przeniesie cię do menu gry'

    def initHandler(self):
        self.screen.setPixelsFromArray(self.titleScreen.pixels)
        self.screen.clearPixelsText()
        self.screen.clearScreen(full=True)
        self.screen.setText("Naciśnij enter aby rozpocząć", 50, 30, (0, 0, 0))
        self.screen.render(full=True)
        print(self.helpMessage)
        _ = input()
        self.gameData.roundNumber = 0
        self.gameData.dragons = self.generateDragons(self.gameData.roundNumber)
        self.changeState("GAME")

    def gameHandler(self):
        sep = self.generateCaveSeparation(self.gameData.roundNumber)
        img = self.backgroundImage
        self.screen.clearPixelsText()
        for i in range(self.gameData.roundNumber + 2):
            img = overlayImages(img, self.caveImage, sep * i + 2, 16)
            self.screen.setText(str(i), (sep * i + 2) * 2 + 4, 21)
        self.screen.setText(f"runda: {self.gameData.roundNumber + 1}", 2, 0)
        self.screen.setPixelsFromArray(img.pixels)

        self.screen.clearScreen(full=True)
        self.screen.render(full=True)
        choice = input("Wprowadź numer jaskini którą chcesz wybrać: ")
        if choice == "menu":
            self.changeState("MENU")
        else:
            try:
                choice = int(choice)
            except ValueError:
                print("Nie rozpoznano polecenia, naciśnij enter aby kontynuować")
                _ = input()
            else:
                if choice >= len(self.gameData.dragons) or choice < 0:
                    print("Numer jaskini jest poza zakresem, naciśnij enter aby kontynuować")
                    _ = input()
                else:
                    if self.gameData.dragons[choice]:
                        self.screen.setPixelsFromArray(self.goodDragonImage.pixels)
                        self.screen.clearPixelsText()
                        self.screen.clearScreen(full=True)
                        self.screen.render()
                        print("wybrano przyjaznego smoka!")
                        sleep(3)
                        self.gameData.roundNumber += 1
                        self.gameData.dragons = self.generateDragons(self.gameData.roundNumber)
                    else:
                        self.screen.setPixelsFromArray(self.evilDragonImage.pixels)
                        self.screen.clearPixelsText()
                        self.screen.clearScreen(full=True)
                        self.screen.render()
                        print("Wybrano żarłocznego smoka, Game Over")
                        sleep(3)
                        self.changeState("END")
        if self.gameData.roundNumber == 10:
            self.screen.setPixelsFromArray(self.treasureImage.pixels)
            self.screen.clearPixelsText()
            self.screen.clearScreen(full=True)
            self.screen.render(full=True)
            print("Brawo udało ci się zwyciężyć!")
            print("Smoczy skarb jest twój!")
            _ = input("Naciśnij enter aby kontynuować")
            self.changeState("END")

    def endHandler(self):
        print("Czy chcesz zakończyć grę czy rozpocząć nową?")
        print("1) nowa gra 2) zakończ")
        textInput = input()
        if textInput == "1":
            self.changeState("INIT")
        elif textInput == "2":
            self.running = False
        elif textInput == "menu":
            self.changeState("MENU")
            return
        else:
            print("Nie rozpoznano polecenia")

    def generateDragons(self, roundNumber: int) -> list:
        dragonNumber = 2 + roundNumber
        goodDragonNumber = round(dragonNumber * 0.3)
        evilDragonNumber = dragonNumber - goodDragonNumber
        goodDragons = [True for _ in range(goodDragonNumber)]
        evilDragons = [False for _ in range(evilDragonNumber)]

        dragons = goodDragons + evilDragons
        shuffle(dragons)
        return dragons

    def generateCaveSeparation(self, roundNumber: int) -> int:
        return 64 // (2 + roundNumber)


if __name__ == '__main__':
    game = LandOfDragons()
    game.run()
