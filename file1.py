import pygame

pygame.init()

w = h = 600
s = 100
window = pygame.display.set_mode((600, 600))

while True:
    colors = [
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
        (0, 255, 255),
        (255, 0, 255),
        (255, 255, 0),
        (255, 255, 255),
    ]
    x = 0
    color_index = 0
    while x <= w-s:
        y = 0
        while y <= h-s:
            color = colors[color_index]
            pygame.draw.rect(window, color, (x, y, s, s), 1)
            y += s
            color_index += 1

            if color_index > len(colors) - 1:
                color_index = 0
        x += s
    pygame.draw.circle(window, (0,0,0), ((int)(w/2), (int)(h/2)), s, 0)
    pygame.draw.ellipse(window, (255, 255, 255), ((int)(w / 2), (int)(h / 2), s/2, s*2))
    pygame.display.update()