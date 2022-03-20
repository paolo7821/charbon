import pygame

background = pygame.image.load("resources/background.png")
background = [background, background.get_width(), background.get_height()]
player = pygame.transform.scale(pygame.image.load("resources/player.png"), (150, 183))
player = [player, player.get_width(), player.get_height()]