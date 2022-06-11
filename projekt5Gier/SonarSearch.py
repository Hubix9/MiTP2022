from common.termscreen import Screen
from common.ppmReader import Image
from common.game import Game
from random import randint
from math import sqrt, floor

from dataclasses import dataclass
import os.path as path


class SonarSearch(Game):
    @dataclass
    class Message:
        text: str
        color: tuple

    @dataclass
    class MapItem:
        pass

    @dataclass
    class Crate(MapItem):
        x: int
        y: int
        found: bool = False

    @dataclass
    class Dud(MapItem):
        rangeToNearestCrate: int

    def __init__(self):
        super(SonarSearch, self).__init__()
        self.screen = Screen(64, 32, widthMargin=0, heightMargin=5)
        self.setStateHandler("INIT", self.initHandler)
        self.setStateHandler("GAME", self.gameHandler)
        self.setStateHandler("END", self.endHandler)
        self.changeState("INIT")
        self.gameDirectory = "sonarSearch"
        self.titleScreen = Image(path.join(self.gameDirectory, "title_screenv2.ppm"))
        self.waterImage = Image(path.join(self.gameDirectory, "water_instruments.ppm"))
        self.loseImage = Image(path.join(self.gameDirectory, "game_over.ppm"))
        self.winImage = Image(path.join(self.gameDirectory, "game_win.ppm"))
        self.invalidValueMessage = "Niepoprawna wartość"
        self.greenColor = (34, 255, 0)
        self.redColor = (255, 17, 0)
        self.boardDimensions = (60, 15)
        self.maxRange = 5
        self.helpMessage = 'Witaj w grze "Poszukiwanie skarbu sonarem"! twoim zadaniem będzie odnalezienie zatopionych skrzyń' \
                           '\nSonar posiada wystarczająco energi na jedynie 20 impulsów' \
                           '\nstąd też musisz jak najwydajniej wybierać miejsca wykonywania impulsów aby udało ci się odnaleźć wszystkie skrzynie' \
                           '\nDo wykonania impulsu wymagane jest podanie współrzędnych w których ma on zostać wysłany.' \
                           '\nW tym celu odczytaj współrzędne z mapy a następnie wprowadź je w momencie gdy gra Cię o nie poprosi' \
                           '\nNajpier wprowadź współrzędną x, a następnie oddzielając je spacją wprowadź współrzędną y' \
                           '\nPrzykład: 20 5, rownież w dowolnym momencie gry możesz wprowadzić polecenie "menu" które przeniesie Cię do menu gry' \
                           '\nOdnaleziona skrzynia zostanie oznaczona jako zielony znak "@"' \
                           '\nW innym wypadku zostanie ci przedstawiony dystans do najbliższej skrzyni' \
                           '\nJesli maksymalny dystans sonaru (5) zostanie przekroczony, plansza wyświetli znak "X"'

    def difficultyPrompt(self):
        @dataclass
        class Difficulty:
            name: str
            crateNumber: int

        difficulties = [Difficulty("łatwy", 3), Difficulty("zaawansowany", 5), Difficulty("ekspert", 8)]
        print("")
        for i, diff in enumerate(difficulties):
            print(f"{i}) {diff.name}")
        while True:
            textInput = input("Wybierz poziom trudności: ")
            try:
                selection = int(textInput)
                if not (len(difficulties) > selection >= 0):
                    print(self.invalidValueMessage)
                else:
                    difficulty = difficulties[selection]
                    self.gameData.crateNumber = difficulty.crateNumber
                    print(
                        f"Wybrano poziom trudności: {difficulty.name}, liczba skrzyń do odnalezienia: {difficulty.crateNumber}")
                    break
            except ValueError:
                print(self.invalidValueMessage)

    def generateMap(self, width, height, amount):
        self.gameData.map = []
        self.gameData.crates = []
        self.gameData.duds = []
        for y in range(height):
            tempList = []
            for x in range(width):
                tempList.append(self.MapItem())
            self.gameData.map.append(tempList)
        for _ in range(amount):
            x = randint(0, width - 1)
            y = randint(0, height - 1)
            while isinstance(self.gameData.map[y][x], self.Crate):
                x = randint(0, width - 1)
                y = randint(0, height - 1)
            self.gameData.map[y][x] = self.Crate(x, y)
            self.gameData.crates.append(self.gameData.map[y][x])

    def initHandler(self):
        self.gameData.charges = 20
        self.gameData.messages = []
        self.screen.setPixelsFromArray(self.titleScreen.pixels)
        self.screen.clearPixelsText()
        self.screen.clearScreen(full=True)
        self.screen.setText("Naciśnij enter aby rozpocząć", 50, 30, (255, 255, 255))
        self.screen.render(full=True)
        _ = input()
        print(self.helpMessage)
        print("")
        _ = input("naciśnij enter aby kontynuować")
        self.difficultyPrompt()
        print("")
        _ = input("naciśnij enter aby kontynuować")
        self.generateMap(self.boardDimensions[0], self.boardDimensions[1], self.gameData.crateNumber)
        self.changeState("GAME")

    def gameHandler(self):
        while True:
            foundCrates = [x for x in self.gameData.crates if x.found]
            self.screen.clearPixelsText()
            self.screen.clearPixels()
            if self.gameData.charges == 0:
                self.screen.setPixelsFromArray(self.loseImage.pixels)
                self.screen.clearScreen(full=True)
                self.screen.render(full=True)
                print("Koniec energi w akumulatorach sonaru")
                print(f"liczba odnalezionych skrzyń: {len(foundCrates)}")
                print(f"Łączna liczba skrzyń: {self.gameData.crateNumber}")
                self.changeState("END")
                break
            if len(foundCrates) == len(self.gameData.crates):
                self.screen.clearPixelsText()
                self.screen.clearPixels()
                self.screen.setPixelsFromArray(self.winImage.pixels)
                self.screen.clearScreen(full=True)
                self.screen.render(full=True)
                print("Udało Ci się zebrać wszystkie skrzynie")
                print(f"łączna liczba skrzyń: {self.gameData.crateNumber}")
                self.changeState("END")
                break
            self.drawMap(5, 2, self.boardDimensions[0], self.boardDimensions[1], self.greenColor)
            foundCrates = [x for x in self.gameData.crates if x.found]
            self.screen.clearScreen(full=True)
            self.drawMessageBoard(82, 2, self.gameData.messages, 10)
            self.screen.setText(f"pozostałe skrzynie: {len(self.gameData.crates) - len(foundCrates)}", 44, 23,
                                self.greenColor)
            self.screen.setText(f"zebrane skrzynie: {len(foundCrates)}", 44, 24, self.greenColor)
            self.screen.setText("BAT: 1", 106, 15, self.greenColor)
            self.screen.setText("BAT: 2", 118, 15, self.greenColor)
            self.drawChargeGauge(106, 20, self.gameData.charges - 10, 10)
            self.drawChargeGauge(118, 20, self.gameData.charges, 10)
            self.screen.render(full=True)

            self.screen.moveCursorToPos(4, 29)
            textInput = input("wprowadź współrzędne: ")
            if textInput == "menu":
                self.changeState("MENU")
                self.screen.moveCursorToPos(0, 33)
                break
            try:
                splitInput = textInput.split(" ")
                if len(splitInput) != 2:
                    mess = self.Message(self.invalidValueMessage, self.redColor)
                    self.gameData.messages.append(mess)
                    continue
                x = int(splitInput[0])
                y = int(splitInput[1])
                if isinstance(self.gameData.map[y][x], self.Crate):
                    self.gameData.map[y][x].found = True
                    mess = self.Message(f"Znaleziono skrzynię!: {x}, {y}", self.greenColor)
                else:
                    rangeToNearestCrate = self.maxRange + 1
                    for crate in self.gameData.crates:
                        rangeTmp = round(sqrt((x - crate.x) ** 2 + (y - crate.y) ** 2), 2)
                        if rangeTmp < rangeToNearestCrate:
                            rangeToNearestCrate = rangeTmp
                    self.gameData.map[y][x] = self.Dud(rangeToNearestCrate)
                    self.gameData.duds.append(self.gameData.map[y][x])
                    if rangeToNearestCrate > self.maxRange:
                        mess = self.Message(f"Brak skrzyni w zasięgu: {x}, {y}", self.redColor)
                    else:
                        mess = self.Message(f"Dystans:{rangeToNearestCrate} współrzedne: {x}, {y}", self.redColor)
                self.gameData.messages.append(mess)
                self.gameData.charges -= 1
            except IndexError:
                mess = self.Message(self.invalidValueMessage, self.redColor)
                self.gameData.messages.append(mess)
            except ValueError:
                mess = self.Message(self.invalidValueMessage, self.redColor)
                self.gameData.messages.append(mess)

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

    def drawMap(self, x, y, width, height, color=(255, 255, 255)):
        self.screen.setPixelsFromArray(self.waterImage.pixels)
        topBarCoords = (x + 3, y)
        tensBar = ""
        onesBar = ""
        for i in range(1, width // 10, 1):
            tensBar += " " * 9 + str(i)
        while len(onesBar) != width:
            for i in range(10):
                onesBar += str(i)
                if len(onesBar) == width:
                    break

        self.screen.setText(tensBar, topBarCoords[0], topBarCoords[1],
                            color)
        self.screen.setText(onesBar, topBarCoords[0],
                            topBarCoords[1] + 1, color)
        for i in range(height):
            self.screen.setText(str(i), x, y + i + 2, color)

        for yCoord, row in enumerate(self.gameData.map):
            for xCoord, element in enumerate(row):
                if isinstance(element, self.Crate):
                    if element.found:
                        self.screen.setText("@", xCoord + x + 3, yCoord + y + 2, self.greenColor)
                elif isinstance(element, self.Dud):
                    printStr = "X" if element.rangeToNearestCrate > self.maxRange else floor(
                        element.rangeToNearestCrate)
                    self.screen.setText(str(printStr), xCoord + x + 3, yCoord + y + 2, self.redColor)

    def drawChargeGauge(self, x, y, value, length):
        for i in range(length):
            if i >= (length - value):
                self.screen.setText("\u2593" * 2, x, y + i, (255, 17, 0))
            self.screen.setText(f"{length - i}", x + 4, y + i, (255, 255, 255))

    def drawMessageBoard(self, x, y, messages, amount):
        for i, message in enumerate(messages[-amount:]):
            self.screen.setText(message.text, x, y + i, message.color)


if __name__ == '__main__':
    game = SonarSearch()
    game.run()
