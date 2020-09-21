import pygame, sys
import pygame.locals as GAME_LOCALS
import pygame.event as GAME_EVENTS

pygame.init()

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Hello pygame')

MOUSE_POSITION = None
MOUSE_CLICKED = False

DEFAULT_COLOR = (255, 0, 0)
DRAGGED_COLOR = (0, 255, 0)
COLOR = DEFAULT_COLOR
SIZE = 40
SQUARE_X = WINDOW_WIDTH / 2
SQUARE_Y = WINDOW_HEIGHT - SIZE
IS_DRAGGED = False
GRAVITY = 2


def check_bounds():
    global COLOR, SQUARE_X, SQUARE_Y, IS_DRAGGED
    if MOUSE_CLICKED:
        horizontal_check = SQUARE_X < MOUSE_POSITION[0] < SQUARE_X + SIZE
        vertical_check = SQUARE_Y < MOUSE_POSITION[1] < SQUARE_Y + SIZE
        if horizontal_check and vertical_check:
            IS_DRAGGED = True
            pygame.mouse.set_visible(0)
    else:
        COLOR = DEFAULT_COLOR
        IS_DRAGGED = False
        pygame.mouse.set_visible(1)


def check_gravity():
    global GRAVITY, SQUARE_Y, SIZE, WINDOW_HEIGHT
    if WINDOW_HEIGHT - SIZE > SQUARE_Y > WINDOW_HEIGHT - (SIZE * 3):
        GRAVITY = 0.9
        SQUARE_Y += GRAVITY
    elif SQUARE_Y < WINDOW_HEIGHT - SIZE and not MOUSE_CLICKED:
        SQUARE_Y += GRAVITY
        GRAVITY = GRAVITY * 1.1
    else:
        SQUARE_Y = WINDOW_HEIGHT - SIZE
        GRAVITY = 5


def draw_square():
    global COLOR, SQUARE_X, SQUARE_Y, IS_DRAGGED
    if IS_DRAGGED:
        COLOR = DRAGGED_COLOR
        SQUARE_X = MOUSE_POSITION[0] - SIZE / 2
        SQUARE_Y = MOUSE_POSITION[1] - SIZE / 2
    pygame.draw.rect(surface, COLOR, (SQUARE_X, SQUARE_Y, SIZE, SIZE))


def quit_game():
    pygame.quit()
    sys.exit()


def handle_events():
    for event in GAME_EVENTS.get():
        escape_down = event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        if escape_down or event.type == GAME_LOCALS.QUIT:
            quit_game()


while True:
    MOUSE_POSITION = pygame.mouse.get_pos()
    surface.fill((0, 0, 0))
    MOUSE_CLICKED = pygame.mouse.get_pressed()[0]
    check_bounds()
    check_gravity()
    draw_square()
    handle_events()
    pygame.display.update()
