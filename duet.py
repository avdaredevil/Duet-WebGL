import pygame
from pygame.locals import *
from objects import *
from utils import *
import sys

def run():
    screen = pygame.display.set_mode((config.width, config.height))
    config.screen = screen
    clock = pygame.time.Clock()
    Player = player.Player()
    Block = block.Block()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()            
        clock.tick(60)
        screen.fill((0,0,0))
        drawExtras.drawExtras()
        Player.update()
        Block.update(Player.red, Player.blue)
        pygame.display.update()


if __name__ == "__main__":
    run()
