import pygame
import motomamiFunction as mF
import motomamiRessources as mR
from vector import Vector

pygame.init()

WINDOW = pygame.display.set_mode((0, 0))
WIDTH, HEIGHT = pygame.display.get_window_size()
print(HEIGHT, WIDTH)
pygame.display.set_caption("Motomami!")

FPS = 30


def main():

    starting_pos_background = Vector(WIDTH // 2 - mR.background[1] // 2, HEIGHT // 2 - mR.background[2] // 2)
    starting_pos_player = Vector(WIDTH // 2 - mR.player[1] // 2, HEIGHT // 2 - mR.player[2] // 2)
    WINDOW.blit(mR.background[0], starting_pos_background.vector)
    WINDOW.blit(mR.player[0], starting_pos_player.vector)

    player = mF.Player(starting_pos_background)
    mob1 = mF.Mob(Vector(100, 100))
    mob2 = mF.Mob(Vector(100, 200))
    mob2.velocity = 20

    clock = pygame.time.Clock()
    run = True
    while run:

        WINDOW.fill("black")

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        pressed_key = pygame.key.get_pressed()
        player.update(pressed_key)
        mob1.update_mob(pressed_key)
        mob2.update_mob(pressed_key)
        WINDOW.blit(mR.background[0], player.position.vector)
        pygame.draw.circle(WINDOW, "red", mob1.position.vector, 50)
        pygame.draw.circle(WINDOW, "blue", mob2.position.vector, 50)
        WINDOW.blit(mR.player[0], starting_pos_player.vector)
        pygame.display.update()


if __name__ == "__main__":
    main()
