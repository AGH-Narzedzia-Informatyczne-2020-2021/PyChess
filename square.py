import pygame as pg
import sys

screen = pg.display.set_mode((1280, 720))
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit(0)
    pg.draw.rect(screen, (255, 255, 255), pg.Rect(0, 0, 100, 100))
    pg.display.flip()
