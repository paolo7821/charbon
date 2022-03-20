import pygame
import motomamiRessources as mR


class Player:

    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]
        self.velocity = 1

    def update(self, pressed_key):

        if pressed_key[pygame.K_LEFT]:
            self.x += self.velocity
        if pressed_key[pygame.K_RIGHT]:
            self.x -= self.velocity

        if pressed_key[pygame.K_UP]:
            self.y += self.velocity
        if pressed_key[pygame.K_DOWN]:
            self.y -= self.velocity

        return self.x, self.y



