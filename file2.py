import pygame
from math import cos, sin

pygame.init()

h = w = 600
window = pygame.display.set_mode((w, h))

color = (255, 255, 255)

center_x = int(w/2)
center_y = int(h/2)

X_DELIMETER = 20


def fix_y(y):
    return y * 20 + 400


def draw_sin():
    start_x = 0
    color_sin = (255, 0, 0)  # red
    start_sin_y = fix_y(sin(start_x / X_DELIMETER))
    for x in range(start_x, w, 1):
        sin_y = fix_y(sin(x / X_DELIMETER))
        pygame.draw.line(window, color_sin, (start_x, start_sin_y), (x, sin_y), 2)
        start_x, start_sin_y = x, sin_y


def draw_cos():
    start_x = 0
    color_cos = (0, 255, 0)  # green
    start_cos_y = fix_y(cos(start_x / X_DELIMETER))
    points = [(start_x, start_cos_y)]
    for x in range(start_x, w-1, 1):
        cos_y = fix_y(cos(x / X_DELIMETER))
        points.append((x, cos_y))
    pygame.draw.lines(window, color_cos, False, tuple(points), 1)


while True:
    pygame.draw.line(window, color, (0, 400), (w, 400), 1)
    pygame.draw.line(window, color, (60, 0), (60, h), 1)
    draw_sin()
    draw_cos()
    pygame.display.update()