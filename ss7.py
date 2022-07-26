import pygame
import sys
from pygame.locals import *

img_galaxy = pygame.image.load("image_gl/galaxy.png")
img_sship = [
    pygame.image.load("image_gl/starship.png"),
    pygame.image.load("image_gl/starship_l.png"),
    pygame.image.load("image_gl/starship_r.png"),
    pygame.image.load("image_gl/starship_burner.png"),
]
img_weapon = pygame.image.load("image_gl/bullet.png")

tmr = 0  # タイマー変数
bg_y = 0

ss_x = 480
ss_y = 360
ss_d = 0  # 自機の傾き変数
key_spc = 0  # スペースキーを押した時に使う変数

MISSILE_MAX = 200
msl_no = 0
msl_f = [False]*MISSILE_MAX  # 弾が発射中かを管理するフラグ
msl_x = [0]*MISSILE_MAX  # 弾のx座標
msl_y = [0]*MISSILE_MAX  # 弾のy座標


def move_starship(scrn, key):  # 自機の移動
    global ss_x, ss_y, ss_d, key_spc
    ss_d = 0
    if key[K_UP] == 1:
        ss_y = ss_y - 20
        if ss_y < 80:
            ss_y = 80
    if key[K_DOWN] == 1:
        ss_y = ss_y + 20
        if ss_y > 640:
            ss_y = 640
    if key[K_LEFT] == 1:
        ss_d = 1
        ss_x = ss_x - 20
        if ss_x < 40:
            ss_x = 40
    if key[K_RIGHT] == 1:
        ss_d = 2
        ss_x = ss_x + 20
        if ss_x > 920:
            ss_x = 920

    key_spc = (key_spc+1) * key[K_SPACE]  # スペースキーを押している間key_spcを加算
    if key_spc % 5 == 1:
        set_missile()
    scrn.blit(img_sship[3], [ss_x-8, ss_y+40+(tmr % 3)*2])
    scrn.blit(img_sship[ss_d], [ss_x-37, ss_y-48])


def set_missile():
    global msl_no
    msl_f[msl_no] = True
    msl_x[msl_no] = ss_x
    msl_y[msl_no] = ss_y - 50
    msl_no = (msl_no+1) % MISSILE_MAX


def move_missile(scrn):
    global msl_f, msl_y
    for i in range(MISSILE_MAX):
        if msl_f[i] == True:
            msl_y[i] = msl_y[i]-36
            scrn.blit(img_weapon, [msl_x[i]-10, msl_y[i]-32])
            if msl_y[i] < 0:
                msl_f[i] = False


def main():  # メインループ
    global tmr, bg_y
    pygame.init()
    pygame.display.set_caption("Pygameの使い方")
    screen = pygame.display.set_mode((960, 720))
    clock = pygame.time.Clock()
    ang = 0

    while True:
        tmr += 1
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_F1:
                    screnn = pygame.display.set_mode((960, 720), FULLSCREEN)
                if event.key == K_F2 or event.key == K_ESCAPE:
                    screnn = pygame.display.set_mode((960, 720))

        bg_y = (bg_y+16) % 720
        screen.blit(img_galaxy, [0, bg_y-720])
        screen.blit(img_galaxy, [0, bg_y])

        key = pygame.key.get_pressed()
        move_starship(screen, key)
        move_missile(screen)

        pygame.display.update()
        clock.tick(30)


if __name__ == "__main__":
    main()
