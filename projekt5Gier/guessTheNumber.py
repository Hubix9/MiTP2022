from common.termscreen import Screen
from common.ppmReader import Image
from common.game import Game
from random import randint


class GuessTheNumber(Game):

    def __init__(self):
        super(GuessTheNumber, self).__init__()
        self.screen = Screen(64, 32, widthMargin=0, heightMargin=5)
        self.setStateHandler("INIT", self.initHandler)
        self.setStateHandler("GAME", self.gameHandler)
        self.setStateHandler("END", self.endHandler)
        self.changeState("INIT")
        self.gameDirectory = "zgadnijLiczbe"

    def initHandler(self):
        titleScreen = Image("zgadnijLiczbe/title_screen.ppm")
        self.screen.setPixelsFromArray(titleScreen.pixels)
        self.screen.clearPixelsText()
        self.screen.clearScreen(full=True)
        self.screen.setText("Naciśnij enter aby rozpocząć", 56, 30, (0, 0, 0))
        self.screen.render(full=True)
        _ = input()
        self.screen.clearPixelsText()
        self.screen.clearScreen(full=True)
        self.screen.render(full=True)
        self.gameData.magicNumber = randint(0, 100)
        self.gameData.tries = 0
        self.gameData.initDone = False
        self.changeState("GAME")
        self.previousState = "GAME"
        self.helpMessage = "Aby dokonać operacji w grze musisz wprowadzić liczbę w momencie kiedy gra cię o to poprosi" + \
                           "\nW dowolnym momencie możesz wprowadzić również polecenie: menu, zamiast wartości sugerowanej przez grę" + \
                           "\nZASADY GRY:" + \
                           "\nMasz 6 prób na zgadnięcie liczby z zakresu od 0 do 100" + \
                           "\nPo każdej próbie otrzymasz informację czy podana przez ciebię liczba jest mniejsza lub większa od docelowej" + \
                           "\nPowodzenia!"

    def gameHandler(self):
        if not self.gameData.initDone:
            print("Witaj w grze zgadnij liczbę!")
            print("Właśnie wylosowano liczbę całkowitą z zakresu od 0 do 100")
            print(
                "Masz 6 prób na zgadnięcie jaka to liczba, jako wskazówki powiem ci czy podane liczby są zbyt małe lub zbyt duże")
            print("W dowolnym momencie możesz skorzystać z menu, wpisując polecenie: menu, zamiast liczby")
            self.gameData.initDone = True
        if self.gameData.tries < 6:
            print(f"liczba pozostałych prób: {6 - self.gameData.tries}")
            number = input("wprowadź liczbę: ")
            try:
                number = int(number)
            except ValueError:
                if number == "menu":
                    self.changeState("MENU")
                else:
                    print("Nie wprowadzono liczby całkowitej lub polecenia menu")
                return

            if number == self.gameData.magicNumber:
                print("GRATULACJE! wprowadzono poprawną liczbę")
                self.changeState("END")
                return
            elif number < self.gameData.magicNumber:
                print("Wprowadzona przez Ciebię liczba jest za mała")
            elif number > self.gameData.magicNumber:
                print("Wprowadzona przez Ciebie liczba jest zbyt duża")
            self.gameData.tries += 1
        else:
            print("Niestety, przegrałeś")
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


if __name__ == '__main__':
    game = GuessTheNumber()
    game.run()
