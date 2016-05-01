from utils import config
import pygame
import math

class Player:
    def __init__(self):
        self.angle1 = 1
        self.angle2 = 180
        self.radius = 75
        self.speed = 3
        self.distFromBottom = 60
        self.playerSize = 13
        self.lastMovement = 0
        self.blue = pygame.Rect(0, 0, self.playerSize, self.playerSize)
        self.red = pygame.Rect(0, 0, self.playerSize, self.playerSize)
        self.move(1) # Sets the two objects the correct distance apart
        self.move(-1)

    def update(self):
        
        self.draw()
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.move(-1)
        elif key[pygame.K_LEFT]:
            self.move(1)

    def move(self, direction):
        x1 = config.width / 2 - self.playerSize / 2 + math.sin(math.radians(self.angle1)) * self.radius
        y1 = config.height + self.playerSize / 2 - self.distFromBottom - self.radius + math.cos(math.radians(self.angle1)) * self.radius
        x2 = config.width / 2 - self.playerSize / 2 + math.sin(math.radians(self.angle2)) * self.radius
        y2 = config.height + self.playerSize / 2 - self.distFromBottom - self.radius + math.cos(math.radians(self.angle2)) * self.radius
        self.blue.x = x1
        self.blue.y = y1
        self.red.x = x2
        self.red.y = y2
        self.angle1 += 4 * direction
        self.angle2 += 4 * direction

    def draw(self):
        pygame.draw.rect(config.screen, (0, 0, 255), self.blue)
        pygame.draw.rect(config.screen, (255, 0, 0), self.red)

