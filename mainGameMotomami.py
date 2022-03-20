import pygame
import motomamiFunction as mF
import motomamiRessources as mR

pygame.init()

WINDOW = pygame.display.set_mode((0, 0))
WIDTH, HEIGHT = pygame.display.get_window_size()
pygame.display.set_caption("Motomami!")

FPS = 30


def main():

    starting_pos_background = (WIDTH // 2 - mR.background[1] // 2, HEIGHT // 2 - mR.background[2] // 2)
    starting_pos_player = (WIDTH // 2 - mR.player[1] // 2, HEIGHT // 2 - mR.player[2] // 2)
    WINDOW.blit(mR.background[0], starting_pos_background)
    WINDOW.blit(mR.player[0], starting_pos_player)

    player = mF.Player(starting_pos_background)
    player.velocity = 10

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
        x, y = player.update(pressed_key)
        WINDOW.blit(mR.background[0], (x, y))
        WINDOW.blit(mR.player[0], starting_pos_player)
        pygame.display.update()


if __name__ == "__main__":
    main()
