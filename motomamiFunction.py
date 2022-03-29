import pygame
import motomamiRessources as mR
from vector import Vector


class Player:

    def __init__(self, position):
        self.position = position
        self.velocity = 25

    def update(self, pressed_key):

        if pressed_key[pygame.K_LEFT]:
            print("")
            self.position += Vector(self.velocity, 0)
        if pressed_key[pygame.K_RIGHT]:
            self.position -= Vector(self.velocity, 0)

        if pressed_key[pygame.K_UP]:
            self.position += Vector(0, self.velocity)
        if pressed_key[pygame.K_DOWN]:
            self.position -= Vector(0, self.velocity)


class Mob(Player):

    def __init__(self, position):
        super().__init__(position)
        self.velocity = 10

    def update_mob(self, pressed_key):
        print("1")
        self.update(pressed_key)
        print("3")
        self.position += Vector(self.velocity, self.velocity)
