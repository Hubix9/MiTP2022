from sys import exit
import glob
import os.path
import pickle
import re

class GameData:
    def __init__(self):
        pass

pressEnterToContinueStr = "Naciśnij enter aby kontynuować"

class Game:
    def __init__(self):
        self.state = "GAME"
        self.previousState = "GAME"
        self.stateHandlers = {}
        self.setStateHandler("MENU", self.menuHandler)
        self.setStateHandler("SAVE", self.saveHandler)
        self.setStateHandler("LOAD", self.loadHandler)
        self.setStateHandler("HELP", self.helpHandler)
        self.running = True
        self.screen = None
        self.gameDirectory = ""
        self.gameData = GameData()
        self.helpMessage = ""

    def changeState(self, state):
        self.previousState = self.state
        self.state = state

    # Run main game loop
    def run(self):
        self.running = True
        while self.running:
            self.stateHandlers[self.state]()

    # Low level internal function to save game state to a filename
    def save(self, filename):
        with open(os.path.join(self.gameDirectory, "saves", filename + ".save"), "wb") as f:
            pickle.dump(self.gameData, f)

    # Low level internal function to load game state from filename
    def load(self, filename):
        with open(filename, "rb") as f:
            self.gameData = pickle.load(f)

    def setStateHandler(self, state, callback):
        self.stateHandlers[state] = callback

    def menuHandler(self):
        print("Prosze wybierz jedną z poniższych opcji:")
        print("1) wznów 2) zapisz 3) wczytaj 4) pomoc 5) wyjdź ")
        command = input()
        if command == "1":
            self.changeState(self.previousState)
        elif command == "2":
            self.state = "SAVE"
        elif command == "3":
            self.state = "LOAD"
        elif command == "4":
            self.state = "HELP"
        elif command == "5":
            exit()
        else:
            self.screen.clearScreen(True)
            self.screen.render(full=True)
            print("Nie rozpoznano polecenia, wpisz pojedynczą cyfrę jako wybór opcji menu")

    def saveHandler(self):
        self.screen.clearScreen(True)
        self.screen.render(full=True)
        print("Wprowadź nazwę zapisu gry")
        filename = input("Nazwa zapisu:")
        if not re.search("^[a-zA-Z0-9_-]*$", filename):
            print("Nazwa zapisu może zawierać jedynie litery alfabetu angielskiego, cyfry, myślniki oraz podkreślniki")
            input(pressEnterToContinueStr)
            return
        if filename == "":
            return
        self.save(filename)
        self.state = "MENU"

    def loadHandler(self):
        self.screen.clearScreen(True)
        self.screen.render(full=True)
        files = glob.glob(os.path.join(self.gameDirectory, "saves", "*.save"))
        if len(files) == 0:
            print("Nie znaleziono żadnych zapisanych gier")
            input(pressEnterToContinueStr)
            self.state = "MENU"
            return
        for i, file in enumerate(files):
            print(f"{i}) {file}")
        fileNumber = input("Wprowadź numer pliku który chcesz wczytać: ")
        try:
            fileNumber = int(fileNumber)
            self.load(files[fileNumber])
            self.state = "MENU"
        except IndexError:
            print("Numer zapisu poza indeksem")
            input(pressEnterToContinueStr)
        except ValueError:
            print("Nie wprowadzono liczby całkowitej")
            input(pressEnterToContinueStr)

    def helpHandler(self):
        self.screen.clearScreen(full=True)
        self.screen.render(full=True)
        print(self.helpMessage)
        input(pressEnterToContinueStr)
        self.state = "MENU"

    def enableMenu(self, value):
        pass
