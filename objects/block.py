import pygame
from utils import config
import copy

class Block:
    def __init__(self):
        self.blocks = []
        self.delay = 0
        self.levelFile = "levels/0.txt"
        self.level = filter(None, open(self.levelFile).read().split("\n"))
        self.centerSquareBlock = pygame.Rect(config.width / 2 - 12, -25, 25, 25)
        self.leftSquareBlock = pygame.Rect(100, -25, 25, 25)
        self.rightSquareBlock = pygame.Rect(config.width - 125, -25, 25, 25)

        self.centerRectBlock = pygame.Rect(config.width / 2 - 12, -25, 100, 25)
        self.leftRectBlock = pygame.Rect(100, -25, 100, 25)
        self.rightRectBlock = pygame.Rect(config.width - 1100, -25, 100, 25)

    def update(self, red, blue):
        self.red = red
        self.blue = blue
        if self.delay == 0 and len(self.level) > 0:
            block = self.level.pop(0)
            block = block.split(",")
            typeOf = block[0]
            location = block[1]
            delay = int(block[2])
            self.delay = delay
            if typeOf == "r":
                if location == "l":
                    self.blocks.append(copy.copy(self.leftRectBlock))
                elif location == "c":
                    self.blocks.append(copy.copy(self.centerRectBlock))
                elif locationn == "r":
                    self.blocks.append(copy.copy(self.rightRectBlock))

            elif typeOf == "s":
                if location == "l":
                    self.blocks.append(copy.copy(self.leftSquareBlock))
                elif location == "c":
                    self.blocks.append(copy.copy(self.centerSquareBlock))
                elif location == "r":
                    self.blocks.append(copy.copy(self.rightSquareBlock))

        elif self.delay > 0:
            self.delay -= 1
        self.moveBlocks()

    def moveBlocks(self):
        for block in self.blocks:
            block.y += 4
            if block.colliderect(self.blue):
                print "Collided blue"
            elif block.colliderect(self.red):
                print "Collided red"
            if block.y >= config.height:
                self.blocks.remove(block)
            else:
                pygame.draw.rect(config.screen, (255,255,255), block)
