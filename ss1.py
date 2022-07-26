import pygame
import sys
import math

img_galaxy = pygame.image.load("image_gl/galaxy.png")
img_sship = pygame.image.load("image_gl/starship.png")


def main():
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

        screen.blit(img_galaxy, [0, 0])

        ang = (ang+1) % 360
        img_rz = pygame.transform.rotozoom(
            img_sship, ang, 1.0+math.sin(ang/10))
        x = 480 - img_rz.get_width()/2
        y = 360 - img_rz.get_height()/2
        screen.blit(img_rz, [x, y])

        pygame.display.update()
        clock.tick(30)


if __name__ == "__main__":
    main()
