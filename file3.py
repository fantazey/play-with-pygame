import pygame, sys, random
import pygame.locals as GAME_LOCALS
import pygame.event as GAME_EVENTS
import math

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Hello pygame')


def first():
    surface.fill((0, 0, 0))
    pygame.draw.rect(
        surface,
        (255, 0, 0),
        (
            random.randint(0, WINDOW_WIDTH),
            random.randint(0, WINDOW_HEIGHT),
            10,
            10
        ),
    )


GREEN_SQUARE_X = WINDOW_WIDTH / 2
GREEN_SQUARE_Y = WINDOW_HEIGHT / 2


def second():
    global GREEN_SQUARE_X, GREEN_SQUARE_Y
    surface.fill((0, 0, 0))
    pygame.draw.rect(
        surface,
        (0, 255, 0),
        (GREEN_SQUARE_X, GREEN_SQUARE_Y, 10, 10),
    )
    GREEN_SQUARE_X += 1

    if GREEN_SQUARE_X > WINDOW_WIDTH:
        GREEN_SQUARE_X = 0

    GREEN_SQUARE_Y += 1
    if GREEN_SQUARE_Y > WINDOW_HEIGHT:
        GREEN_SQUARE_Y = 0


SINUS_TIME = 1


def animated_sin():
    def calc_sin(x):
        return math.sin(x / 20) * 100 + 400
    global SINUS_TIME
    start_x = SINUS_TIME
    start_y = calc_sin(start_x)
    color = (255, 255, 255)
    sin_x = SINUS_TIME + 1
    sin_y = calc_sin(sin_x)
    pygame.draw.line(surface, color, (start_x, start_y), (sin_x, sin_y))

    SINUS_TIME += 1
    if SINUS_TIME > WINDOW_WIDTH:
        SINUS_TIME = 0


COS_TIME = 1


def animated_cos():
    def calc_cos(x):
        return math.cos(x / 20) * 100 + 200
    global COS_TIME
    start_x = 0
    start_y = calc_cos(start_x)
    color = (
        COS_TIME % 255,
        random.randint(COS_TIME % 255, 255),
        random.randint(0, 255),
    )
    for x in range(1, WINDOW_WIDTH, 1):
        sin_y = calc_cos(x + COS_TIME)
        pygame.draw.line(surface, color, (start_x, start_y), (x, sin_y))
        start_x, start_y = x, sin_y

    COS_TIME += 1
    if COS_TIME > 1000000:
        COS_TIME = 0


BLUE_S_X = BLUE_S_Y = 100
BLUE_S_SPEED_X = 1
BLUE_S_SPEED_Y = 1


def third():
    global BLUE_S_X, BLUE_S_Y, BLUE_S_SPEED_X, BLUE_S_SPEED_Y
    color = (0, 0, 255)
    pygame.draw.rect(surface, color, (BLUE_S_X, BLUE_S_Y, 10, 10))
    BLUE_S_X = BLUE_S_X + BLUE_S_SPEED_X
    BLUE_S_Y = BLUE_S_Y + BLUE_S_SPEED_Y
    BLUE_S_SPEED_X -= 0.004
    BLUE_S_SPEED_Y += 0.002

    if BLUE_S_Y < 0 or BLUE_S_Y > WINDOW_HEIGHT or \
            BLUE_S_X < 0 or BLUE_S_X > WINDOW_WIDTH:
        BLUE_S_X = 100
        BLUE_S_Y = 100
        BLUE_S_SPEED_X = 1
        BLUE_S_SPEED_Y = 1


RECT_F_X = WINDOW_WIDTH / 2
RECT_F_Y = WINDOW_HEIGHT / 2
RECT_F_W = 50
RECT_F_H = 50


def fourth():
    global RECT_F_H, RECT_F_W
    pygame.draw.rect(
        surface,
        (255, 255, 255),
        (RECT_F_X - RECT_F_W / 2, RECT_F_Y - RECT_F_H / 2, RECT_F_W, RECT_F_H)
    )
    RECT_F_W -= 0.5
    RECT_F_H += 1


def handle_events():
    for event in GAME_EVENTS.get():
        if event.type == GAME_LOCALS.QUIT:
            pygame.quit()
            sys.exit()


while True:
    surface.fill((0, 0, 0))
    # first()
    # second()
    # animated_sin()
    # animated_cos()
    # third()
    fourth()
    handle_events()
    pygame.display.update()
