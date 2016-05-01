import config
import pygame

def drawExtras():
    pygame.draw.line(config.screen, (255,255,255), (100, 0), (100, config.height))
    pygame.draw.line(config.screen, (255,255,255), (config.width - 100, 0), (config.width - 100, config.height))
    pygame.draw.circle(config.screen, (255,255,255), (config.width / 2, config.height - 125), 75, 1)  
