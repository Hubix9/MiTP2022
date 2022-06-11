from common.termscreen import Screen
from common.compositing import overlayImages
from common.ppmReader import Image
from common.game import Game
from random import randint
from os import path

from multiprocessing import Process, Queue
from queue import Empty
from dataclasses import dataclass
from math import sqrt, asin, degrees, sin, cos, tan, radians, ceil, floor
from common.hitbox import detectRayHit, ddaHit
from time import time, sleep
from collections import deque
import common.thirdParty.keyboard as keyboard
import sys


class Pong(Game):
    @dataclass
    class Pos:
        x: int
        y: int

    class Ball:
        def __init__(self, initialX, initialY, initialVector, mapWidth, mapHeight):
            self.x = initialX
            self.y = initialY
            self.vector = initialVector
            self.width = mapWidth
            self.height = mapHeight
            self.hitCooldown = 0

        def move(self):
            self.x += self.vector[0]
            self.y += self.vector[1]

            if round(self.x) <= 0 or round(self.x) >= self.width:
                self.vector = [self.vector[0] * -1, self.vector[1]]
                if round(self.x) <= 0:
                    self.x = 1
                else:
                    self.x = self.width - 1

            if round(self.y <= 0) or round(self.y) >= self.height:
                self.vector = [self.vector[0], self.vector[1] * -1]
                if round(self.y) <= 0:
                    self.y = 1
                else:
                    self.y = self.height - 1

        def handleCollision(self, objX, objY, objWidth, objHeight):
            if self.hitCooldown > 0:
                self.hitCooldown -= 1
                return

            vecEndpoint = [self.x + self.vector[0], self.y + self.vector[1]]

            hit = ddaHit(self.x, self.y, vecEndpoint[0], vecEndpoint[1], objX, objY, objWidth, objHeight, 1, 1)
            if hit:
                confirmed = False
                distFromCenter = objY + (objHeight // 2) - self.y
                if -1.5 >= distFromCenter > -2.5:
                    self.vector = [(self.vector[0] * -1), 0.5]
                    confirmed = True
                elif -0.5 >= distFromCenter > -1.5:
                    self.vector = [self.vector[0] * -1, 0.25]
                    confirmed = True
                elif 0 >= distFromCenter > -0.5 or 0.5 > distFromCenter >= 0:
                    self.vector = [self.vector[0] * -1, 0]
                    confirmed = True
                elif 1.5 > distFromCenter >= 0.5:
                    self.vector = [self.vector[0] * -1, -0.25]
                    confirmed = True
                elif 2.5 > distFromCenter >= 1.5:
                    self.vector = [self.vector[0] * -1, -0.5]
                    confirmed = True
                if confirmed:
                    # self.x += 1
                    self.vector[0] = self.vector[0] * 1.01
                    self.hitCooldown = 10
                else:
                    self.vector = [self.vector[0] * -1, self.vector[1] * -1]

    class Paddle:
        def __init__(self, x, y, image: Image, keybinds: dict, xBarrier):
            self.x = x
            self.y = y
            self.image = image
            self.keybinds = keybinds
            self.queue = deque()
            self.xBarrier = xBarrier
            self.leftBound = True if self.x < self.xBarrier else False

        def pushChars(self, chars):
            for char in chars:
                self.queue.append(char)

        def handleUp(self):
            if self.y > 0:
                self.y -= 1

        def handleDown(self):
            if self.y + 5 < 32:
                self.y += 1

        def handleLeft(self):
            if self.x > 0:
                self.x -= 1

        def handleRight(self):
            if self.x < (63 - 9):
                self.x += 1

        def handleInput(self):
            if keyboard.is_pressed(self.keybinds["up"]):
                if self.y > 0:
                    self.y -= 1
            elif keyboard.is_pressed(self.keybinds["down"]):
                if self.y + 5 < 32:
                    self.y += 1
            elif keyboard.is_pressed(self.keybinds["left"]):
                if self.x > 0 and (self.leftBound or self.x > self.xBarrier):
                    self.x -= 1
            elif keyboard.is_pressed(self.keybinds["right"]):
                if self.x < (63 - 9) and (not self.leftBound or self.x < self.xBarrier):
                    self.x += 1

    def __init__(self):
        super(Pong, self).__init__()
        self.screen = Screen(64, 32, widthMargin=0, heightMargin=5)
        self.setStateHandler("INIT", self.initHandler)
        self.setStateHandler("GAME", self.gameHandler)
        self.setStateHandler("END", self.endHandler)
        self.changeState("INIT")
        self.gameDirectory = "pong"
        self.titleScreen = Image(path.join(self.gameDirectory, "title_screen.ppm"))
        self.paddleImage = Image(path.join(self.gameDirectory, "paddle.ppm"))
        self.backgroundImage = Image(path.join(self.gameDirectory, "game_background_color.ppm"))
        self.redPaddleImage = Image(path.join(self.gameDirectory, "pong_red_paddle.ppm"))
        self.blackPaddleImage = Image(path.join(self.gameDirectory, "pong_black_paddle.ppm"))
        self.trophyImage = Image(path.join(self.gameDirectory, "pong_trophy.ppm"))
        self.digitImages = {0: Image(path.join(self.gameDirectory, "digits", "digit_0.ppm")),
                            1: Image(path.join(self.gameDirectory, "digits", "digit_1.ppm")),
                            2: Image(path.join(self.gameDirectory, "digits", "digit_2.ppm")),
                            3: Image(path.join(self.gameDirectory, "digits", "digit_3.ppm")),
                            4: Image(path.join(self.gameDirectory, "digits", "digit_4.ppm")),
                            5: Image(path.join(self.gameDirectory, "digits", "digit_5.ppm")),
                            6: Image(path.join(self.gameDirectory, "digits", "digit_6.ppm")),
                            7: Image(path.join(self.gameDirectory, "digits", "digit_7.ppm")),
                            8: Image(path.join(self.gameDirectory, "digits", "digit_8.ppm")),
                            9: Image(path.join(self.gameDirectory, "digits", "digit_9.ppm"))}

        self.lastFrame = time()
        self.timeDelta = 0.001
        self.winScore = 10
        self.enteredMenu = False

    def initHandler(self):
        self.helpMessage = "Witaj w grze Pong!\n" \
                           "Gra została przeznaczona dla dwóch osób grających na jednej klawiaturze\n" \
                           "Gracz A steruje następującymi klawiszami: w (góra), a (lewo), d (prawo), s (dół)\n" \
                           "Gracz B steruje następującymi klawiszami: i (góra), j (lewo), l (prawo), k (dół)\n" \
                           "Gracze mogą poruszać paletkami po całej powierzchni swoich połów boiska\n" \
                           "Gra zakończy się gdy jeden z graczy osiągnie wynik 10\n" \
                           "Miłej gry!"
        self.screen.setPixelsFromArray(self.titleScreen.pixels)
        self.screen.clearPixelsText()
        self.screen.clearScreen(full=True)
        self.screen.setText("Naciśnij enter aby rozpocząć", 50, 30, (0, 0, 0))
        self.screen.render(full=True)
        print(self.helpMessage)
        input()
        self.screen.clearPixelsText()
        self.screen.clearScreen(full=True)
        self.screen.render(full=True)

        self.gameData.playerAPaddle = self.Paddle(0, 13, self.redPaddleImage,
                                                  {"up": "w", "down": "s", "left": "a", "right": "d"}, 22)
        self.gameData.playerBPaddle = self.Paddle(54, 13, self.blackPaddleImage,
                                                  {"up": "i", "down": "k", "left": "j", "right": "l"}, 32)
        self.gameData.ball = self.Ball(64, 15, [-1, 0], 128 - 2, 32)
        self.gameData.playerAScore = 0
        self.gameData.playerBScore = 0
        self.changeState("GAME")

    def overlayPlayerScores(self, scoreA, scoreB, img, aX, aY, bX, bY) -> Image:
        img = overlayImages(img, self.digitImages[scoreA], aX, aY)
        img = overlayImages(img, self.digitImages[scoreB], bX, bY)
        return img

    def gameHandler(self):
        if self.enteredMenu:
            self.screen.clearScreen(full=True)
            self.screen.render(full=True)
            self.enteredMenu = False
        tmpImg = overlayImages(self.backgroundImage, self.redPaddleImage, self.gameData.playerAPaddle.x,
                               self.gameData.playerAPaddle.y)
        tmpImg = overlayImages(tmpImg, self.blackPaddleImage, self.gameData.playerBPaddle.x,
                               self.gameData.playerBPaddle.y)
        tmpImg = self.overlayPlayerScores(self.gameData.playerAScore, self.gameData.playerBScore, tmpImg, 10, 2, 45,
                                          2)
        self.screen.setPixelsFromArray(tmpImg.pixels)
        self.screen.clearPixelsText()
        self.screen.clearScreen()
        self.screen.setText("\u2593" * 2, round(self.gameData.ball.x), round(self.gameData.ball.y), (255, 255, 255))
        self.screen.setText(f"fps: {abs(1 / self.timeDelta)}", 0, 0, (255, 255, 255))
        self.screen.render()
        self.gameData.playerAPaddle.handleInput()
        self.gameData.playerBPaddle.handleInput()
        self.timeDelta = self.lastFrame - time()
        self.lastFrame = time()
        self.gameData.ball.move()
        self.gameData.ball.handleCollision((self.gameData.playerAPaddle.x + 7) * 2, self.gameData.playerAPaddle.y,
                                           1 * 1, 5)
        self.gameData.ball.handleCollision((self.gameData.playerBPaddle.x + 2) * 2, self.gameData.playerBPaddle.y,
                                           1 * 1, 5)
        if self.gameData.ball.x <= 1:
            self.gameData.playerBScore += 1
            self.gameData.ball.x = 64
            self.gameData.ball.y = 15
            self.gameData.ball.vector = [1, 0]
        elif self.gameData.ball.x >= 125:
            self.gameData.playerAScore += 1
            self.gameData.ball.x = 64
            self.gameData.ball.y = 15
            self.gameData.ball.vector = [-1, 0]

        if self.gameData.playerAScore == self.winScore or self.gameData.playerBScore == self.winScore:
            self.screen.setPixelsFromArray(self.trophyImage.pixels)
            self.screen.clearPixelsText()
            self.screen.clearScreen(full=True)
            if self.gameData.playerAScore == self.winScore:
                winnerText = "Gracz A wygrywa!"
            else:
                winnerText = "Gracz B wygrywa!"
            self.screen.setText(winnerText, 56, 29)
            self.screen.render(full=True)
            self.changeState("END")

        if keyboard.is_pressed("m"):
            self.changeState("MENU")
            self.enteredMenu = True

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
    game = Pong()
    game.run()
