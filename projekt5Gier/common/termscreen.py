from enum import Enum
import os
import platform
from copy import deepcopy, copy
import ctypes


class ColorMode(Enum):
    ASCII = 0
    ANSI4BIT = 1
    ANSI8BIT = 2
    ANSITRUECOLOR = 3


class RenderMode(Enum):
    ClASSIC = 0
    EXPERIMENTAL = 1


class RGBPALLETE(Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)


DEFAULTCHAR = "\u2588"


class Pixel:
    def __init__(self, channels: int = 3, char: str = DEFAULTCHAR):
        self.values = [0 for _ in range(channels)]
        self.charValues = [0 for _ in range(channels)]
        self.char = char

    def clear(self):
        self.values = [0 for _ in range(len(self.values))]
        self.charValues = [0 for _ in range(len(self.values))]
        self.char = DEFAULTCHAR

    def set(self, newValues):
        if len(newValues) == len(self.values):
            self.values = newValues

    def setChar(self, char, newValues: tuple = (0, 0, 0)):
        self.char = char
        self.charValues = newValues

    def clearChar(self):
        self.char = DEFAULTCHAR
        self.charValues = deepcopy(self.values)

    def __eq__(self, other):
        return self.values == other.values and self.charValues == other.charValues and self.char == other.char


class Screen:
    def __init__(self, width: int = 100, height: int = 100, mode: ColorMode = ColorMode.ANSITRUECOLOR,
                 renderMode: RenderMode = RenderMode.EXPERIMENTAL, widthMargin: int = 5, heightMargin: int = 5):
        self.width = width
        self.height = height
        self.widthMargin = widthMargin
        self.heightMargin = heightMargin
        self.colorMode = mode
        self.pixels = []
        self.textPixels = []
        self.initializeScreenSize()
        self.initializePixels()
        self.initializeColors()
        self.previousPixels = deepcopy(self.pixels)
        self.cursorX = 0
        self.cursorY = 0
        self.renderMode = renderMode
        self.previousTextPixels = deepcopy(self.textPixels)
        self.clearScreen(True)


    def initializePixels(self):
        if self.colorMode == ColorMode.ANSITRUECOLOR:
            for y in range(self.height):
                xList = []
                for x in range(self.width * 2):
                    pixel = Pixel(channels=3)
                    xList.append(pixel)
                self.pixels.append(xList)

    def setPixel(self, x: int, y: int, newValues, legacy = False):
        xCoord = x
        if legacy:
            yCoord = self.height - 1 - y
        else:
            yCoord = y
        self.pixels[yCoord][xCoord].set(newValues)

    def setPixelsFromArray(self, NewValues):
        if self.colorMode == ColorMode.ANSITRUECOLOR:
            if len(NewValues) == self.height and len(NewValues[0]) == self.width and len(NewValues[0][0]) == 3:
                for y, row in enumerate(NewValues):
                    for x, pixel in enumerate(row):
                        self.pixels[y][x * 2].set(pixel)
                        self.pixels[y][(x * 2) + 1].set(pixel)
            else:
                print(f"Image file has different dimensions than the screen")

    def setText(self, text, start_x, start_y, color: tuple = (0, 0, 0)):
        if self.colorMode == ColorMode.ANSITRUECOLOR:
            if len(text) + start_x <= len(self.pixels[0]):
                for x, char in enumerate(text):
                    self.pixels[start_y][start_x + x].setChar(char, color)
            else:
                raise ValueError("Coordinate out of screen bounds")

    def clearPixelsText(self):
        if self.colorMode == ColorMode.ANSITRUECOLOR:
            for row in self.pixels:
                for pixel in row:
                    pixel.clearChar()

    def clearPixels(self):
        for row in self.pixels:
            for pixel in row:
                pixel.clear()

    def clearScreen(self, full = False):
        if self.renderMode == RenderMode.EXPERIMENTAL and not full:
            # print("\x1b[F" * (self.height + 1))
            print("\x1b[H")
        elif platform.system() == "Windows":
            os.system("cls")
        elif platform.system() == "Linux":
            os.system("clear")
        elif platform.system() == "Darwin":
            os.system("clear")

    def render(self, blockInput=True, full=False):
        if blockInput:
            self.disableQuickEdit(True)
        if self.colorMode == ColorMode.ANSITRUECOLOR:
            if self.renderMode == RenderMode.EXPERIMENTAL:
                print("\x1b[48;5;0m", end="")
                for y in range(len(self.pixels)):
                    for x in range(0, len(self.pixels[0]), 1):
                        pixel = self.pixels[y][x]
                        if pixel != self.previousPixels[y][x] or full:
                            bgColor = f"\x1b[48;2;{pixel.values[0]};{pixel.values[1]};{pixel.values[2]}m"
                            char = pixel.char
                            if char == DEFAULTCHAR:
                                fgColor = f"\x1b[38;2;{pixel.values[0]};{pixel.values[1]};{pixel.values[2]}m"
                            else:
                                fgColor = f"\x1b[38;2;{pixel.charValues[0]};{pixel.charValues[1]};{pixel.charValues[2]}m"

                            renderString = bgColor + fgColor + char
                            self.moveCursorToPos(x, y + 1)
                            print(renderString, end="")
                            self.previousPixels[y][x] = deepcopy(pixel)

                self.moveCursorToPos(0, self.height + 1)
                self.resetColor()

            elif self.renderMode == RenderMode.ClASSIC:
                for row in self.pixels:
                    renderString = "\x1b[48;5;0m"
                    for pixel in row:
                        renderString += f"\x1b[38;2;{pixel.values[0]};{pixel.values[1]};{pixel.values[2]}m" + "\u2588" * 2
                    print(renderString)
        if blockInput:
            self.disableQuickEdit(False)

    def moveCursorToPos(self, x, y):
        leftString = f"\x1b[{y};{x+1}H"
        print(leftString, end="")

    def initializeColors(self):
        if platform.system() == "Windows":
            os.system("color")

    def resetColor(self):
        print("\x1b[0m", end="")

    def disableQuickEdit(self, value):
        if platform.system() == "Windows":
            kernel32 = ctypes.windll.kernel32
            if value:
                kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), (0x4 | 0x20 | 0x2 | 0x10 | 0x1))
            else:
                kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), (0x4 | 0x20 | 0x2 | 0x10 | 0x1 | 0x40))

    def initializeScreenSize(self):
        if platform.system() == "Windows":
            os.system(f"mode {self.width * 2 + self.widthMargin},{self.height + self.heightMargin}")
