import pygame, sys
import pygame.locals as GAME_LOCALS
import pygame.event as GAME_EVENTS

pygame.init()

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Hello pygame')

PLAYER_SIZE = 10
PLAYER_X = WINDOW_WIDTH / 2 - PLAYER_SIZE / 2
PLAYER_Y = WINDOW_HEIGHT - PLAYER_SIZE
PLAYER_VX = 0.1
PLAYER_VY = 0.0
JUMP_H = 25
MOVE_SPEED = 0.1
MOVE_SPEED_MAX = 2
GRAVITY = 0.5

LEFT_DOWN = False
RIGHT_DOWN = False
JUMPED = False


def move():
    global PLAYER_X, PLAYER_Y, PLAYER_VX, PLAYER_VY, JUMPED, GRAVITY
    if LEFT_DOWN:
        if PLAYER_VX > 0.0:
            PLAYER_VX = MOVE_SPEED
            PLAYER_VX = -PLAYER_VX
        if PLAYER_X > 0:
            PLAYER_X += PLAYER_VX
    if RIGHT_DOWN:
        if PLAYER_VX < 0:
            PLAYER_VX = MOVE_SPEED
        if PLAYER_X + PLAYER_SIZE < WINDOW_WIDTH:
            PLAYER_X += PLAYER_VX

    if PLAYER_VY > 1.0:
        PLAYER_VY = PLAYER_VY * 0.9
    else:
        PLAYER_VY = 0
        JUMPED = False

    if PLAYER_Y < WINDOW_HEIGHT - PLAYER_SIZE:
        PLAYER_Y += GRAVITY
        GRAVITY = GRAVITY * 1.1
    else:
        PLAYER_Y = WINDOW_HEIGHT - PLAYER_SIZE
        GRAVITY = 0.5

    PLAYER_Y -= PLAYER_VY

    if (PLAYER_VX > 0.0 and PLAYER_VX < MOVE_SPEED_MAX) or \
            (PLAYER_VX < 0 and PLAYER_VX > -MOVE_SPEED_MAX):
        if not JUMPED and (LEFT_DOWN or RIGHT_DOWN):
            PLAYER_VX = PLAYER_VX * 1.1


def quit_game():
    pygame.quit()
    sys.exit()


def main():
    pygame.draw.rect(surface, (255, 255, 255), (PLAYER_X, PLAYER_Y, PLAYER_SIZE, PLAYER_SIZE))


def handle_events():
    global LEFT_DOWN, RIGHT_DOWN, JUMPED, PLAYER_VY, PLAYER_VX
    for event in GAME_EVENTS.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                LEFT_DOWN = True
            if event.key == pygame.K_RIGHT:
                RIGHT_DOWN = True
            if event.key == pygame.K_UP:
                if not JUMPED:
                    JUMPED = True
                    PLAYER_VY += JUMP_H
            if event.key == pygame.K_ESCAPE:
                quit_game()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                LEFT_DOWN = False
                PLAYER_VX = MOVE_SPEED
            if event.key == pygame.K_RIGHT:
                RIGHT_DOWN = False
                PLAYER_VX = MOVE_SPEED

        if event.type == GAME_LOCALS.QUIT:
            quit_game()


while True:
    surface.fill((0, 0, 0))
    main()
    handle_events()
    move()
    pygame.display.update()
