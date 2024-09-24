import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    kt_img = pg.image.load("fig/3.png")
    kt_img = pg.transform.flip(kt_img, True, False)
    tmr = 0

    kt_rect = kt_img.get_rect()
    kt_rect.center = 300,200


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = -(tmr%1600)
        screen.blit(bg_img, [x,0])
        screen.blit(pg.transform.flip(bg_img, True, False), [x+1600,0])
        screen.blit(bg_img, [x+3200,0])
        screen.blit(pg.transform.flip(bg_img, True, False), [x+4800,0])
        screen.blit(kt_img, kt_rect)

        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()