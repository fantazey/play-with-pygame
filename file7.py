import sys
import pygame
import pygame.locals as game_locals
import pygame.event as game_event

w_width = 600
w_height = 650

pygame.init()

surface = pygame.display.set_mode((w_width, w_height))
pygame.display.set_caption('Sounding')

SOUND_ASSETS_PATH = 'assets/file7/sounds'
IMAGE_ASSETS_PATH = 'assets/file7/images'


def build_image_path(name):
    return "%s/%s.png" % (IMAGE_ASSETS_PATH, name)


def build_sound_path(name):
    return "%s/%s.ogg" % (SOUND_ASSETS_PATH, name)


BUTTONS = []
STOP_BUTTON = {
    'image': pygame.image.load(build_image_path('stop')),
    'position': (275, 585)
}
MOUSE_POSITION = None
VOLUME = 1.0

pygame.mixer.init()
pygame.mixer.music.load(build_sound_path('farm'))
pygame.mixer.music.play(-1)


def draw_buttons():
    for button in BUTTONS:
        surface.blit(button['image'], button['position'])

    surface.blit(STOP_BUTTON['image'], STOP_BUTTON['position'])


def is_inside(point1, point2, size):
    inside_x = point2[0] < point1[0] < point2[0] + size[0]
    inside_y = point2[1] < point1[1] < point2[1] + size[1]
    return inside_x and inside_y


def draw_volume():
    pygame.draw.rect(surface, (229, 229, 229), (450, 610, 100, 5))
    volume_position = VOLUME * 100 + 450
    pygame.draw.rect(surface, (204, 204, 204), (volume_position, 600, 10, 25))


def handle_click():
    global MOUSE_POSITION, VOLUME
    for button in BUTTONS:
        button_size = button['image'].get_rect().size
        button_position = button['position']

        if is_inside(MOUSE_POSITION, button_position, button_size):
            button['sound'].set_volume(VOLUME)
            button['sound'].play(-1)

        stop_button_size = STOP_BUTTON['image'].get_rect().size
        if is_inside(MOUSE_POSITION, STOP_BUTTON['position'], stop_button_size):
            pygame.mixer.stop()


def check_volume():
    global VOLUME
    if pygame.mouse.get_pressed()[0] and is_inside(MOUSE_POSITION, (450, 600), (100, 25)):
        VOLUME = float((MOUSE_POSITION[0] - 450)) / 100


def quit_game():
    pygame.quit()
    sys.exit()


ANIMALS = [
    ('sheep', (25, 25)),
    ('rooster', (225, 25)),
    ('pig', (425, 25)),
    ('mouse', (25, 225)),
    ('horse', (225, 225)),
    ('dog', (425, 225)),
    ('cow', (25, 425)),
    ('chicken', (225, 425)),
    ('cat', (425, 425)),
]

for name, position in ANIMALS:
    BUTTONS.append({
        'image': pygame.image.load(build_image_path(name)),
        'position': position,
        'sound': pygame.mixer.Sound(file=build_sound_path(name))
    })


while True:
    surface.fill((255, 255, 255))
    MOUSE_POSITION = pygame.mouse.get_pos()
    for event in game_event.get():
        is_esc_pressed = event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        if is_esc_pressed or event.type == game_locals.QUIT:
            quit_game()

        if event.type == pygame.MOUSEBUTTONUP:
            handle_click()

    draw_buttons()
    check_volume()
    draw_volume()

    pygame.display.update()