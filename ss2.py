import pygame
import sys

img_galaxy = pygame.image.load("image_gl/galaxy.png")
# img_sship = pygame.image.load("image_gl/starship.png")

bg_y = 0


def main():
    global bg_y
    pygame.init()
    pygame.display.set_caption("Pygameの使い方")
    screen = pygame.display.set_mode((960, 720))
    clock = pygame.time.Clock()
    ang = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    screnn = pygame.display.set_mode(
                        (960, 720), pygame.FULLSCREEN)
                if event.key == pygame.K_F2 or event.key == pygame.K_ESCAPE:
                    screnn = pygame.display.set_mode((960, 720))

        bg_y = (bg_y+16) % 720
        screen.blit(img_galaxy, [0, bg_y-720])
        screen.blit(img_galaxy, [0, bg_y])

        pygame.display.update()
        clock.tick(30)


if __name__ == "__main__":
    main()
